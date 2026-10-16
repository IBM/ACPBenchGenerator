#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path

def is_goal_empty(domain_file : Path, problem_file : Path):
    command = ["validate", str(domain_file.absolute()), str(problem_file.absolute()), "empty_plan"]
    run = subprocess.run(" ".join(command),shell=True, stdout=subprocess.DEVNULL)
    return run.returncode == 0

def generate(name, n, r, o, k):
    exec_file = Path(__file__).parent / "generator" / "grippers"
    seed = str(2020 + k)
    command = [str(exec_file.absolute()), "-n", str(n), "-r", str(r), "-o", str(o), "-s", seed]
    while True:
        with open(name, "w") as f:
            run = subprocess.run(" ".join(command),shell=True, stdout=f)
        if not is_goal_empty(Path("domain.pddl"), Path(name)):
            break


if __name__ == "__main__":
    """
    -n <num>    number of robots (minimal 1)
    -r <num>    number of rooms (minimal 1)
    -o <num>    number of balls (minimal 1)
    -s <num>    random seed (optional)
    """
    # Number of robots is 1 (more robots means easier to solve)
    # Number of rooms vary, number of balls vary  
    count = 1
    n = 1
    for r in [2, 3, 5, 7, 10]:
        o = 4 
        for k in range(2):
            nm = f'p{count:02}.pddl'            
            generate(nm, n, r, o, k)
            count+=1

    for o in [5, 7, 10, 15, 20]:
        r = 3
        for k in range(2):
            nm = f'p{count:02}.pddl'            
            generate(nm, n, r, o, k)
            count+=1

    for r, o in [(3, 4), (5, 8), (10, 12), (15, 25), (25, 50)]:
        for k in range(2):
            nm = f'p{count:02}.pddl'            
            generate(nm, n, r, o, k)
            count+=1
