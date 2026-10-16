#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path

def is_goal_empty(domain_file : Path, problem_file : Path):
    command = ["validate", str(domain_file.absolute()), str(problem_file.absolute()), "empty_plan"]
    run = subprocess.run(" ".join(command),shell=True, stdout=subprocess.DEVNULL)
    print(run.returncode)
    return run.returncode == 0

def generate(name, num_disks):
    exec_file = Path(__file__).parent / "generator" / "hanoi"
    command = [str(exec_file.absolute()), "-n",  str(num_disks)]
    while True:
        with open(name, "w") as f:
            run = subprocess.run(" ".join(command),shell=True, stdout=f)
        if not is_goal_empty(Path("domain.pddl"), Path(name)):
            break
    print( f"{name} finalized")


if __name__ == "__main__":
    count = 1
    for i in range(3,100):
        # for k in range(5):
        nm = f'./generated_instances/p{count:02}.pddl'            
        generate(nm, i)            
        count+=1





