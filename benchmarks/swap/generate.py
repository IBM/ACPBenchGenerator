#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path
import generator.generator as sg

def is_goal_empty(domain_file : Path, problem_file : Path):
    command = ["validate", str(domain_file.absolute()), str(problem_file.absolute()), "empty_plan"]
    run = subprocess.run(" ".join(command),shell=True, stdout=subprocess.DEVNULL)
    return run.returncode == 0

def generate(name,  num_agents, k):
    instance_name = f'swap-{num_agents}-{k}'
    print(instance_name)
    while True:
        with open(name, "w") as f:
            ret = sg.main(instance_name, num_agents, 2020 + k)
            f.writelines(ret)
        if not is_goal_empty(Path("domain.pddl"), Path(name)):
            break



if __name__ == "__main__":
    # A single axis of generalization: keep the number of roles and the number of agents the same. 
    count = 1
    for a in [3, 4, 5, 6, 7, 8, 9, 11, 13, 15]:
        for k in range(3):
            nm = f'p{count:02}.pddl'                                
            generate(nm, a, count*2)            
            count+=1
