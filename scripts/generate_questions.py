import gzip
import json
import glob 
import os
import random 
import argparse
import time

from PDDL2NL import utils as ut
from PDDL2NL.tasks.action_applicability_task import generate_applicable_actions_for_problem_state_bool, generate_applicable_actions_for_problem_state_gen, generate_applicable_actions_for_problem_state_mcq 
from PDDL2NL.tasks.atom_reachability_task import generate_reachability_for_problem_state_bool, generate_reachability_for_problem_state_gen, generate_reachability_for_problem_state_mcq
from PDDL2NL.tasks.description_task import generate_problem_description
from PDDL2NL.tasks.distances_task import generate_problem_distances
from PDDL2NL.tasks.goal_closer_task import generate_goal_closer_bool, generate_goal_closer_gen, generate_goal_closer_mcq
from PDDL2NL.tasks.landmarks_task import generate_landmarks_for_problem_state_bool, generate_landmarks_for_problem_state_gen, generate_landmarks_for_problem_state_mcq
from PDDL2NL.tasks.multistep_progression_task import generate_multistep_progression_for_problem_state_bool, generate_multistep_progression_for_problem_state_mcq
from PDDL2NL.tasks.progression_task import generate_progression_for_problem_state_bool, generate_progression_for_problem_state_gen, generate_progression_for_problem_state_mcq
from PDDL2NL.tasks.transitions_generation_task import generate_transitions_for_problem_state
from PDDL2NL.tasks.validation_task import generate_validation_for_problem_state_bool, generate_validation_for_problem_state_gen, generate_validation_for_problem_state_mcq
from PDDL2NL.tasks.action_reachability_task import generate_action_reachability_for_problem_state_gen, generate_action_reachability_for_problem_state_mcq, generate_action_reachability_for_problem_state_bool
from PDDL2NL.tasks.action_justification_task import generate_examples_action_justification_for_problem_state_gen, generate_examples_action_justification_for_problem_state_mcq, generate_examples_action_justification_for_problem_state_bool
from PDDL2NL.tasks.plan_generation_task import generate_plan_for_problem_state

from PDDL2NL.utils.tarski_utils import state_as_sorted_tuple
from PDDL2NL.utils.tarskilite import STRIPS
from merge import merge

train_domains = ['ferry', 'logistics', 'blocksworld', 'grid', 'floortile', 'grippers', 'rovers', 'visitall']
test_domains = ['depot', 'goldminer', 'satellite', 'swap', 'alfworld']

dirname = os.path.dirname(__file__)


def get_problem_files(args, domain, instance_choice):
    sample_indices = [2,4,6]
    test_indices = set([1, 5, 9, 13, 17, 25, 26, 27, 28, 29])
    neurips_indices = set([1, 5, 9, 13, 17])
    training_indices = set(range(30)) - test_indices
    problems = sorted(glob.glob(f"{dirname}/../benchmarks/{domain}/generated_instances/*"))
    test_problems = [problems[i] for i in test_indices]
    training_problems = [problems[i] for i in training_indices]

    if args.instance_name and len(args.instance_name) > 0:
        return sorted(glob.glob(f"{dirname}/../benchmarks/{domain}/generated_instances/{args.instance_name}"))        

    if instance_choice == "random":
        return [ random.choice(problems) ]
    elif instance_choice == "first":
        # Lexicographically first instance
        return problems[:1]
    elif instance_choice == "training":
        return training_problems
    elif instance_choice == "test":
        return test_problems
    elif instance_choice == "all":
        return problems
    elif instance_choice == "sample":
        return [problems[i] for i in sample_indices]
    elif instance_choice == "neurips":
        return [problems[i] for i in neurips_indices]
    else:
        print("Undefined option, should not happen")


def get_json_filename(args, domain, test_set_only):
    pref_suff = "test" if test_set_only else "training"
    if args.json_name:
        return f'{args.jsons_folder}/{domain}-{pref_suff}-{args.json_name}'
    else:
        return f"{args.jsons_folder}/{domain}-{pref_suff}.json"

    # if args.domain == "test":
    #     return f"{domain}-test.json"
    # elif args.domain == "train" or args.domain == "all":
    #     return f"{domain}-{pref_suff}.json"
    # else:
    #     print("If --domain is neither train nor test, you must specify --json-name")
    #     exit(1)
    # return None

