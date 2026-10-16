#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path

def is_goal_empty(domain_file : Path, problem_file : Path):
    command = ["validate", str(domain_file.absolute()), str(problem_file.absolute()), "empty_plan"]
    run = subprocess.run(" ".join(command),shell=True, stdout=subprocess.DEVNULL)
    return run.returncode == 0

def generate(name, x, y, u, r, k):
    exec_file = Path(__file__).parent / "generator" / "grid"
    seed = str(2022 + k)
    command = [str(exec_file.absolute()), "-x", str(x), "-y", str(y), "-u", str(u), "-r", str(r), "-s", seed]
    while True:
        with open(name, "w") as f:
            run = subprocess.run(" ".join(command),shell=True, stdout=f)
        if not is_goal_empty(Path("domain.pddl"), Path(name)):
            break


if __name__ == "__main__":
    """
    -n <num>    size of square grid
    -x <num>    width of rectangular grid
    -y <num>    height of rectangular grid
    -r <num>    ratio of cells in the goal state
    -u <num>    number of unavailable locations ---which are randomly arranged
    -s <num>    random seed (optional)
    """
    # The size of the grid is defined by either -n (square grid) or specifying -x -y
    # Ratio of the cells in the goal state is static, 1
    # Grid size vary and number of unavailable locations vary

    count = 1
    r = 1
    for x, y in [(4,4), (4, 5), (5,5)]:
        for u in [0, 1, 2, 3, 4]:
            for k in range(2):
                nm = f'p{count:02}.pddl'            
                generate(nm, x, y, u, r, k)
                count+=1

