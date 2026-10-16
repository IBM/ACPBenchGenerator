import gzip
import json
import glob 
import os
import random 
import argparse
import time

from generate_questions import train_domains, test_domains, get_problem_files
from PDDL2NL import utils as ut

from PDDL2NL.utils.tarski_utils import state_as_sorted_tuple
from PDDL2NL.utils.tarskilite import STRIPS
from PDDL2NL.tasks.atom_reachability_task import generate_reachability_for_problem_state_bool, generate_reachability_for_problem_state_gen, generate_reachability_for_problem_state_mcq, generate_reachability_for_problem_state_reachable, generate_reachable_atom_task

dirname = os.path.dirname(__file__)

def generate_examples_reachability_for_original_problem(args, P, state, action_templates, domain, example_id, random, timeout=30):
    partial_state, is_reachable, actions, reason_code_and_atom  =  generate_reachability_for_problem_state_reachable(P, state, action_templates, domain, example_id, random, plan_depth=0, timeout=timeout)
    return generate_reachable_atom_task(P, state, action_templates, domain, example_id+"_p", partial_state, is_reachable, actions, random, reason_code_and_atom)


def generate_reachability_questions(args, domain):
    action_templates = json.load(open(f'{dirname}/../benchmarks/action_templates.json','r'))
    domain_file=f"{dirname}/../benchmarks/{domain}/domain.pddl"
    examples = []
    problems = get_problem_files(args, domain, instance_choice="all") 
    if args.json_name is not None:
        json_file_name = f"{args.jsons_folder}/{domain}-original-{args.json_name}"
    else:
        json_file_name = f"{args.jsons_folder}/{domain}-original.json"
    all_time = time.time()
    examples = []
    for problem_file in problems:
        
        s_time = time.time()
        P = STRIPS(domain_file, problem_file)
        
        initial_state = state_as_sorted_tuple(P.init)
        filename = os.path.splitext(os.path.basename(problem_file))[0]
        generated = generate_examples_reachability_for_original_problem(args, P, state=set(initial_state), action_templates=action_templates, domain=domain, example_id=f"{filename}", random=random, timeout=args.timeout)
        if len(generated)>0:
            examples.append(generated)
        if args.verbose:
            e_time = time.time()
            print(f"Generated {len(examples)} examples in {e_time - all_time:0.2f} seconds") 
        # Moving it inward.
        print("Writing to ", json_file_name)
        json.dump(examples,open(json_file_name,'w'), indent=2)
    
if __name__ == "__main__":
    all_domains = train_domains + test_domains + ['hanoi', 'random_hanoi', 'frogs_jumping']
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain', type=str, choices=['all', "test", "train"] + all_domains, required=True)
    parser.add_argument('--question-type', type=str, default='bool', choices=['bool'])
    parser.add_argument('--seed', type=int)
    parser.add_argument('--timeout', type=int, default=30)
    parser.add_argument('--json-name', type=str)
    parser.add_argument('--instance-name', type=str)
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--jsons-folder', type=str, default="./")
    
    args = parser.parse_args()
    
    domains = []
    if args.domain == "all":
        domains = all_domains
    elif args.domain == "test":
        domains = test_domains
    elif args.domain == "train":
        domains = train_domains
    else:
        domains.append(args.domain)
    
    for domain in domains:
        print(f"========== Starting {domain} ============")
        generate_reachability_questions(args, domain)