def generate_questions(args, domain):
    if args.task in ["applicability", "progression", "reachability", "action_reachability", "landmarks", "plan_generation", "next_action", "transitions", "multistep_progression", "description", "distance"]:
        # Test 
        sample = generate_sample(args, domain, test_sample=None)
        if args.domain == "test" or args.domain in test_domains or args.instance_name:
            return
        # Train
        generate_sample(args, domain, test_sample=sample)
    elif args.task in ["validation", "action_justification"]:
        # Test
        sample = generate_init_plans(args, domain, test_sample=None)
        if args.domain == "test" or args.domain in test_domains or args.instance_name:
            return
        # Train
        generate_init_plans(args, domain, test_sample=sample)


def generate_init_plans(args, domain, test_sample):
    # If test_sample is None, we are generating test sample, otherwise, we are generating training sample
    if test_sample is None:
        test_set_only = True
        instance_choice = "test"
    else: 
        test_set_only = False
        instance_choice = "training"

    json_file_name = get_json_filename(args, domain, test_set_only)
    action_templates = json.load(open(f'{dirname}/../benchmarks/action_templates.json','r'))
    examples = []
    problems = get_problem_files(args, domain, instance_choice)
    num_plans = 200 # default value for these tasks
    if args.num_plans:
        num_plans = args.num_plans

    generated_plans = []
    removed_plans = 0
    all_time = time.time()
    sample_time = 0

    for problem in problems:
        domain_file=f"{dirname}/../benchmarks/{domain}/domain.pddl"
        s_time = time.time()
        P, plans = ut.tlu.get_task_plans(domain_file, problem, num_plans)
        sample_time += time.time() - s_time
        print(problem, f'Plans: {len(plans)}.')
        s_time = time.time()

        filename = os.path.splitext(os.path.basename(problem))[0]
        if args.task == "validation":
            for i, plan in enumerate(plans):
                if test_sample is not None and plan in test_sample:
                    removed_plans += 1
                    continue
                generated = generate_examples_validation_for_problem_state(args, P, state=P.init, plan=plan, action_templates=action_templates, domain=domain, example_id=f"{filename}_{i}", random=random)
                if len(generated) > 0:
                    generated_plans.append(plan)
                    examples.extend(generated)        
        elif args.task == "action_justification":
            for i, plan in enumerate(plans):
                if test_sample is not None and plan in test_sample:
                    continue
                generated = generate_examples_action_justification_for_problem_state(args, P, state=P.init, plan=plan, action_templates=action_templates, domain=domain, example_id=f"{filename}_{i}", random=random)
                if len(generated) > 0:
                    generated_plans.append(plan)
                    examples.extend(generated)        
    if args.verbose:
        e_time = time.time()
        print(f"Generated {len(examples)} examples in {e_time - all_time:0.2f} seconds, of which {sample_time:0.2f} seconds for plans sampling.")    
        if test_sample is not None: 
            print(f"Removed {removed_plans} test plans from the training set.")

    print("Writing to ", json_file_name)
    json.dump(examples,open(json_file_name,'w'), indent=2)
    with gzip.open(json_file_name+".gz", "w") as f:
        f.write(json.dumps(examples, indent=2).encode('utf-8'))    
    if args.dump_no_newlines:
        write_no_newlines(examples, json_file_name)    
    return generated_plans

