#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path

def is_goal_empty(domain_file : Path, problem_file : Path):
    command = ["validate", str(domain_file.absolute()), str(problem_file.absolute()), "empty_plan"]
    run = subprocess.run(" ".join(command),shell=True, stdout=subprocess.DEVNULL)
    return run.returncode == 0

def generate(name,  de, di, t, p, c, h, k):
    exec_file = Path(__file__).parent / "generator" / "depots"
    command = [str(exec_file.absolute()), "-e", str(de), "-i", str(di), "-t", str(t), "-p", str(p), "-h", str(h), "-c", str(c), "-s", str(2020+k)]
    print(command)
    while True:
        with open(name, "w") as f:
            run = subprocess.run(" ".join(command),shell=True, stdout=f)
        if not is_goal_empty(Path("domain.pddl"), Path(name)):
            break


DEPOTS = [2, 3, 5, 7, 10]
CRATES = [3, 5, 7, 10, 15]
# DISTRIBUTORS = [2]
# TRUCKS = [2]
# PALLETS = [3, 5, 10, 20]
# HOISTS = [3, 5, 10, 15]

def get_pallets(depots):
    import random
    return depots + random.randint(2,3)

if __name__ == "__main__":
    # Pallets == hoists, two or three more than depots
    # Two distributors and trucks
    # Two axes of generalization, depots and crates.
    count = 1
    for de in DEPOTS:
        p = get_pallets(de)
        h = p
        c, di, t = 2, 2, 2
        for k in range(3):
            nm = f'p{count:02}.pddl'                                
            generate(nm, de, di, t, p, c, h, k)            
            count += 1

    for c in CRATES:
        de, di, t = 4, 2, 2
        p = get_pallets(de)
        h = p
        for k in range(3):
            nm = f'p{count:02}.pddl'                                
            generate(nm, de, di, t, p, c, h, k)            
            count+=1




