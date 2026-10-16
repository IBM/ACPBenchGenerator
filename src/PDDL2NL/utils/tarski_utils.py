import gzip
import json
import os
import re
import tempfile
import time
from typing import Optional

from PDDL2NL.utils.translation_util import get_action_description, get_pddl_domain, remove_trailing_dot
from . import tarskilite as tl
import math
from tarski.syntax import BuiltinPredicateSymbol

from pathlib import Path 
from kstar_planner import planners as kp
from forbiditerative import planners as fi


def get_tarski_problem(domain, problem):
    with tempfile.NamedTemporaryFile() as domain_temp, \
         tempfile.NamedTemporaryFile() as problem_temp:
        if "logistics" in str(domain):
            domain = get_pddl_domain("logistics")
        if "depot" in str(domain):
            domain = get_pddl_domain("depot")

        with open(str(domain_temp.name), 'w', encoding='utf8') as file:
            file.write(domain.lower())
        with open(str(problem_temp.name), 'w', encoding='utf8') as file:
            file.write(problem.lower())

        try:
            P = tl.STRIPS(str(domain_temp.name), str(problem_temp.name))
            return P
        except Exception as e:
            print(f"||{e}||")
            return None


def goal_met(s, P):
    return tl.entails(s, P.goal)

def get_applicable_actions(P, s):
    return [a for a in P.actions if tl.entails(s, a.pres)]

def get_inapplicable_actions(P, s):
    return [a for a in P.actions if not tl.entails(s, a.pres)]

def get_lifted_actions_desc(P, template):
    lifted_actions = []
    for aname, a in P.problem.actions.items():
        n = aname + " " + " ".join([str(par) for par in a.parameters])
        desc = remove_trailing_dot(get_action_description(n, template, P))

        # lifted_actions.append(f"{n.lower()} ({desc})")
        lifted_actions.append(f"({n.lower()}) - {desc}")
    return lifted_actions

def fix_args(args):
    arr = args.strip().split("?")[1:]
    # print(args, arr)
    fixed_args = ["?"+a.split(" ")[0] for a in arr]
    return " ".join(fixed_args)
    

def get_lifted_predicate(domain_file, name):
    # template = rf'\({name} .*?\)'
    skip_start = True
    with open(domain_file) as f:
        for line in f:
            line = line.strip()
            if skip_start and ":predicates" not in line:
                continue
            skip_start = False
            if f"({name} " in line.lower():
                a = line.lower().split(f"({name} ")[1].split(")")[0]
                a = fix_args(a)
                # print(f"Line: {line}")
                # print(f"Predicate: ({name} {a})")
                return f'{name} {a}'

def get_lifted_atoms_desc(P, translator):
    lifted_atoms = []
    fluent_names = []     
    for symbol in P.fluent_symbols():
        fluent_names.append(symbol.name)
    for symbol in P.problem.language.predicates:
        if str(symbol.name) not in fluent_names:
            continue

        if symbol.arity > 0:
            pred = get_lifted_predicate(P.domain_file, symbol.name)
        else:
            pred = symbol.name
        # print(symbol.name, pred)
        desc = remove_trailing_dot(translator.get_atoms_description(P, pred))
        # print(desc)
        lifted_atoms.append(f"({pred.lower()}) - {desc}")
        # # print(f"|{symbol}|")
        # n = symbol.name + " " + " ".join([a.name for a in symbol.sort])
        # desc = remove_trailing_dot(translator.get_atoms_description(P, n))
        # lifted_atoms.append(f"({n.lower()}) - {desc}")
    return lifted_atoms


def get_random_invalid_action_name(P, random):
    all_action_names = set(['drop', 'right', 'communicate_rock_data', 'calibrate', 'pick', 'change-color', 'drive-truck', 'lift', 'fly-airplane', 'pickup-and-loose', 'unload-airplane', 'move', 'down', 'communicate_soil_data', 'pickup-laser', 'navigate', 'left', 'unstack', 'drive', 'load-airplane', 'pick-gold', 'load', 'paint-down', 'take_image', 'switch_off', 'pickup', 'switch_on', 'stack', 'unload-truck', 'putdown-laser', 'putdown', 'load-truck', 'up', 'debark', 'detonate-bomb', 'unload', 'fire-laser', 'sample_rock', 'sample_soil', 'pickup-bomb', 'turn_to', 'communicate_image_data', 'paint-up', 'unlock', 'board', 'sail', 'pick-up', 'put-down'])
    problem_action_names =  set([a.name for a in P.actions])
    invalid = list(all_action_names - problem_action_names)
    if len(invalid) == 0:
        return None
    return random.choice(invalid)    