def generate_sample(args, domain, test_sample):
    # If test_sample is None, we are generating test sample, otherwise, we are generating training sample
    if test_sample is None:
        test_set_only = True
        instance_choice = "test"
    else: 
        test_set_only = False
        instance_choice = "training"

    json_file_name = get_json_filename(args, domain, test_set_only)
    action_templates = json.load(open(f'{dirname}/../benchmarks/action_templates.json','r'))
    examples = []
    problems = get_problem_files(args, domain, instance_choice)
    sampled_states = set()
    removed_states = 0
    all_time = time.time()
    sample_time = 0
    lmg_time = 0
    unreachable_time = 0
    for problem in problems:
        s_time = time.time()
        P, states = _generate_random_sample_from_plans(args, domain, problem)
        sample_time += time.time() - s_time
        if test_sample is not None:
            train_states = states - test_sample
            removed_states += len(states) - len(train_states)
            states = train_states

        filename = os.path.splitext(os.path.basename(problem))[0]
        if args.task == "applicability":
            for i, current_state in enumerate(states):
                generated = generate_examples_applicable_actions_for_problem_state(args, P, state=set(current_state), action_templates=action_templates, domain=domain,example_id=f"{filename}_{i}", random=random)
                if len(generated)>0:
                    sampled_states.add(current_state)
                    examples.extend(generated)        
        if args.task == "progression":
            for i, current_state in enumerate(states):
                generated = generate_examples_progression_for_problem_state(args, P, state=set(current_state), action_templates=action_templates, domain=domain,example_id=f"{filename}_{i}", random=random)
                if len(generated)>0:
                    sampled_states.add(current_state)
                    examples.extend(generated)                
        if args.task == "multistep_progression":
            for i, current_state in enumerate(states):
                generated = generate_examples_multistep_progression_for_problem_state(args, P, state=set(current_state), action_templates=action_templates, domain=domain,example_id=f"{filename}_{i}", random=random)
                if len(generated)>0:
                    sampled_states.add(current_state)
                    examples.extend(generated)
        if args.task == "reachability":
            if args.question_type != "gen" or True:
                s_time = time.time()
                P.compute_LMG()
                lmg_time += time.time() - s_time
            for i, current_state in enumerate(states):
                generated = generate_examples_reachability_for_problem_state(args, P, state=set(current_state), action_templates=action_templates, domain=domain,example_id=f"{filename}_{i}", random=random)
                if len(generated)>0:
                    sampled_states.add(current_state)
                    examples.extend(generated)                
        if args.task == "action_reachability":
            if args.question_type != "gen" or True:
                s_time = time.time()
                domain_file=f"{dirname}/../benchmarks/{domain}/domain.pddl"
                P = STRIPS(domain_file, problem, compute_unreachable_actions=True)
                P.compute_unreachable_actions()
                unreachable_time += time.time() - s_time
            # if unreachable_time > 0:
            #     print(f"Unreachable actions computation took {unreachable_time:0.2f} seconds.")
            for i, current_state in enumerate(states):
                generated = generate_examples_action_reachability_for_problem_state(args, P, state=set(current_state), action_templates=action_templates, domain=domain,example_id=f"{filename}_{i}", random=random)
                if len(generated)>0:
                    sampled_states.add(current_state)
                    examples.extend(generated)
        if args.task == "landmarks":
            # Timeout for the planner
            timeout = args.planner_timeout if args.planner_timeout is not None else 30
            for i, current_state in enumerate(states):
                generated = generate_examples_landmarks_for_problem_state(args, P, state=set(current_state), action_templates=action_templates, domain=domain,example_id=f"{filename}_{i}", random=random, timeout = timeout)
                if len(generated)>0:
                    sampled_states.add(current_state)
                    examples.extend(generated)                
        if args.task == "plan_generation":
            # Timeout for the planner
            timeout = args.planner_timeout if args.planner_timeout is not None else 30
            for i, current_state in enumerate(states):
                generated = generate_plan_for_problem_state(P, state=set(current_state), action_templates=action_templates, domain=domain,example_id=f"{filename}_{i}", random=random, timeout = timeout)
                if len(generated)>0:
                    sampled_states.add(current_state)
                    examples.extend(generated)
        if args.task == "next_action":
            # Timeout for the planner
            timeout = args.planner_timeout if args.planner_timeout is not None else 5
            for i, current_state in enumerate(states):
                generated = generate_examples_goal_closer_for_problem_state(args, P, state=set(current_state), action_templates=action_templates, domain=domain,example_id=f"{filename}_{i}", random=random, timeout = timeout)
                if len(generated)>0:
                    sampled_states.add(current_state)
                    examples.extend(generated)       
        if args.task == "transitions":
            num_transitions = args.num_transitions
            for i, current_state in enumerate(states):
                generated = generate_transitions_for_problem_state(P, state=set(current_state), action_templates=action_templates, domain=domain, num_transitions=num_transitions, example_id=f"{filename}_{i}", random=random)
                if len(generated)>0:
                    sampled_states.add(current_state)
                    examples.extend(generated)       
        if args.task == 'description':
            for i, current_state in enumerate(states):
                generated = generate_problem_description(P, action_templates=action_templates, domain=domain, example_id=f"{filename}_{i}", random=random)
                if len(generated)>0:
                    sampled_states.add(current_state)
                    examples.extend(generated)
        if args.task == 'distance':
            for i, current_state in enumerate(states):
                generated = generate_problem_distances(P, state=set(current_state), action_templates=action_templates, domain=domain, example_id=f"{filename}_{i}", random=random)
                if len(generated)>0:
                    sampled_states.add(current_state)
                    examples.extend(generated)
                    


    if args.verbose:
        e_time = time.time()
        print(f"Generated {len(examples)} examples in {e_time - all_time:0.2f} seconds, of which {sample_time:0.2f} seconds for states sampling.")    
        if lmg_time > 0:
            print(f"LMG computation took {lmg_time:0.2f} seconds.")
        if unreachable_time > 0:
            print(f"Unreachable actions computation took {unreachable_time:0.2f} seconds.")
        if test_sample is not None: 
            print(f"Removed {removed_states} test states from the training set.")

    print("Writing to ", json_file_name)
    json.dump(examples,open(json_file_name,'w'), indent=2)
    with gzip.open(json_file_name+".gz", "w") as f:
        f.write(json.dumps(examples, indent=2).encode('utf-8'))
    if args.dump_no_newlines:
        write_no_newlines(examples, json_file_name)
    
    return sampled_states    

