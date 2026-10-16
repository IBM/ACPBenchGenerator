#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path

def is_goal_empty(domain_file : Path, problem_file : Path):
    command = ["validate", str(domain_file.absolute()), str(problem_file.absolute()), "empty_plan"]
    run = subprocess.run(" ".join(command),shell=True, stdout=subprocess.DEVNULL)
    return run.returncode == 0

def generate(name,  l, c):
    exec_file = Path(__file__).parent / "generator" / "ferry"
    command = [str(exec_file.absolute()), "-l", str(l), "-c", str(c)]
    print(command)
    while True:
        with open(name, "w") as f:
            run = subprocess.run(" ".join(command),shell=True, stdout=f)
        if not is_goal_empty(Path("domain.pddl"), Path(name)):
            break



if __name__ == "__main__":
    # Two axes of generalization: locations & cars
    count = 1
    for l in [2, 3, 5, 10, 20]:
        for c in [2, 3, 5, 10, 20, 50]:
            nm = f'p{count:02}.pddl'                                
            generate(nm, l, c)            
            count+=1




