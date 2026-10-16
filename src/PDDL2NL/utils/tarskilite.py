
import itertools
import json
import time
import os, re
from collections import defaultdict

import tarski
from tarski.io import PDDLReader
from tarski.io import fstrips as iofs
from tarski.syntax.formulas import is_atom
from tarski.syntax.transform.action_grounding import ground_schema_into_plain_operator_from_grounding
from tarski.io import FstripsWriter


from tarski.search import GroundForwardSearchModel
from tarski.grounding.lp_grounding import (
    ground_problem_schemas_into_plain_operators,
    LPGroundingStrategy,
)
from tarski.util import SymbolIndex
from tarski.grounding.common import StateVariableLite
from tarski.grounding.naive_grounding import NaiveGroundingStrategy

from PDDL2NL.utils.cpddl_util import get_LMGs_with_counting_variables, get_actions_with_mutex_preconditions
from PDDL2NL.utils.translation_util import get_pddl_domain

from pddl import parse_domain, parse_problem
from pddl.core import Problem
from pddl.logic.base import Atomic, UnaryOp, BinaryOp, And, Not
from pddl.logic import Predicate
from pddl.parser.domain import DomainParser
from pddl.parser.problem import ProblemParser

def entails(state, partialstate):
    return partialstate <= state

def progress(state, act):
    assert entails(state, act.pres), "Cannot progress with inconsistent state / action precondition:\n\t Action: "+act.name+"\n\t State: \n\t\t"+'\n\t\t'.join(state)
    return (state - act.dels) | act.adds

def regress(state, act):
    assert len(state & act.dels) == 0, f"Cannot regress with inconsistent state / action delete effect:\n\t Action: "+act.name+"\n\t State: \n\t\t"+'\n\t\t'.join(state)
    return (state - act.adds) | act.pres


def parse_lmg_variables(lmg):
    fixed, counting= {}, {}
    variables = defaultdict(list)
    for atom_idx, a in enumerate(lmg):
            for i, v in enumerate(a[1:]):
                if v.startswith("C") and ":" in v:
                    counting[(atom_idx, i)] = v
                    variables[v].append((atom_idx, i))
                elif v.startswith("V") and ":" in v:
                    fixed[(atom_idx, i)] = v
                    variables[v].append((atom_idx, i))
                else:
                    fixed[(atom_idx, i)]=  v
    return counting, fixed, variables

def fix_name(s):
    # (act param)
    if '(' == s[0] and ')' == s[-1]:
        return s[1:-1]
    # make it space separated
    s = s.replace(', ', ' ').replace(',', ' ')
    # act(param)
    if '(' in s:
        assert ')' == s[-1], f"Broken name? {s}"
        s = s.replace('(', ' ').replace(')', '')
    # act param
    return s






class Action:
    def __init__(self, name, pre, add, delete):
        self.name = name
        self.pres = pre
        self.adds = add
        self.dels = delete

    def __str__(self):
        pres = "{" + ", ".join([f"({a})" for a in self.pres]) + "}"
        adds = "{" + ", ".join([f"({a})" for a in self.adds]) + "}"
        dels = "{" + ", ".join([f"({a})" for a in self.dels]) + "}"

        return f"< {self.name}, {pres}, {adds}, {dels} >"

    def toJSON(self):
        return json.dumps(
            { "name": self.name, "preconditions": [f"({a})" for a in self.pres], "add_effects": [f"({a})" for a in self.adds], "delete_effects": [f"({a})" for a in self.dels] },
            sort_keys=True,
            indent=4)

    def __repr__(self):
        return self.name
    
    def __eq__(self, action):
        return self.name == action.name
    

    def __hash__(self):
        return hash(self.name)

