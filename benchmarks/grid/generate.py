#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path

def is_goal_empty(domain_file : Path, problem_file : Path):
    command = ["validate", str(domain_file.absolute()), str(problem_file.absolute()), "empty_plan"]
    run = subprocess.run(" ".join(command),shell=True, stdout=subprocess.DEVNULL)
    return run.returncode == 0

def generate(name, x, y, t, key, lock, k):
    exec_file = Path(__file__).parent / "generator" / "grid"
    seed = str(2020 + k)
    command = [str(exec_file.absolute()), "-x", str(x), "-y", str(y), "-t", str(t), "-k", str(key), "-l", str(lock), "-s", seed]
    while True:
        with open(name, "w") as f:
            run = subprocess.run(" ".join(command),shell=True, stdout=f)
        if not is_goal_empty(Path("domain.pddl"), Path(name)):
            break


if __name__ == "__main__":
    """
    -x <num>    x scale (minimal 1)
    -y <num>    y scale (minimal 1)
    -t <num>    num different key+lock types (minimal 1)
    -k <num>    number keys vector (dezimal)
    -l <num>    number locks vector (dezimal)
    -p <num>    probability of any key being mentioned in the goal (preset: 100)
    -s <num>    random seed (optional)
    """
    # Number of grid size is static
    # Number of keys/locks vary (together), number of key/lock types vary
    # Number of locks must be lower than 10!
    count = 1
    x, y = 5, 5
    for t in [1, 2]:
        for key in [2, 3, 4]:
            lock = key
            for k in range(5):
                nm = f'p{count:02}.pddl'            
                generate(nm, x, y, t, key, lock, k)
                count+=1

