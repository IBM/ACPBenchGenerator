#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path

def is_goal_empty(domain_file : Path, problem_file : Path):
    command = ["validate", str(domain_file.absolute()), str(problem_file.absolute()), "empty_plan"]
    run = subprocess.run(" ".join(command),shell=True, stdout=subprocess.DEVNULL)
    return run.returncode == 0

def generate(name, r, w, o, c, g, k):
    exec_file = Path(__file__).parent / "generator" / "rovgen"
    seed = str(2020 + k)
    args = [str(r), str(w), str(o), str(c), str(g)]
    from_pname = f'roverprob{seed}'
    to_pname = "prob-" + "-".join(args) + "-" + seed
    command = [str(exec_file.absolute()), seed] + args
    while True:
        print(command)
        with open(name, "w") as f:
            run = subprocess.run(" ".join(command),shell=True, stdout=f)
            # Replace filename
        with open(name, "r") as f:
            s = f.read()
        with open(name, 'w') as f:
            s = s.replace(from_pname, to_pname)
            f.write(s)
        if not is_goal_empty(Path("domain.pddl"), Path(name)):
            break


if __name__ == "__main__":
    # <seed> <#rovers> <#waypoints> <#objectives> <#cameras> <#n-goals>
    # Stabilize <#rovers> <#cameras> , vary <#objectives> and <#waypoints>, setting <#n-goals> to one of these  
    count = 1
    r, c = 2, 2
    for g in [3, 5, 7, 10, 15]:
        o, w = g, 3
        for k in range(3):
            nm = f'p{count:02}.pddl'            
            generate(nm, r, w, o, c, g, k)
            count+=1

        o, w = 2, g
        for k in range(3):
            nm = f'p{count:02}.pddl'            
            generate(nm, r, w, o, c, g, k)
            count+=1

    # for o, w in [(3, 5), (5, 8), (10, 15), (15, 25), (25, 50)]:
    #     g = o
    #     for k in range(2):
    #         nm = f'p{count:02}.pddl'            
    #         generate(nm, r, w, o, c, g, k)
    #         count+=1