def generate_examples_progression_for_problem_state(args, P, state, action_templates, domain, example_id, random):
    if args.question_type == "mcq":
        return generate_progression_for_problem_state_mcq(P, state, action_templates, domain, example_id, random)
    if args.question_type == "bool":
        return generate_progression_for_problem_state_bool(P, state, action_templates, domain, example_id, random)
    if args.question_type == "gen":
        return generate_progression_for_problem_state_gen(P, state, action_templates, domain, example_id, random)
    

def generate_examples_multistep_progression_for_problem_state(args, P, state, action_templates, domain, example_id, random):

    if args.depth:
        depth = args.depth
    else:
        depth = random.randint(args.min_depth,args.max_depth)

    if args.question_type == "mcq":
        return generate_multistep_progression_for_problem_state_mcq(P, state, depth, action_templates, domain, example_id, random)
    if args.question_type == "bool":
        return generate_multistep_progression_for_problem_state_bool(P, state, depth, action_templates, domain, example_id, random)


def generate_examples_reachability_for_problem_state(args, P, state, action_templates, domain, example_id, random):
    
    if args.depth:
        plan_depth = args.depth
    else:
        plan_depth = random.randint(args.min_depth,args.max_depth)
    
    if args.question_type == "mcq":
        return generate_reachability_for_problem_state_mcq(P, state, action_templates, domain, example_id, random, plan_depth=plan_depth)
    if args.question_type == "bool":
        return generate_reachability_for_problem_state_bool(P, state, action_templates, domain, example_id, random, plan_depth=plan_depth)
    if args.question_type == "gen":
        return generate_reachability_for_problem_state_gen(P, state, action_templates, domain, example_id, random, plan_depth=plan_depth)

def generate_examples_action_reachability_for_problem_state(args, P, state, action_templates, domain, example_id, random):
    if args.question_type == "mcq":
        return generate_action_reachability_for_problem_state_mcq(P, state, action_templates, domain, example_id, random)
    if args.question_type == "bool":
        return generate_action_reachability_for_problem_state_bool(P, state, action_templates, domain, example_id, random)    
    if args.question_type == "gen":
        return generate_action_reachability_for_problem_state_gen(P, state, action_templates, domain, example_id, random)

def generate_examples_applicable_actions_for_problem_state(args, P, state, action_templates, domain, example_id, random):
    if args.question_type == "mcq":
        return generate_applicable_actions_for_problem_state_mcq(P, state, action_templates, domain, example_id, random)
    if args.question_type == "bool":
        return generate_applicable_actions_for_problem_state_bool(P, state, action_templates, domain, example_id, random)
    if args.question_type == "gen":
        num_actions_bound = args.num_actions_bound
        return generate_applicable_actions_for_problem_state_gen(P, state, num_actions_bound, action_templates, domain, example_id, random)

