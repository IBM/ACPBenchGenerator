#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path

def is_goal_empty(domain_file : Path, problem_file : Path):
    command = ["validate", str(domain_file.absolute()), str(problem_file.absolute()), "empty_plan"]
    run = subprocess.run(" ".join(command),shell=True, stdout=subprocess.DEVNULL)
    return run.returncode == 0

def generate(name,  r, c, k):
    exec_file = Path(__file__).parent / "generator" / "gold-miner-generator"
    seed = 2020 + k
    command = [str(exec_file.absolute()), "-r", str(r), "-c", str(c), "-s", str(seed)]
    print(command)
    while True:
        with open(name, "w") as f:
            run = subprocess.run(" ".join(command),shell=True, stdout=f)
        if not is_goal_empty(Path("domain.pddl"), Path(name)):
            break


if __name__ == "__main__":
    # The size of the grid is the only parameter
    count = 1
    for r, c in [(3, 3), (3,4), (3,5), (4, 4), (4,5), (5,5)]:
        for k in range(5):
            nm = f'p{count:02}.pddl'                
            generate(nm, r, c, k)            
            count += 1


    # for de in DEPOTS:
    #     p = get_pallets(de)
    #     h = p
    #     c, di, t = 2, 2, 2
    #     for k in range(3):
    #         nm = f'p{count:02}.pddl'                                
    #         generate(nm, de, di, t, p, c, h, k)            
    #         count += 1