def get_random_applicable_action(P, s, random, lifted_random=False):
    applicable = get_applicable_actions(P, s)
    if len(applicable) == 0:
        return None
    if lifted_random:
        problem_action_names = {} 
        for a in applicable:
            lifted_name = a.name.split()[0]
            if lifted_name not in problem_action_names:
                problem_action_names[lifted_name] = []
            problem_action_names[lifted_name].append(a)
        lifted_name = random.choice(list(problem_action_names.keys()))
        return random.choice(problem_action_names[lifted_name])

    return random.choice(applicable)

def create_tmp_dom_prob_replace_init(P, state, result_domain_file, result_problem_file):
    # d, p = P.PDDL_replace_init(state)
    d, p = P.PDDL_replace_init_pddl_parser(state)
    # print(d)
    # print(p)
    with open(str(result_domain_file.name), 'w', encoding='utf8') as file:
        file.write(str(d))
    with open(str(result_problem_file.name), 'w', encoding='utf8') as file:
        file.write(str(p))

    return d, p

def get_json_file_name(domain, problem):
    domain_name = os.path.basename(os.path.dirname(domain))
    problem_name = os.path.basename(problem)
    plans_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "plans"))
    return os.path.join(plans_folder, domain_name, "%s.json.gz" % problem_name)

def write_to_json(domain, problem, plans):
    if len(plans["plans"]) == 0:
        return
    # Keeping files in a separate folder per domain. 
    # JSON per task, file name adds ".json.gz" to the problem file name         
    json_file = get_json_file_name(domain, problem)
    json_path = os.path.dirname(json_file)
    # print("Creating json at path" + json_path)
    os.makedirs(json_path, exist_ok=True)
    # Writing back to json
    with gzip.open(json_file, 'w') as jf:
        jf.write(json.dumps(plans).encode('utf-8'))



def generate_optimal_plans_for_problem_state(P, state, num_plans, timeout):
    import tempfile
    with tempfile.NamedTemporaryFile() as domain_temp, \
         tempfile.NamedTemporaryFile() as problem_temp:
        
        create_tmp_dom_prob_replace_init(P, state, domain_temp, problem_temp)
        plans = generate_top_q_plans(domain=str(domain_temp.name), problem=str(problem_temp.name), num_plans=num_plans, quality_bound=1.0, timeout=timeout)
        # print(plans)
        if plans is None or len(plans['plans']) == 0:
            return None
        return plans['plans']


def generate_a_plan_for_problem_state(P, state, timeout):
    import tempfile
    with tempfile.NamedTemporaryFile() as domain_temp, \
         tempfile.NamedTemporaryFile() as problem_temp:
        
        create_tmp_dom_prob_replace_init(P, state, domain_temp, problem_temp)
        plans = generate_agile_plan(domain=str(domain_temp.name), problem=str(problem_temp.name), timeout=timeout)
        # print(plans)
        if plans is None or len(plans['plans']) == 0:
            return None
        return plans['plans']

def generate_a_plan_for_problem(d, p, timeout):
    import tempfile
    with tempfile.NamedTemporaryFile() as domain_temp, \
         tempfile.NamedTemporaryFile() as problem_temp:
        
        with open(str(domain_temp.name), 'w', encoding='utf8') as file:
            file.write(str(d))
        with open(str(problem_temp.name), 'w', encoding='utf8') as file:
            file.write(str(p))

        plans = generate_agile_plan(domain=str(domain_temp.name), problem=str(problem_temp.name), timeout=timeout)
        # print(plans)
        if plans is None or len(plans['plans']) == 0:
            return None
        return plans['plans']

def generate_an_optimal_plan_for_problem(d, p, timeout):
    import tempfile
    with tempfile.NamedTemporaryFile() as domain_temp, \
         tempfile.NamedTemporaryFile() as problem_temp:

        with open(str(domain_temp.name), 'w', encoding='utf8') as file:
            file.write(str(d))
        with open(str(problem_temp.name), 'w', encoding='utf8') as file:
            file.write(str(p))

        plans = generate_top_q_plans(domain=str(domain_temp.name), problem=str(problem_temp.name), num_plans=1, quality_bound=1.0, timeout=timeout)
        # print(plans)
        if plans is None or len(plans['plans']) == 0:
            return None
        return plans['plans']

def generate_landmarks(domain_file, problem_file):
    # print("Running FI planner")
    return fi.get_landmarks(domain_file=Path(domain_file), problem_file=Path(problem_file))