def generate_examples_action_justification_for_problem_state(args, P, state, plan, action_templates, domain, example_id, random):
    if args.question_type == "mcq":
        return generate_examples_action_justification_for_problem_state_mcq(P, state, plan, action_templates, domain, example_id, random)
    if args.question_type == "bool":
        return generate_examples_action_justification_for_problem_state_bool(P, state, plan, action_templates, domain, example_id, random)
    if args.question_type == "gen":
        return generate_examples_action_justification_for_problem_state_gen(P, state, plan, action_templates, domain, example_id, random)

def generate_examples_validation_for_problem_state(args, P, state, plan, action_templates, domain, example_id, random):
    if args.question_type == "mcq":
        return generate_validation_for_problem_state_mcq(P, state, plan, action_templates, domain, example_id, random)
    if args.question_type == "bool":
        return generate_validation_for_problem_state_bool(P, state, plan, action_templates, domain, example_id, random)
    if args.question_type == "gen":
        return generate_validation_for_problem_state_gen(P, state, plan, action_templates, domain, example_id, random)


def generate_examples_landmarks_for_problem_state(args, P, state, action_templates, domain, example_id, random, timeout):
    if args.question_type == "mcq":
        return generate_landmarks_for_problem_state_mcq(P, state, action_templates, domain, example_id, random, timeout)
    if args.question_type == "bool":
        return generate_landmarks_for_problem_state_bool(P, state, action_templates, domain, example_id, random, timeout)
    if args.question_type == "gen":
        return generate_landmarks_for_problem_state_gen(P, state, action_templates, domain, example_id, random, timeout)


def generate_examples_goal_closer_for_problem_state(args, P, state, action_templates, domain, example_id, random, timeout):
    if args.question_type == "mcq":
        return generate_goal_closer_mcq(P, state, action_templates, domain, example_id, random, timeout)
    if args.question_type == "bool":
        return generate_goal_closer_bool(P, state, action_templates, domain, example_id, random, timeout)
    if args.question_type == "gen":
        return generate_goal_closer_gen(P, state, action_templates, domain, example_id, random, timeout)


def _generate_random_sample_from_plans(args, domain, problem_file):
    domain_file=f"{dirname}/../benchmarks/{domain}/domain.pddl"
    if args.task in ['description'
                    #  , 'distance'
                     ]:
        P = STRIPS(domain_file, problem_file)
        states = set()
        states.add(state_as_sorted_tuple(P.init))
        return P, states
    num_plans = 20 # default value for these tasks
    if args.num_plans:
        num_plans = args.num_plans

    num_samples = 200 # default value for these tasks
    if args.sample_size:
        num_samples=args.sample_size    
    P, plan_states, other_states = ut.tlu.get_states_sample_along_plans(domain_file, problem_file, num_plans, num_samples, random=random)
    # print(problem_file, f'States on plans: {len(plan_states)}, other states: {len(other_states)}, check other states {len(other_states - plan_states)}.')
    sample_states = set()
    if len(plan_states) == num_samples:
        sample_states = plan_states
    elif len(plan_states) > num_samples:
        sample_states = set(random.sample(list(plan_states), k=num_samples))         
    elif len(plan_states) + len(other_states) >= num_samples:
        remaining_sample_size = num_samples - len(plan_states)
        sample_states = plan_states | set(random.sample(list(other_states), k=remaining_sample_size))
    else:
        # Use what we have
        sample_states = plan_states | other_states
    print(problem_file, f'States on plans: {len(plan_states)}, other states: {len(other_states)}, selected {len(sample_states)} states.')
    return P, sample_states

def get_generated_folder_name(args, source_name):
    return f"{source_name}" if args.task in ["plan_generation", "transitions", 'description', 'distance'] else f"{source_name}-{args.question_type}"

def merge_train_domains(args, domains, test_set_only):
    source_name = "test" if test_set_only else "training"
    source_folder = "."
    if args.jsons_folder:
        source_folder = f"{args.jsons_folder}/{get_generated_folder_name(args, source_name)}"

    dest = f"{get_generated_folder_name(args, source_name)}.json"
    res = merge(domains, source_name, source_folder, dest)
    if args.dump_no_newlines:
        write_no_newlines(res, dest)

