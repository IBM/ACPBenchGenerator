#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path

def is_goal_empty(domain_file : Path, problem_file : Path):
    command = ["validate", str(domain_file.absolute()), str(problem_file.absolute()), "empty_plan"]
    run = subprocess.run(" ".join(command),shell=True, stdout=subprocess.DEVNULL)
    return run.returncode == 0

def generate(name, s, i, m, t, o, k):
    exec_file = Path(__file__).parent / "generator" / "satgen"
    seed = str(2020 + k)
    args = [str(s), str(i), str(m), str(t), str(o)]
    from_pname = 'strips-sat-x-1'
    to_pname = "prob-" + "-".join(args)
    command = [str(exec_file.absolute()), seed] + args
    while True:
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
    # #s = number of satellites, #i = max instruments/satellite, #m = number of modes, #t = number of targets, #o = number of observations
    # Stabilize #i and #m, vary #s, #t (set #o to #t - 3) 
    count = 1
    i, m = 3, 3
    for s in [1, 3, 5, 7, 10]:
        t = 5
        o = t - 3
        for k in range(3):
            nm = f'p{count:02}.pddl'            
            generate(nm, s, i, m, t, o, k)
            count+=1

    for t in [7, 8, 10, 12, 15]:
        o = t - 3
        s = 6
        for k in range(3):
            nm = f'p{count:02}.pddl'            
            generate(nm, s, i, m, t, o, k)
            count+=1

    # for s, t in [(3, 5), (5, 8), (10, 15), (15, 25), (25, 50)]:
    #     o = t - 3
    #     for k in range(2):
    #         nm = f'p{count:02}.pddl'            
    #         generate(nm, s, i, m, t, o, k)
    #         count+=1