class STRIPS:
    def __init__(self, domain, problem, compute_LMG=False, 
                 compute_unreachable_facts=False, compute_unreachable_actions=False):
        self.domain_file = domain 
        self.problem_file = problem
        self.reader = PDDLReader(raise_on_error=True)
        self.reader.parse_domain(domain)
        self.problem = self.reader.parse_instance(problem)
        self.relaxed_unreachable_actions_groundings = {}
        self.relaxed_unreachable_actions_groundings_exist = None
        self.exist_unreachable_actions = None
        (self.grounded_fluents, init, goal, self.operators, self.grounder) = self.ground_problem(self.problem, compute_unreachable_actions)

        self.fluents = set([fix_name(str(f)) for f in self.grounded_fluents])
        self.fluents_map = dict()
        for f in self.grounded_fluents:
            self.fluents_map[fix_name(str(f))] = f
        self.init = set([fix_name(str(f)) for f in init])
        self.goal = set([fix_name(str(f)) for f in goal])
        self.actions = set()
        self.action_map = {}
        self.init_fluents = [self.fluents_map[f] for f in self.init]

        # self.grounder = LPGroundingStrategy(problem=self.problem, include_variable_inequalities=True)
        self.static_predicates = [ i.name for i in self.grounder.static_symbols]
        for op in self.operators:
            act = self.operator_to_action(op)
            self.actions.add(act)
            self.action_map[act.name.lower()] = act

        self.lmgs = None
        self.relaxed_unreachable_facts = None
        self.relaxed_unreachable_actions = None
        self.mutex_pre_actions = None
        self.mgs = {}
        self.invertible_dict = None

        self.unreachable_facts_computed = False
        self.unreachable_actions_computed = False

        if compute_LMG:
            self.compute_LMG()

        if compute_unreachable_facts:
            self.compute_unreachable_facts()

        if compute_unreachable_actions:
            self.compute_unreachable_actions()
    def __str__(self):
        fluents = "P = {" + ", ".join([f"({a})" for a in self.fluents]) + "}"
        init = "I = {" + ", ".join([f"({a})" for a in self.init]) + "}"
        goal = "G = {" + ", ".join([f"({a})" for a in self.goal]) + "}"
        actions = "A = {" + "\n ".join([a.__str__() for a in self.actions]) + "}"
        return fluents + ",\n" + init + "\n" + goal + "\n" + actions

    def toJSON(self):
        actions = [a.toJSON() for a in self.actions]
        return json.dumps( 
            { "fluents": list(self.fluents), "initial_state": list(self.init), "goal": list(self.goal), "actions": actions },
            sort_keys=True,
            indent=4)

    # Not used anymore 
    # def is_relaxed_unreachable_actions_groundings_exist(self):
    #     self.compute_unreachable_facts()
    #     # Removed - this is not true - mutex preconditions are reachable
    #     # if len(self.relaxed_unreachable_facts) == 0:
    #     #     # All facts are reachable, all actions will be reachable
    #     #     # print("All facts are reachable, all actions will be reachable")
    #     #     return False
    #     if self.relaxed_unreachable_actions_groundings_exist is None:
    #         # Approximating if valid relaxed_unreachable_actions_groundings exist
    #         # Trying to get a 100 random actions, if none returned, then none assumed to exist
    #         # print("Approximating relaxed unreachable action groundings")
    #         import random
    #         gr = self.get_random_unreachable_action_groundings(random, k=1000)
    #         self.relaxed_unreachable_actions_groundings_exist = len(gr) > 0
    #     return self.relaxed_unreachable_actions_groundings_exist

    def operator_to_action(self, op, check_fluents= True, check_static=False):
        adds = {fix_name(str(f.atom)) for f in op.effects if isinstance(f, iofs.AddEffect)} & self.fluents
        dels = {fix_name(str(f.atom)) for f in op.effects if isinstance(f, iofs.DelEffect)} & self.fluents
        pre = self.fix_pre_name(op.precondition) 
        if check_fluents:
            pre = pre & self.fluents
        if check_static:
            pre = {p for p in pre if p.split()[0] not in self.static_predicates}
        act = Action(fix_name(str(op)), pre, adds, dels)
        return act


    def compute_LMG(self):
        self.lmgs = get_LMGs_with_counting_variables(self.domain_file, self.problem_file)
        
    def get_grounded_mutex_groups(self, lmg):
        counting, fixed, _ = parse_lmg_variables(lmg)
        mutex_groups = []
        counting_domain, fixed_domain = {}, {}
        for index, variable in counting.items():
            counting_domain[variable] = list([ s for s in self.problem.language.sorts if s.name == variable.split(":")[-1]][0].domain())
        for index, variable in fixed.items():
            if ':' not in variable:
                fixed_domain[variable] = [i for i in self.problem.language.constants() if i.name == variable]
                continue
            fixed_domain[variable] = list([ s for s in self.problem.language.sorts if s.name == variable.split(":")[-1]][0].domain())
        for f in itertools.product(*list(fixed_domain.values())):
            mutex_group = set()
            fixed_binding = dict(zip(fixed_domain.keys(),f))
            for c in itertools.product(*list(counting_domain.values())):
                counted_binding = dict(zip(counting_domain.keys(), c))
                counted_binding.update(fixed_binding)
                for atom in lmg:
                    atom_symbol = [s for s in  self.fluent_symbols() if s.name==atom[0]][0]
                    atom_binding = tuple([counted_binding[p] for p in atom[1:]])
                    mutex_group.add(fix_name(str(StateVariableLite(atom_symbol, atom_binding ).to_atom())))
            mutex_groups.append(mutex_group)
        return mutex_groups

    # # Not called, disabled
    # def compute_MGs(self):
    #     if self.lmgs is None:
    #         self.compute_LMG()
    #     self.mgs=[]
    #     for lmg in self.lmgs:
    #         self.mgs += self.get_grounded_mutex_groups(lmg)

    def compute_reachable_facts(self):
        relaxed_reachable = []
        for symbol in self.fluent_symbols():
            relaxed_reachable.extend([fix_name(x) for x in self.get_grounded_atoms(symbol).dump()])
        return relaxed_reachable
        
    def compute_unreachable_facts(self):
        if self.unreachable_facts_computed:
            return
        self.relaxed_unreachable_facts = set()
        for symbol in self.fluent_symbols():
            all_groundings = [fix_name(str(StateVariableLite(symbol, binding).to_atom()))  for binding in itertools.product(*[s.domain() for s in symbol.domain])]
            relaxed_reachable = [fix_name(x) for x in self.get_grounded_atoms(symbol).dump()]
            # print(f"All groundings {len(all_groundings)}, relaxed reachable {len(relaxed_reachable)}")
            self.relaxed_unreachable_facts |= (set(all_groundings) - set(relaxed_reachable))
        self.unreachable_facts_computed = True

    def compute_unreachable_actions(self):
        if self.unreachable_actions_computed:
            return
        s_time = time.time()
        if self.relaxed_unreachable_facts is None:
            self.compute_unreachable_facts()
        # self.relaxed_unreachable_actions = []
        print(f"Got {len(self.relaxed_unreachable_facts)} relaxed unreachable facts in {(time.time() - s_time):0.2f} seconds.")
        
        s_time = time.time()
        if self.lmgs is None:
            self.compute_LMG()
        print(f"Got {len(self.lmgs)} lifted mutex groups in {(time.time() - s_time):0.2f} seconds.")
        
        s_time = time.time()
        list_mutex_actions, list_lmg = get_actions_with_mutex_preconditions(self.domain_file, self.problem_file)
        print(f"Got {len(list_mutex_actions)} mutex actions with CPDDL in {(time.time() - s_time):0.2f} seconds.")
        # print("Mutex actions: ")
        # print(list_mutex_actions)
        # print("Mutex groups: ")
        # print(list_lmg)
        self.mutex_pre_actions = []
        
        s_time = time.time()
        mutex_groups_per_action_name = {}
        for aname, action in self.problem.actions.items():
            mutex_action_idx = None
            mutex_groups = None
            if aname.lower() in list_mutex_actions:
                mutex_action_idx = list_mutex_actions.index(aname.lower())
                lmg_key = str(list_lmg[mutex_action_idx])
                if lmg_key not in self.mgs:
                    self.mgs[lmg_key] = self.get_grounded_mutex_groups(list_lmg[mutex_action_idx])
                mutex_groups = self.mgs[lmg_key]
                mutex_groups_per_action_name[aname.lower()] = mutex_groups
            # print(f"action {aname} first step took {(time.time() - s_time):0.2f} seconds.")
            # print(f"Number of mutex groups is {len(mutex_groups) if mutex_groups is not None else 0}.")
        print(f"First step took {(time.time() - s_time):0.2f} seconds.")
        # Now, going over relaxed reachable actions only, looking for mutexes
        s_time = time.time()
        # print(mutex_groups_per_action_name.keys())
        for aname, action in self.action_map.items():
            lifted_name = aname.split(" ")[0]
            # print(aname, lifted_name)
            if lifted_name in  mutex_groups_per_action_name:
                for mg in mutex_groups_per_action_name[lifted_name]:
                    # print(f'Mutex group {mg}')
                    # print(f'Action precondition {action.pres}')
                    mutex_preconditions = action.pres & mg
                    # print(lifted_name, mutex_preconditions)
                    if len(mutex_preconditions) > 1:
                        self.mutex_pre_actions.append(tuple([action, mutex_preconditions]))
                        break
        print(f"Mutex computation took {(time.time() - s_time):0.2f} seconds, found {len(self.mutex_pre_actions)} actions with mutex preconditions.")
        self.unreachable_actions_computed = True            


    def fix_pre_name(self, precondition):
        if not is_atom(precondition):
            return {fix_name(str(f)) for f in precondition.subformulas}
        return {fix_name(str(precondition))} 

    def action(self, name):
        return self.action_map[fix_name(name).lower()]

    def get_action_or_none(self, name):
        if '(' in name and ')' != name[-1]:
            return None
        return self.action_map.get(fix_name(name).lower(), None)

    def fluent(self, name):
        return fix_name(name)
    
    def static_symbols(self):
        return list(self.grounder.static_symbols)
    
    def fluent_symbols(self):
        return list(self.grounder.fluent_symbols)

    def get_atom_counts(self, symbol):
        key = 'atom_' + symbol.name
        return len(self.grounder._solve_lp()[key])

    def get_grounded_atoms(self, symbol):
        variables = SymbolIndex()
        lang = symbol.language
        key = 'atom_' + symbol.name
        model = self.grounder._solve_lp()
        if key in model:  # in case there is no reachable ground state variable from that fluent symbol
            for binding in model[key]:
                binding_with_constants = tuple(lang.get(c) for c in binding)
                variables.add(StateVariableLite(symbol, binding_with_constants))
        return variables

    def parse_plan(self, plan):
        # check if it's a file
        if os.path.isfile(plan):
            with open(plan) as f:
                anames = f.read().strip().split('\n')
        # check if it's a string
        elif isinstance(plan, str):
            anames = plan.strip().split('\n')
        # check if it's a list
        elif isinstance(plan, list):
            anames = plan
        else:
            raise Exception("Unknown plan type")
        return [self.action(a) for a in anames]

    def get_applicable_actions(self, s):
        return [a for a in self.actions if entails(s, a.pres)]

    def execute(self, _actions : list):
        current_state = self.init
        real_plan = []
        for action in _actions:
            applicable_actions = self.get_applicable_actions(current_state)
            app_actions_list = [a.name.lower() for a in applicable_actions]
            assert action.lower() in app_actions_list, f"{action} is not in {applicable_actions}"
            a = applicable_actions[app_actions_list.index(action.lower())]
            current_state = progress(current_state, a)
            real_plan.append(a)
        return real_plan


    def get_random_unreachable_action_groundings(self, random, k):
        num_groundings = 0
        for _, groundings in self.relaxed_unreachable_actions_groundings.items():
            num_groundings += len(groundings)
        if num_groundings <= k:
            # Getting all that are there
            ret = []
            for action_name, groundings in self.relaxed_unreachable_actions_groundings.items():
                for grounding in groundings:
                    t = self.get_unreachable_action(action_name, grounding)
                    if len(t[1]) > 0:
                        ret.append(t)
            return ret
        ret = set()
        num_tries = 0
        empty_pre = set()
        # while len(ret) < k and num_tries < k*3:
        while len(ret) < k and len(empty_pre) + len(ret) < num_groundings and num_tries < 100:
            num_tries += 1
            action_name = random.choice(list(self.relaxed_unreachable_actions_groundings.keys()))
            grounding = random.choice(self.relaxed_unreachable_actions_groundings[action_name])
            # print(action_name, grounding)
            t = self.get_unreachable_action(action_name, grounding)
            # print(t)
            if len(t[1]) == 0:
                empty_pre.add(t)
                continue
            # print(type(t), t)
            ret.add(t)
        # print(len(ret))
        return list(ret)
    
    # Not used
    # def get_unreachable_actions_groundings(self, action_name):
    #     return self.relaxed_unreachable_actions_groundings[action_name]

    def get_unreachable_action(self, action_name, grounding):
        action = self.problem.get_action(action_name)
        op = ground_schema_into_plain_operator_from_grounding(action, grounding)
        upre = self.fix_pre_name(op.precondition)
        if self.relaxed_unreachable_facts is not None:
            # print(self.relaxed_unreachable_facts)
            upre &= self.relaxed_unreachable_facts
        return tuple([self.operator_to_action(op, check_fluents=False, check_static=True), tuple(sorted(list(upre)))])
    
    def ground_problem(self, problem, compute_unreachable_actions):
        # operators = ground_problem_schemas_into_plain_operators(problem)
        # instance = GroundForwardSearchModel(problem, operators)
        grounder = LPGroundingStrategy(problem, include_variable_inequalities=True)
        action_groundings = grounder.ground_actions()
        operators = []
        for action_name, groundings in action_groundings.items():
            action = problem.get_action(action_name)
            for grounding in groundings:
                # print(type(grounding[0]), grounding)
                operators.append(ground_schema_into_plain_operator_from_grounding(action, grounding))

            num_groundings = 1
            # Check the number of groundings
            for p in action.parameters:
                num_groundings *= len(list(p.sort.domain()))
            if len(groundings) < num_groundings:
                self.exist_unreachable_actions = True
                # print(f'Number of groundings of action {action_name} is {num_groundings}, out of those {len(groundings)} are reachable')

            # Add groundings that are NOT relaxed reachable 
            if compute_unreachable_actions:
                domains = [list(p.sort.domain()) for p in action.parameters]
                # Getting up to 1k unreachable groundings
                num_to_keep = min(1000 + len(groundings), num_groundings)
                # print(f'Generating {num_to_keep} groundings')
                all_groundings = set()
                candidates = []
                import random
                if num_groundings < 100000:
                    candidates = random.sample(list(itertools.product(*domains)), k=num_to_keep)
                    for p in candidates:
                        g = [x.name for x in p]
                        if len(set(g)) == len(g) or True:
                            all_groundings.add(tuple(g))
                else:
                    r = split_domains(domains, 10)
                    ind = list(range(len(r)))
                    random.shuffle(ind)
                    for i in ind:
                        if len(all_groundings) > num_to_keep:
                            break

                        groundings_chunk = list(itertools.product(*r[i]))
                        l = min(len(groundings_chunk), num_to_keep)
                        candidates = random.sample(groundings_chunk, k=l)
                        for p in candidates:
                            g = [x.name for x in p]
                            if len(set(g)) == len(g) or True:
                                all_groundings.add(tuple(g))
                
                # all_groundings = set([tuple([x.name for x in p]) for p in itertools.product(*domains)])
                # print(f"All groundings: {action_name}")
                # for a in all_groundings:
                #     print(a)
                # print("--------------")
                # print([x.name for x in all_groundings[0]])
                relaxed_unreachable_groundings = all_groundings - groundings
                # print(f"Action {action_name}, number of groundings {num_groundings}, reachable: {len(groundings)}, relaxed unreachable: {len(relaxed_unreachable_groundings)}")        
                # Keep the groundings
                if len(relaxed_unreachable_groundings) > 0:
                    self.relaxed_unreachable_actions_groundings[action_name] = list(relaxed_unreachable_groundings)
        if self.exist_unreachable_actions is None:
            self.exist_unreachable_actions = False
        grounded_fluents = set([grounded_fluent.to_atom() for grounded_fluent in grounder.ground_state_variables().objects])
        init = [f for f in problem.init.as_atoms() if f in grounded_fluents]
        if isinstance(problem.goal, tarski.syntax.Atom):
            goal = [problem.goal]
        else:
            goal = [f for f in problem.goal.subformulas if f in grounded_fluents]

        return (grounded_fluents, init, goal, operators, grounder)


    def get_total_num_groundings(self):
        num_groundings = 0
        for action_name, action in self.problem.actions.items():
            num_groundings+= self.get_total_num_action_groundings(action)
        return num_groundings

    def get_total_num_action_groundings(self, action):
        num_groundings = 1
        # Check the number of groundings
        domains = [list(p.sort.domain()) for p in action.parameters]
        for p in domains:
            num_groundings *= len(list(p))
        return num_groundings

    def check_invertible(self, a, b):
        # del in pre, add not in pre (for both actions)
        # add(a) == del(b), add(b) == del(a)
        # pre(a)\del(a)+add(a)==pre(b) 
        # pre(b)\del(b)+add(b)==pre(a) 
        if len(a.dels - a.pres) > 0 or len(a.adds & a.pres) > 0:
            return False
        if len(b.dels - b.pres) > 0 or len(b.adds & b.pres) > 0:
            return False
        if a.dels != b.adds or b.dels != a.adds:
            return False
        if ((a.pres - a.dels) | a.adds) != b.pres: 
            return False
        if ((b.pres - b.dels) | b.adds) != a.pres: 
            return False
        return True

    def compute_invertible_pairs(self):
        if self.invertible_dict is not None:
            return
        self.invertible_dict = {}
        for a, b in itertools.combinations(self.actions, 2):
            if self.check_invertible(a,b):
                if a.name not in self.invertible_dict:
                    self.invertible_dict[a.name] = []
                self.invertible_dict[a.name].append(b.name)
                if b.name not in self.invertible_dict:
                    self.invertible_dict[b.name] = []
                self.invertible_dict[b.name].append(a.name)

    def get_invertible_actions(self, a):
        self.compute_invertible_pairs()
        if a.name in self.invertible_dict:
            return self.invertible_dict[a.name]
        return []

    def naive_grounding_variables(self):
        grounding = NaiveGroundingStrategy(self.problem)
        return grounding.ground_state_variables()
    
    def domain_to_PDDL(self):
        writer = FstripsWriter(self.problem)
        return writer.print_domain().replace(":numeric-fluents","")

    def problem_to_PDDL(self):
        writer = FstripsWriter(self.problem)
        return writer.print_instance()



    def PDDL_replace_init(self, s):
        new_reader = PDDLReader(raise_on_error=True)
        new_reader.parse_domain(self.domain_file)
        new_problem = new_reader.parse_instance(self.problem_file)
        for p in self.init:
            p = self.fluents_map[p]
            new_problem.init.remove(p.predicate, *p.subterms)
        for p in s:
            p = self.fluents_map[p]
            new_problem.init.add(p)
        writer = FstripsWriter(new_problem)

        if "alfworld" not in self.domain_file:
            return writer.print_domain().replace(":numeric-fluents",""), writer.print_instance()
        else:
            # Hack - in Alfworld, Tarski does not produce a valid domain due to constants, 
            # so copying from the original domain file instead
            # and removing constants from the list of objects in the problem file
            d = get_pddl_domain("alfworld")

            prob = writer.print_instance().split("\n")
            for i, line in enumerate(prob):
                if " - otype" in line:
                    prob[i] = line.replace("butterknifetype ", "").replace("knifetype ", "").replace("sinktype ", "")
                if " - rtype" in line:
                    prob[i] = line.replace("fridgetype ", "").replace("microwavetype ", "").replace("sinkbasintype ", "")
            return d, " \n".join(prob)

    def get_static(self):
        static_symbols = self.static_symbols()
        ret = []
        for symbol in static_symbols:
            ret.extend(self.get_grounded_atoms(symbol))
        return set([fix_name(str(x)) for x in ret])

    def PDDL_replace_init_pddl_parser(self, s, g=None):
        # d = parse_domain(self.domain_file)
        # p = parse_problem(self.problem_file)

        d = DomainParser()(open(self.domain_file, "r").read().lower())
        p = ProblemParser()(open(self.problem_file, "r").read().lower())

        # print(self.init)
        # print("-------------------")
        # print(s)
       
        new_state = get_atoms_pddl(d, p, s | self.get_static())
        

        if g is None:
            new_p = Problem(p.name, domain=d,
                        objects=p.objects,
                        init=new_state,
                        goal=p.goal)

        else:
            goal = And(*get_atoms_pddl(d, p, g))
            new_p = Problem(p.name, domain=d,
                        objects=p.objects,
                        init=new_state,
                        goal=goal)

        return d, new_p
    

    def PDDL_pddl_parser(self):
        d = DomainParser()(open(self.domain_file, "r").read().lower())
        p = ProblemParser()(open(self.problem_file, "r").read().lower())
        return d, p