def merge_test_domains(args, domains):
    source_name = "test"
    source_folder = "."
    if args.jsons_folder:
        source_folder = f"{args.jsons_folder}/{get_generated_folder_name(args, source_name)}"

    dest = f"{get_generated_folder_name(args, f'{source_name}-gen')}.json"

    res = merge(domains, source_name, source_folder, dest)
    if args.dump_no_newlines:
        write_no_newlines(res, dest)

def fix_data(data):
    fields = ["context", "inputs", "targets", "question", "query"]
    for e in data:
        for f in fields:
            if f in e:
                if 'sequence of actions \"' in e[f]:
                    # Replacing \n in the sequence of actions first.
                    if "and the current state?" in e[f]:
                        a = e[f].split("and the current state?")
                        a[0] = a[0].replace("\n", ", ")
                        a[1] = a[1].replace("\n", " ").replace("  ", " ")
                        e[f] = "".join(a)
                    else:
                        e[f] = e[f].replace("\n", ", ")
                else:
                    e[f] = e[f].replace("\n", " ").replace("  ", " ")
    return data

def write_no_newlines(res, dest):
    dest_fixed = dest.replace(".json", "-nnl.json")
    res = fix_data(res)
    with open(dest_fixed, "w") as f:
        json.dump(res, f, indent=2)
    with gzip.open(dest_fixed+".gz", "w") as f:
        f.write(json.dumps(res).encode('utf-8'))

def select_smallest(data):
    def matches_smallest(id):
        # Choosing from the following out of the test instances: ["_p02_", "_p06_", "_p10_", "_p14_", "_p18_"]

        import re
        regexp = re.compile(r'_p(0[26]|1[048])_')
        return regexp.search(id)
    return [e for e in data if matches_smallest(e["id"])]


def select_smallest_dev(data):
    def matches_smallest(id):
        # Choosing from the following out of the test instances: ["_p01_", "_p03_", "_p04_", "_p05_", "_p07_"]

        import re
        regexp = re.compile(r'_p(0[13457])_')
        return regexp.search(id)
    return [e for e in data if matches_smallest(e["id"])]

def sample(args, domains, dest, sample_size):
    small = []
    for d in domains:
        if args.task in ["plan_generation", "transitions", "description", "distance"]:
            data = json.load(gzip.open(f'{args.jsons_folder}/test/{d}-test.json.gz'))    
        else:
            data = json.load(gzip.open(f'{args.jsons_folder}/test-{args.question_type}/{d}-test.json.gz'))    
        smallest = select_smallest(data)
        if len(smallest) < sample_size:
            print(f"Not enough samples for domain {d}, taking all {len(smallest)} samples")
            small.extend(smallest)
        else:
            small.extend(random.sample(smallest, k=sample_size))
    with open(dest, "w") as f:
        json.dump(small, f, indent=2)
    with gzip.open(dest+".gz", "w") as f:
        f.write(json.dumps(small, indent=2).encode('utf-8'))      

    if args.dump_no_newlines:
        write_no_newlines(small, dest)
        

def dev_sample(args, domains, dest, sample_size):
    small = []
    for d in domains:
        if args.task in ["plan_generation", "transitions", "description", "distance"]:
            data = json.load(gzip.open(f'{args.jsons_folder}/training/{d}-test.json.gz'))    
        else:
            data = json.load(gzip.open(f'{args.jsons_folder}/training-{args.question_type}/{d}-training.json.gz'))    
        smallest = select_smallest_dev(data)
        if len(smallest) < sample_size:
            print(f"Not enough samples for domain {d}, taking all {len(smallest)} samples")
            small.extend(smallest)
        else:
            small.extend(random.sample(smallest, k=sample_size))
    # Removing fields
    for e in small:
        if "targets" in e:
            del e["targets"]
        if "question" in e:
            e["query"] = e.pop("question")
        e["question"] = e.pop("inputs")

    with open(dest, "w") as f:
        json.dump(small, f, indent=2)
    with gzip.open(dest+".gz", "w") as f:
        f.write(json.dumps(small, indent=2).encode('utf-8'))      

    if args.dump_no_newlines:
        write_no_newlines(small, dest)
        