def generate_agile_plan(domain, problem, timeout=30):
    # print("Running FI planner, diverse agile")
    plans = fi.plan_diverse_agl(domain_file=Path(domain), problem_file=Path(problem), number_of_plans_bound=1, timeout=timeout)
    return plans

def generate_top_q_plans(domain, problem, num_plans=10, quality_bound=1.0, timeout=30):
    # print("Running K* planner")
    plans = kp.plan_unordered_topq(domain_file=Path(domain), problem_file=Path(problem), number_of_plans_bound=num_plans, quality_bound=quality_bound, timeout=timeout)
    return plans

def generate_plans(domain, problem, num_plans=10, timeout=30, single_phase=False):
    # print("Running K* planner")

    plans = kp.plan_topk(domain_file=Path(domain), problem_file=Path(problem), number_of_plans_bound=num_plans, timeout=timeout)
    # plans = { 'plans' : [] }
    # print(f"Got {len(plans['plans'])} plans")
    # print(plans)
    if len(plans['plans']) < num_plans and not single_phase:
        # print("Running FI planner, diverse agile")
        plans = fi.plan_diverse_agl(domain_file=Path(domain), problem_file=Path(problem), number_of_plans_bound=num_plans, timeout=timeout)
        # print(f"Got {len(plans['plans'])} plans")
        # print(plans)
    return plans

def get_plans(domain, problem, num_plans=10, timeout=30):
    # Alfworld action names changed
    # d = {
    #         "gotolocation" :"go_to_location", 
    #         "openobject" :"open_receptacle",
    #         "closeobject" :"close_receptacle",
    #         "pickupobjectnotopenable" :"pickup_object_from_not_openable_receptacle",
    #         "pickupobjectopenable" :"pickup_object_from_openable_receptacle",
    #         "putobjectnotopenable" :"put_object_on_not_openable_receptacle",
    #         "putobjectopenable" :"put_object_in_openable_receptacle",
    #         "cleanobject" :"clean_object",
    #         "heatobject" :"heat_object",
    #         "coolobject" :"cool_object",
    #         "toggleobjectoff" :"toggle_object_off",
    #         "toggleobjecton" :"toggle_object_on",
    #         "sliceobject" :"slice_object",
    #         "validatepickandplace" :"validate_pick_and_place_in_receptacle",
    #         "validateexamineinlight" :"validate_examine_in_light",
    #         "validatecleanandplace" :"validate_clean_and_place_in_receptacle",
    #         "validateheatandplace" :"validate_heat_and_place_in_receptacle",
    #         "validatecoolandplace" :"validate_cool_and_place_in_receptacle", 
    #         "validatepicktwoandplace" :"validate_pick_two_and_place_in_receptacle"
    # }

    # Try to load plans from disk, if not exist, run a planner and store plans
    # First, run a top-q planner, then diverse-agl.
    # print("getting states from plans")
    json_file = get_json_file_name(domain, problem)
    if os.path.exists(json_file):
        # print("json file exists, loading plans")
        with gzip.open(json_file, 'r') as jf:
            data = json.loads(jf.read().decode('utf-8'))
            # print(f'Loaded {len(data["plans"])} plans')
            # print(f"Plans from json {json_file}")
            # changed = False
            # for plan in data["plans"]:
            #     if plan["actions"][0].startswith("("):
            #         changed = True
            #         plan["actions"] = [ a.replace("(", "").replace(")", "") for a in plan["actions"]]
            #     # print(f'cost {plan["cost"]}')
            #     aname = plan["actions"][0].split(" ")[0]
            #     if aname in d:
            #         changed = True
            #         res = []
            #         for a in plan["actions"]:
            #             aname = a.split( )[0]
            #             res.append(a.replace(aname, d[aname]))
            #         plan["actions"] = res

            # if "domain" in data:
            #     # changed = True
            #     del data["domain"]
            #     del data["problem"]
            #     del data["domain_file"]
            #     del data["problem_file"]

            # changing the plans, lgripper1 -> left1, rgripper1 -> right1
            # for plan in data["plans"]:
            #     plan["actions"] = [ a.replace("lgripper1", "left1").replace("rgripper1", "right1") for a in plan["actions"]]

            # data["plans"] = sorted(data["plans"], key=lambda d: d['cost'])
            # if changed:
            #     write_to_json(domain, problem, data)
    else:
        # Running planners
        # print("json file does not exist, generating plans")
        data = generate_plans(domain, problem, num_plans, timeout=timeout)
        write_to_json(domain, problem, data)

    # Taking the first (cheapest) 10 plans
    data["plans"] = sorted(data["plans"], key=lambda d: d['cost'])[:num_plans]
    return data