def get_positive_preds(eff):
    if isinstance(eff, Predicate):
        return [eff]
    if isinstance(eff, And):
        ret = []
        for c in eff.operands:
            ret.extend(get_preds(c))
        return ret
    if isinstance(eff, Not):
        return []



def get_preds(eff):
    if isinstance(eff, Predicate):
        return [eff.name]
    if isinstance(eff, And):
        ret = []
        for c in eff.operands:
            ret.extend(get_preds(c))
        return ret
    if isinstance(eff, Not):
        return get_preds(eff.argument)

# def is_atom_in_eff(f, a):
#     if isinstance(a.effect, Atomic):
#         return a.effect.argument.name == f.name
    
#     for e in a.effect.operands:
#         if e.name == f.name:
#             return True
#     return False

# def is_static_predicate_pddl(d, f):
#     for a in d.actions:
#         if is_atom_in_eff(f, a):
#             return False
#     return True

def get_static_predicates_pddl(d, p):
    non_static = []
    for a in d.actions:
        non_static.extend(get_preds(a.effect))

    non_static = set(non_static)

    ret = []

    for f in p.init:
        if f.name not in non_static:
            ret.append(f)
    return ret

def get_atoms_pddl(d, p, atoms):
    # print(atoms)
    objs = set()
    preds = defaultdict(list)
    for atom in atoms:
        a = atom.lower().strip().split(" ")
        args = a[1:]
        # print(f"atom name |{a[0]}|")
        preds[a[0]].append(args)
        objs |= set(args)
    # print(preds)

    constants = [o for o in p.objects | d.constants if o.name.lower() in objs]
    constants_dict = {}
    for c in constants:
        constants_dict[c.name.lower()] = c
    assert len(objs) == len(constants), f"Could not identify all objects: {objs - set(constants_dict.keys())} not found, {set(constants_dict.keys()) - objs} should not be there"

    state = []
    covered_preds = set()
    for f in d.predicates:
        name = f.name.lower()
        # print(f"Checking predicate |{name}|")
        if name in preds:
            covered_preds.add(name)
            assert len(preds[name][0]) == f.arity, f"The arity does not match: {preds[name]} vs {f.terms}"
            # Going over the lists of objects, adding ground predicate for each 
            # print(f.name, preds[f.name])
            for ob in preds[name]:
                c = [ constants_dict[o] for o in ob]
                # print("f: ", f, type(f), [x.type_tags for x in f.terms])
                # print("c: ", c, [type(x) for x in c], [x.type_tags for x in c])
                state.append(f(*c))

    assert len(covered_preds) == len(preds.keys()), f"Covered predicates: \n{sorted(list(covered_preds))} vs \n{sorted(list(preds.keys()))}"        
    return set(state)

def split_domains(domains, dom_size):
    splits = []
    for d in domains:
        splits.append([ d[i:i + dom_size]   for i in range(0, len(d), dom_size) ])

    # print(f'Splitting {len(domains)} domains {[len(d) for d in domains]}')
    # for i, r in enumerate(splits):
    #     print(f'{i}: {[len(d) for d in r]}')
    res = list(itertools.product(*splits))
    # for i, r in enumerate(res):
    #     print(f'{i}: {[len(d) for d in r]}')
    return res

def product(*iterables):
    for x in iterables:
        print(list(x))
    doms = [len(list(x)) for x in iterables]
    print(doms)
    res = list(itertools.product(*iterables))
    print(len(res))
    return res

def get_num_groundings(domains):
    num_groundings = 1
    # Check the number of groundings
    for p in domains:
        num_groundings *= len(list(p))