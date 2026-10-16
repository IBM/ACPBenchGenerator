#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path

def is_goal_empty(domain_file : Path, problem_file : Path):
    command = ["validate", str(domain_file.absolute()), str(problem_file.absolute()), "empty_plan"]
    run = subprocess.run(" ".join(command),shell=True, stdout=subprocess.DEVNULL)
    return run.returncode == 0

def generate(name, a, c, s, p, k):
    exec_file = Path(__file__).parent / "generator" / "logistics"
    seed = str(2020 + k)
    command = [str(exec_file.absolute()), "-a", str(a), "-c", str(c), "-s", str(s), "-p", str(p), "-t", str(c), "-r", seed]
    while True:
        with open(name, "w") as f:
            run = subprocess.run(" ".join(command),shell=True, stdout=f)
        if not is_goal_empty(Path("domain.pddl"), Path(name)):
            break


if __name__ == "__main__":
    """
    -a <num>    number of airplanes
    -c <num>    number of cities (minimal 1)
    -s <num>    city size(minimal 1)
    -p <num>    number of packages (minimal 1)
    -t <num>    number of trucks (optional, default and minimal: same as number of cities; there will be at least one truck per city)
    -r <num>    random seed (minimal 1, optional)
    """
    # Number of airplanes is 1, number of tracks is minimal (one per city) 
    # Number of cities and city size vary (together), number of packages vary  
    count = 1
    a = 1
    for c, s in [(2, 2), (2, 3), (3, 3), (5, 3), (5, 10)]:
        p = 4 
        for k in range(3):
            nm = f'p{count:02}.pddl'            
            generate(nm, a, c, s, p, k)
            count+=1

    for p in [5, 7, 10, 15, 20]:
        c, s = 3, 3
        for k in range(3):
            nm = f'p{count:02}.pddl'            
            generate(nm, a, c, s, p, k)
            count+=1