def get_task_plans(domain, problem, num_plans,timeout=30):
    plans = get_plans(domain, problem, num_plans, timeout=timeout)
    real_plans = []
    P = tl.STRIPS(domain, problem)
    for plan in plans["plans"]:
        action_seq = plan['actions']
        current_state = P.init
        real_plan = []
        for action in action_seq:
            applicable_actions = get_applicable_actions(P, current_state)
            app_actions_list = [a.name.lower() for a in applicable_actions]
            assert action.lower() in app_actions_list, f"{action} is not in {applicable_actions}"
            a = applicable_actions[app_actions_list.index(action.lower())]
            current_state = tl.progress(current_state, a)
            real_plan.append(a)
        real_plans.append(real_plan)
    return P, real_plans


def states_from_plans(domain, problem, num_plans):
    # s_time = time.time()
    plans = get_plans(domain, problem, num_plans)
    # print(f'Got {len(plans["plans"])} plans in {time.time() - s_time:0.2f} seconds.')
    # s_time = time.time()
    P = tl.STRIPS(domain, problem)
    # print(f"Created planning task in {time.time() - s_time:0.2f} seconds.")
    # s_time = time.time()
    states = set()
    states.add(state_as_sorted_tuple(P.init))
    # Getting states from the first 50 plans
    for plan in plans["plans"]:

        action_seq = plan['actions']
        current_state = P.init
        for action in action_seq:
            applicable_actions = get_applicable_actions(P, current_state)
            app_actions_list = [a.name.lower() for a in applicable_actions]
            assert action.lower() in app_actions_list, f"{action} is not in {applicable_actions}"
            current_state = tl.progress(current_state,applicable_actions[app_actions_list.index(action.lower())])
            states.add(state_as_sorted_tuple(current_state))

    # print(f"Got {len(states)} states from plans in {time.time() - s_time:0.2f} seconds.")
    return states, P

def get_states_sample_along_plans(domain : str, problem : str, num_plans : int, num_samples : int, random, depth : Optional[int] = None):
    plan_states, P = states_from_plans(domain, problem, num_plans)
    sample_states = set()
    # print(f'Found {len(plan_states)} states on plans')
    if num_samples == 1:
        return P, plan_states, sample_states
    # P = tl.STRIPS(domain, problem)
    if len(plan_states) < num_samples:
        # Disabling sampling when enough states sampled from plans.
        while True:
            curr_sample_size = len(sample_states)
            num_samples_per_state = max(5, int(num_samples / len(plan_states)))
            # print(f"Number of samples per state is {num_samples_per_state}")
            for s in plan_states:
                sample_states.update(sample_states_from_state(P, init=set(s), num_samples=num_samples_per_state, random=random, depth=depth))
            if len(sample_states) >= num_samples or len(sample_states) == curr_sample_size:
                break

    # print(f"Generated {len(sample_states)} sample states, out of which {len(sample_states - plan_states)} are not on plans.")
    return P, plan_states, (sample_states - plan_states)

def sampe_facts(P : tl.STRIPS, num_samples : int, random, depth : Optional[int] = None):
    # Samples facts in the planning problem P 
    states = sample_states(P, num_samples, random, depth)
    reachable = set()
    for s in states:
        reachable |= set(s)
    return reachable

def state_as_sorted_tuple(s):
    return tuple(sorted(list(s)))

def sample_states(P : tl.STRIPS, num_samples : int, random, depth : Optional[int] = None):
    return sample_states_from_state(P, P.init, num_samples, random, depth)
    # return set([set(s) for s in reachable])

def sample_states_from_state(P : tl.STRIPS, init: set,  num_samples : int, random, depth : Optional[int] = None):
    assert (num_samples >= 1)
    if depth is None:
        depth = math.ceil(math.sqrt(num_samples) * 2)

    reachable = set()
    reachable.add(state_as_sorted_tuple(init))    
    num_walks = 10
    while len(reachable) < num_samples:
        curr_reachable = len(reachable)
        s = init
        for j in range(depth):
            a = get_random_applicable_action(P, s, random)
            if a is None:
                break
            s = tl.progress(s,a)
            reachable.add(state_as_sorted_tuple(s))
            if len(reachable) == num_samples:
                break
        if len(reachable) == curr_reachable:
            if num_walks == 0:
                break
            num_walks -= 1
        else:
            num_walks = 10
    return reachable

def random_path(P : tl.STRIPS, init: set, random, depth : int = 2):
    s = init
    seq = []
    for j in range(depth):
        a = get_random_applicable_action(P, s, random)
        if a is None:
            break
        s = tl.progress(s,a)
        seq.append(a)
    return seq, s