def validate_input(args):
    if args.task not in ["plan_generation", "transitions", "description", "distance"]:
        assert args.question_type is not None, "You must provide --question-type for every task except for plan_generation and transitions."

    if args.task in ["transitions"]:
        assert args.num_transitions is not None, "You must provide --num-transitions for transitions task."

    if args.merge:
        assert(args.domain in ["test", "train", "all"])
    if args.test_sample_size:
        assert(args.domain == "all")
        assert(args.merge or args.merge_only)    

    if args.depth:
        assert (not args.min_depth and not args.max_depth), "Either --depth or --min-depth and --max-depth should be specified, not both"
    elif args.task == "multistep_progression":
        assert (args.min_depth and args.max_depth) , "If --depth is not specified, both --min-depth and --max-depth should be specified"
        


if __name__ == "__main__":
    all_domains = train_domains + test_domains + ['hanoi', 'random_hanoi', 'frogs_jumping']
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain', type=str, choices=['all', "test", "train"] + all_domains, required=True)
    parser.add_argument('--task', type=str, choices=['applicability', 'progression', 'reachability', 'validation', 'action_reachability', 'landmarks', 'action_justification', 'plan_generation', "next_action", 'transitions', 'multistep_progression', 'description', 'distance'], required=True)
    parser.add_argument('--question-type', type=str, choices=['mcq', 'bool', "gen"])
    parser.add_argument('--seed', type=int)

    parser.add_argument('--sample-size', type=int)
    parser.add_argument('--num-plans', type=int)

    parser.add_argument('--json-name', type=str)
    parser.add_argument('--instance-name', type=str)
    parser.add_argument('--instance-choice', type=str, choices=['first', 'random', 'all', 'training', 'test', 'sample', 'neurips'])
    parser.add_argument('--merge', action='store_true')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--merge-only', action='store_true')
    parser.add_argument('--dev-only', action='store_true')
    parser.add_argument('--jsons-folder', type=str, default="./")
    parser.add_argument('--test-sample-size', type=int)
    parser.add_argument('--dev-sample-size', type=int, default=5)
    parser.add_argument('--planner-timeout', type=int)
    parser.add_argument('--dump-no-newlines', action='store_true')
    parser.add_argument('--num-transitions', type=int)
    parser.add_argument('--num-actions-bound', type=int, default=50)
    parser.add_argument('--depth', type=int)
    parser.add_argument('--min-depth', type=int)
    parser.add_argument('--max-depth', type=int)
    

    args = parser.parse_args()
    if args.seed:
        random.seed(args.seed)

    validate_input(args)

    domains = []
    if args.domain == "all":
        domains = all_domains
    elif args.domain == "test":
        domains = test_domains
    elif args.domain == "train":
        domains = train_domains
    else:
        domains.append(args.domain)

    if not args.merge_only and not args.dev_only:
        for domain in domains:
            generate_questions(args, domain)

    if args.merge or args.merge_only:
        # For test domains, we only generate the test-gen files
        # For train domains, we generate test and training files
        if args.domain == "test":
            merge_test_domains(args, domains)
        elif args.domain == "train":
            merge_train_domains(args, domains, test_set_only=True)
            merge_train_domains(args, domains, test_set_only=False)
        else:
            merge_test_domains(args, test_domains)
            merge_train_domains(args, train_domains, test_set_only=True)
            merge_train_domains(args, train_domains, test_set_only=False)
            if args.test_sample_size:
                full_sample_size = len(domains) * args.test_sample_size
                sample_dest = f"{get_generated_folder_name(args, f'test-sample-{full_sample_size}')}.json"

                sample(args, domains, sample_dest, args.test_sample_size)

    if args.dev_only:
        assert args.dev_sample_size
        assert args.domain == "train"

        full_sample_size = len(domains) * args.dev_sample_size
        sample_dest = f"{get_generated_folder_name(args, f'dev-sample-{full_sample_size}')}.json"
        print(f"Writing to {sample_dest}")
        dev_sample(args, domains, sample_dest, args.dev_sample_size)
