import tempfile

from pathlib import Path 
from forbiditerative import planners as fi
from kstar_planner import planners as kp

from pddl.logic import Predicate, constants, variables
from pddl.core import Domain, Problem
from pddl.parser.domain import DomainParser
from pddl.parser.problem import ProblemParser

from pddl.action import Action
from pddl.requirements import Requirements

from PDDL2NL.utils.tarski_utils import get_tarski_problem
from PDDL2NL.utils.tarskilite import get_preds



def get_atom_pddl(d, p, atom):
    a = atom.strip().split(" ")
    name = a[0]
    args = a[1:]
    constants = [o for o in p.objects | d.constants if o.name.lower() in args]
    assert len(args) == len(constants), f"Could not identify all objects: {args} vs {p.objects| d.constants}"
    
    for f in d.predicates:
        if f.name == name:
            assert len(args) == f.arity, f"The arity does not match: {args} vs {f.terms}"
            return f, constants
    
    return None, None

def is_atom_in_eff(f, a):
    if f.name in get_preds(a.effect):
        return True
    return False



def create_is_landmark_task(domain, problem, atom):
    # In order to check whether one atom (P x1,...,xk) (that is not true initially or required in goal) is a landmark, 
    # we perform the following manipulation of the planning task:
    # 1. Each action that has the lifted atom (P ?a1,...,?ak) in effect is added (not (__nachieved__P ?a1,...,?ak)) to the effect as well.
    # 2. The initial state and the goal are extended with (__nachieved__P x1,...,xk)

    # print(f'Atom: {atom}')
    d = DomainParser()(domain)
    # print("Domain parsed")
    p = ProblemParser()(problem)
    # print("Problem parsed")
    f, args = get_atom_pddl(d, p, atom)
    achf = Predicate(f"X__nachieved__{f.name}", *f.terms)
    ground_achf = achf(*args)
    actions = []
    for a in d.actions:
        if is_atom_in_eff(f, a):
            b =  Action(a.name, parameters=a.parameters,
                                precondition=a.precondition,
                                effect=a.effect & ~achf)
            actions.append(b)
        else:
            actions.append(a)

    # define the domain object.
    requirements = [Requirements.TYPING, Requirements.ADL]
    new_d = Domain(d.name,
                requirements=requirements,
                types=d.types,
                constants=d.constants,
                predicates=list(d.predicates) + [achf],
                actions=actions)
    new_p = Problem(p.name, domain=new_d,
                    requirements=requirements,
                    objects=p.objects,
                    init=list(p.init) + [ground_achf],
                    goal=p.goal & ground_achf)

    return new_d, new_p

# This version is replaced by the version above
# def create_is_landmark_task(domain, problem, atom):
#     # In order to check whether one atom (P x1,...,xk) (that is not true initially or required in goal) is a landmark, 
#     # we perform the following manipulation of the planning task:
#     # 1. Each action that has the lifted atom (P ?a1,...,?ak) in effect is added (__achieved__P ?a1,...,?ak) to the effect as well.
#     # 2. The goal is extended with (not (__achieved__P x1,...,xk))

#     # print(f'Atom: {atom}')
#     d = DomainParser()(domain)
#     # print("Domain parsed")
#     p = ProblemParser()(problem)
#     # print("Problem parsed")
#     f, args = get_atom_pddl(d, p, atom)
#     achf = Predicate(f"X__achieved__{f.name}", *f.terms)
#     ground_achf = achf(*args)
#     actions = []
#     for a in d.actions:
#         if is_atom_in_eff(f, a):
#             b =  Action(a.name, parameters=a.parameters,
#                                 precondition=a.precondition,
#                                 effect=a.effect & achf)
#             actions.append(b)
#         else:
#             actions.append(a)

#     # define the domain object.
#     requirements = [Requirements.TYPING, Requirements.ADL]
#     new_d = Domain(d.name,
#                 requirements=requirements,
#                 types=d.types,
#                 constants=d.constants,
#                 predicates=list(d.predicates) + [achf],
#                 actions=actions)
#     new_p = Problem(p.name, domain=new_d,
#                     requirements=requirements,
#                     objects=p.objects,
#                     init=p.init,
#                     goal=p.goal & ~ground_achf)

#     return new_d, new_p


def check_is_landmark(domain, problem, atom):
    P = get_tarski_problem(domain, problem)
    if P is None:
        # Unsolvable
        return False
    
    state = [f'({f})' for f in P.init]
    # print(f'Atom: {atom}')
    # print(f'Init: {state}')

    if atom in state:
        # print(f'Trivial landmark: {atom}, holds in init')
        return False
        
    goal = [f'({f})' for f in P.goal]

    if atom in goal:
        # print(f'Trivial landmark: {atom}, holds in goal')
        return False

    # Check valid atom
    if not atom.startswith("(") or not atom.endswith(")"):
        return False

    atom = atom[1:-1]
    if atom not in P.fluents:
        # print(f'Not part of the problem: {atom}, all atoms are {P.fluents}')
        return False

    d, p = create_is_landmark_task(domain, problem, atom)
    return is_unsolvable(d, p)


def extract_goal(prob):

    a = prob.split("(:goal")[1]
    cp = 1
    for i, c in enumerate(a):
        if c == ")":
            cp -= 1        
        if c == "(":
            cp += 1
        if cp == 0:
            return "(:goal" + a[:i+1]

    assert (False)

def is_unsolvable_new_goal(domain, problem, new_goal):
    goal = extract_goal(problem)
    # print(f'-===============> Extracted goal {goal}')
    new_problem = problem.replace(goal, f"(:goal {new_goal} )")
    # print(f'-===============> New problem {new_problem}')
    return is_unsolvable(domain, new_problem)

def is_unsolvable(domain, problem):
    with tempfile.NamedTemporaryFile() as domain_temp, \
         tempfile.NamedTemporaryFile() as problem_temp:
        with open(str(domain_temp.name), 'w', encoding='utf8') as file:
            file.write(str(domain))
        with open(str(problem_temp.name), 'w', encoding='utf8') as file:
            file.write(str(problem))

        # plans = fi.plan_diverse_agl(domain_file=Path(str(domain_temp.name)), problem_file=Path(str(problem_temp.name)), number_of_plans_bound=1, timeout=3)
        plans = kp.plan_unordered_topq(domain_file=Path(str(domain_temp.name)), problem_file=Path(str(problem_temp.name)),  quality_bound =1.0, number_of_plans_bound=1, timeout=3)

        if len(plans["planner_error"]) > 0:
            fl = plans["planner_error"].split("\n")[0]
            print(f'Planner error: {fl}')
            # print(plans["planner_error"])
            return False
        if plans is None or len(plans['plans']) == 0:
            # print(plans)
            return plans["unsolvable"]
        return False