def random_path_no_loops(P : tl.STRIPS, init: set, random, depth : int = 2):
    s = init
    seq = []
    Closed = set()
    c = " ".join(sorted(list(s)))
    Closed.add(c)
    for j in range(depth):
        x = 0
        while x < 10:
            a = get_random_applicable_action(P, s, random)
            if a is None:
                break
            t = tl.progress(s,a)
            c = " ".join(sorted(list(t)))
            if c not in Closed:
                s = t
                Closed.add(c)
                break
            x += 1
        if x == 10 or a is None:
            break
        seq.append(a)
    return seq, s

def random_trace_no_loops(P : tl.STRIPS, init: set, random, depth : int = 2):
    s = init
    seq = [s]
    Closed = set()
    c = " ".join(sorted(list(s)))
    Closed.add(c)
    for j in range(depth):
        x = 0
        while x < 10:
            a = get_random_applicable_action(P, s, random)
            if a is None:
                break
            t = tl.progress(s,a)
            c = " ".join(sorted(list(t)))
            if c not in Closed:
                s = t
                Closed.add(c)
                break
            x += 1
        if x == 10:
            break
        seq.append(s)
    return seq

def bfs(P : tl.STRIPS, timeout = None, actions=False):
    def _is_done(P, reachable, actions):
        if actions and len(P.actions) == len(reachable):
            return True
        if not actions and len(reachable) == len(P.fluents):
            return True
        return False
    
    s = P.init
    Q = [s]
    Closed = set()
    reachable = set()
    start = time.time()
    while len(Q) > 0:
        if time.time() - start > timeout:
            break
        # Get the top from the queue
        s = Q[0]
        del Q[0]
        c = " ".join(sorted(list(s)))
        if c in Closed:
            continue
        Closed.add(c)
        if not actions:
            reachable |= s
        if _is_done(P, reachable, actions):
            return reachable
        # else:
            # print(f'{len(reachable)} out of {num_fluents} reached')
        for a in P.actions:
            if tl.entails(s, a.pres):
                if actions:
                    reachable.add(a)
                Q.append(tl.progress(s,a))

    return reachable


def iddfs(P: tl.STRIPS):
    # TODO: For some reason, the number of found fluents can decrease with increased depth. 
    #       It is counter-intuitive and requires rethinking the stopping criteria. 
    i = 5
    curr_res = 0
    num_fluents = len(P.fluents)
    while True:
        print(f"Running IDDFS iteration with depth {i}")
        res = iddfs_iteration(P, i)
        if len(res) == num_fluents:
            print(f"Got all {num_fluents} fluents, finished")
            return res

        if len(res) == curr_res:
            print(f"Got {curr_res} fluents, no change from the previous layer")
            return res
        
        print(f"Got {len(res)} fluents out of possible {num_fluents}, going to the next iteration")
        curr_res = len(res)
        i += 2

def iddfs_iteration(P : tl.STRIPS, depth):
    s = P.init
    Q = [ tuple((s,0)) ]
    Closed = set()
    num_fluents = len(P.fluents)
    reachable = set()

    while len(Q) > 0:
        # Get the top from the queue
        (s, d) = Q[-1]
        del Q[-1]
        # print(d)
        c = " ".join(sorted(list(s)))
        if c in Closed:
            # print("in closed")
            continue
        Closed.add(c)
        rs = len(reachable)
        reachable |= s
        # print(f"reachable {rs} -> {len(reachable)}")
        if len(reachable) == num_fluents:
            return reachable
        # else:
        #     print(f'{len(reachable)} out of {num_fluents} reached')
        if d >= depth:
            # print("depth reached, skipping expansion")
            continue
        for a in P.actions:
            if tl.entails(s, a.pres):
                t = tl.progress(s,a)
                Q.append(tuple((t, d+1)))

    return reachable

def reachable_facts(P: tl.STRIPS, random):
    print(P.problem.language.predicates)
    print("lifted predicates", len(P.problem.language.predicates))
    print("fuents", len(P.fluents))
    print("actions", len(P.actions))

    # reachable = bfs(P)
    # reachable = iddfs_iteration(P, 10)
    # reachable = iddfs(P)
    reachable = sampe_facts(P, 100, random, 100)
    
    for f in reachable:
        print(f, "Y")

    print("----------------------")    
    naive_all = P.naive_grounding_variables()
    naive_all = set([tl.fix_name(str(o.to_atom())) for idx, o in naive_all.enumerate()])
    ungrounded = naive_all - P.fluents
    for f in ungrounded:
        print(f, "N")

    print("----------------------")    
    unreachable = P.fluents - reachable
    for f in unreachable:
        print(f, "M")

