#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path
import generator.generator as ftg

def is_goal_empty(domain_file : Path, problem_file : Path):
    command = ["validate", str(domain_file.absolute()), str(problem_file.absolute()), "empty_plan"]
    run = subprocess.run(" ".join(command),shell=True, stdout=subprocess.DEVNULL)
    return run.returncode == 0

def generate(name,  num_rows, num_columns, num_robots, k):
    instance_name = f'floortile-{num_rows}-{num_columns}-{num_robots}'
    print(instance_name)
    while True:
        with open(name, "w") as f:
            ret = ftg.main(instance_name, num_rows, num_columns, num_robots, 2020 + k)
            f.writelines(ret)
        if not is_goal_empty(Path("domain.pddl"), Path(name)):
            break



if __name__ == "__main__":
    # Two axes of generalization: rows/columns & robots
    # Num robots should be smaller than the number of columns
    # The actual number of rows created is one more than the input number
    count = 1
    for r, c in [(2,3), (3,3), (3,4), (3,5), (3,6)]:
        rob = 2
        for k in range(3):
            nm = f'p{count:02}.pddl'                                
            generate(nm, r, c, rob, k)            
            count+=1

    for rob in [3, 4, 5]:
        r, c = 3, 5
        for k in [0, 3, 4, 5, 9]:
            nm = f'p{count:02}.pddl'                                
            generate(nm, r, c, rob, k)            
            count+=1

    # for rob in [10, 15, 20, 30, 50]:     
    #     r, c = 75, 75
    #     nm = f'p{count:02}.pddl'                                
    #     generate(nm, r, c, rob)            
    #     count+=1

    # for r, c in [(3,3), (3,4), (5,5), (5,7), (10,10), (10,15), (20,20), (40,50), (50,50), (50,75)]:
    #     rob = r - 1
    #     nm = f'p{count:02}.pddl'                                
    #     generate(nm, r, c, rob)            
    #     count+=1

