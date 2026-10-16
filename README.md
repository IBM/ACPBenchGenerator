# ACPBench Generator

The repo contains code to generate the Action, Change and Planning  benchmark, ACPBench. Refer [this blog](https://ibm.github.io/ACPBench/blog.html) for information about ACPBench and its hard variant.

If you use this benchmark in your work, please cite:

```bibtex
@inproceedings{kokel2025acp,
  author       = {Harsha Kokel and
                  Michael Katz and
                  Kavitha Srinivas and
                  Shirin Sohrabi},
  title        = {ACPBench: Reasoning about Action, Change, and Planning},
  booktitle    = {{AAAI}},
  publisher    = {{AAAI} Press},
  year         = {2025}
}

@inproceedings{kokel2026acphard,
  author       = {Harsha Kokel and
                  Michael Katz and
                  Kavitha Srinivas and
                  Shirin Sohrabi},
  title        = {{ACPBench Hard}: Unrestrained Reasoning about Action, Change, and Planning},
  booktitle    = {{ICLR}},
  publisher    = {OpenReview.net},
  year         = {2026}
}

@inproceedings{baskar2026planforge,
  title        = {PlanForge: Synthesizing Planners from Natural Language with an {LLM}-Driven Architect--Builder--Runner Pipeline},
  author       = {Sarvesh Baskar and
                  Raviteja Bommireddy and
                  Saksham Kumar Sharma and
                  Harsha Kokel and
                  Manas Gaur and
                  Michael Katz and
                  Shirin Sohrabi and
                  Kavitha Srinivas},
  booktitle    = {COLM 2026 Workshop on Efficient Reasoning},
  year         = {2026},
  url          = {https://openreview.net/forum?id=Jx6FT7aaMZ}
}
```

## Repository Structure

```
benchmarks/          # PDDL domain files, pre-generated instances, and per-domain generate.py scripts
  <domain>/
    domain.pddl        # PDDL domain definition
    generated_instances/  # Pre-generated problem instances (.pddl)
    generator/         # Domain-specific instance generator source + Makefile
    generate.py        # Script to regenerate instances for this domain
scripts/             # Top-level generation and utility scripts
  generate_questions.py  # Main entry point for benchmark question generation
  generate_instances.sh  # Convenience script to regenerate all PDDL instances
src/
  PDDL2NL/           # Natural-language templates and per-task question generators
  evaluators/        # Evaluation harness for scoring model outputs
```

## Setup

1. Create Python venv

    ```bash
    python3.12 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    ```

2. Install dependencies and project

    ```bash
    pip install -e .
    ```

    This installs all required Python packages, including
    [`tarski`](https://tarski.readthedocs.io/),
    [`kstar-planner`](https://github.com/IBM/kstar),
    and [`forbiditerative`](https://github.com/IBM/forbiditerative).
    The latter two may require system-level build tools (cmake, a C++ compiler)
    if binary wheels are not available for your platform.

### Additional Dependencies

For the `reachability` and `action_reachability` tasks, the
[CPDDL](https://gitlab.com/danfis/cpddl) library is required. Follow its
README to build it, then export the path to the `pddl` binary:

```bash
export CPDDL_PATH=[CPDDL_HOME]/bin/pddl
```

## Dataset Generation

### Domains

`--domain` accepts a set alias or any individual domain name:

| Value | Domains included |
|---|---|
| `train` | `blocksworld`, `ferry`, `floortile`, `grid`, `grippers`, `logistics`, `rovers`, `visitall` |
| `test` | `alfworld`, `depot`, `goldminer`, `satellite`, `swap` |
| `all` | all of the above |
| *(any domain name)* | that single domain only |

Three additional domains — `hanoi`, `random_hanoi`, and `frogs_jumping` — were added later for the PlanForge work and are not part of the `train`/`test` sets. Pass the domain name directly to use them (e.g. `--domain hanoi`).

### Tasks and question types

¹ Original [ACPBench (AAAI 2025)](https://ibm.github.io/ACPBench/) tasks — see the [blog](https://ibm.github.io/ACPBench/blog.html) for descriptions and examples.
² Added in [ACPBench Hard (ICLR 2026)](https://ibm.github.io/ACPBench/).
³ Added later.

| Task | Description | `mcq` | `bool` | `gen` | Notes |
|---|---|:---:|:---:|:---:|---|
| `applicability` ¹ | Given a state, determine which actions are applicable (valid to execute). | ✓ | ✓ | ✓ | |
| `progression` ¹ | Given a state and an action, determine the resulting state after the action executes. | ✓ | ✓ | ✓ | |
| `reachability` ¹ | Given a state, determine whether a specific sub-goal atom can eventually be reached. | ✓ | ✓ | ✓ | Requires CPDDL (see Additional Dependencies) |
| `action_reachability` ¹ | Given a state, determine whether a specific action can eventually become executable. | ✓ | ✓ | ✓ | Requires CPDDL |
| `validation` ¹ | Given an initial state, a goal, and a sequence of actions, determine whether the sequence is valid and achieves the goal. | ✓ | ✓ | ✓ | |
| `action_justification` ¹ | Given a plan, determine whether a specific action in it is necessary (removing it would break the plan). | ✓ | ✓ | ✓ | |
| `landmarks` ¹ | Given a state and a goal, identify facts that must become true in every plan achieving the goal. | ✓ | ✓ | ✓ | |
| `next_action` ² | Given a state and a goal, identify the next action that makes progress toward the goal. | — | — | ✓ | `gen` only |
| `plan_generation` ³ | Given an initial state and a goal, generate a valid plan. | — | — | ✓ | `gen` only |
| `transitions` ³ | Generate a set of (state, action, next-state) transition tuples from a given state. | — | — | ✓ | `gen` only; requires `--num-transitions` |
| `description` ³ | Generate a natural-language description of the planning problem (initial state, goal, available actions). | — | — | ✓ | `gen` only |
| `distance` ³ | Given a state, determine the minimum number of actions (plan length) needed to reach the goal. | — | — | ✓ | `gen` only |
| `multistep_progression` ³ | Given a state and a sequence of actions, determine the resulting state after all actions execute. | ✓ | ✓ | — | Requires `--depth` or `--min-depth`/`--max-depth` |

### Key options

* `--sample-size` — number of world states sampled per problem instance (default: 200). The number of questions per state varies by question type.
* `--num-plans` — number of plans from the initial state to use for state sampling or directly (e.g. `validation`). Default: 20.
* `--jsons-folder` — directory where output JSON files are written (default: `./`). Use this to avoid cluttering the repo root.
* `--seed` — integer random seed for reproducible output.
* `--verbose` — print timing and generation statistics.

### Example invocations

Training set (`progression`, MCQ):

```bash
python ./scripts/generate_questions.py \
  --domain train --task progression --question-type mcq \
  --sample-size 200 --num-plans 20 --jsons-folder ./output --merge
```

Test set (`progression`, MCQ):

```bash
python ./scripts/generate_questions.py \
  --domain test --task progression --question-type mcq \
  --sample-size 200 --num-plans 20 --jsons-folder ./output --merge
```

Single domain, generative questions:

```bash
python ./scripts/generate_questions.py \
  --domain blocksworld --task plan_generation \
  --jsons-folder ./output
```

### Reachability questions on original problem states

[`scripts/generate_reachability_originalproblem.py`](scripts/generate_reachability_originalproblem.py)
generates boolean reachability questions evaluated against the **initial state** of each problem
instance (rather than sampled intermediate states). Use this when you need questions that are
grounded to the unmodified, original problem. This script follows similar parameters to `generate_questions.py`.

Example usage:

```bash
python ./scripts/generate_reachability_originalproblem.py \
  --domain blocksworld --jsons-folder ./output \
  --json-name run1.json --verbose
```


## Problem Instance Generation

> **Note:** This step is only needed if you want to regenerate the PDDL problem
> instances from scratch. Pre-generated instances are already present in each
> domain's `benchmarks/<domain>/generated_instances/` directory.

Most domains ship with a `generate.py` script under `benchmarks/<domain>/`
that creates instances using a compiled, domain-specific generator binary.
ALFWorld problem instances were generated manually and do not have a
`generate.py` script.

### Prerequisites

* Each domain's generator binary must be compiled. A `Makefile` is provided
  in each `benchmarks/<domain>/generator/` sub-directory — run `make` there
  before regenerating instances.
* The [`validate`](https://github.com/KCL-Planning/VAL) tool (from VAL / PDDL
  validator) must be available on `PATH`. It is used by the generation scripts
  to filter out trivially-solved instances.

### Regenerating all domains

Use the convenience script to run every domain's `generate.py` from its
correct working directory:

```bash
bash scripts/generate_instances.sh
```

To regenerate only specific domains, pass their names as arguments:

```bash
bash scripts/generate_instances.sh blocksworld ferry grippers
```

Supported domains: `blocksworld`, `depot`, `ferry`, `floortile`,
`frogs_jumping`, `goldminer`, `grid`, `grippers`, `hanoi`, `logistics`,
`random_hanoi`, `rovers`, `satellite`, `swap`, `visitall`.

### Regenerating a single domain manually

Each `generate.py` must be run from **inside** its benchmark directory so that
relative file paths resolve correctly:

```bash
cd benchmarks/grippers
python generate.py
```

Generated `.pddl` files will appear in the current directory or in a
`generated_instances/` sub-directory, depending on the domain.
 
## References

Most problem instance generators in `benchmarks/*/generator/` originate from the [AI-Planning/pddl-generators](https://github.com/AI-Planning/pddl-generators) repository, International Planning Competitions (IPC), or domain-specific benchmark repositories:

| Domain | Generator Source / Reference | Description & Origin |
|---|---|---|
| `alfworld` | [ALFWorld](https://github.com/alfworld/alfworld) / [ALFRED](https://github.com/askforalfred/alfred) | Embodied AI benchmark; instances adapted manually without a generator binary |
| `blocksworld` | [pddl-generators/blocksworld](https://github.com/AI-Planning/pddl-generators/tree/main/blocksworld) | Uses Slaney & Thiébaux's `bwstates` generator and IPP `2pddl` translator (AIPS-2000) |
| `depot` | [pddl-generators/depot](https://github.com/AI-Planning/pddl-generators/tree/main/depots) | AIPS-2002 competition generator by Maria Fox and Derek Long |
| `ferry` | [pddl-generators/ferry](https://github.com/AI-Planning/pddl-generators/tree/main/ferry) | IPP domain collection (Albert Ludwigs University Freiburg) |
| `floortile` | [pddl-generators/floortile](https://github.com/AI-Planning/pddl-generators/tree/main/floortile) | IPC-2011 / IPC-2014 generator by Tomás de la Rosa |
| `frogs_jumping` | Custom generator (`benchmarks/frogs_jumping/generator/`) | Frog jumping puzzle domain generator developed for PlanForge |
| `goldminer` | [pddl-generators/goldminer](https://github.com/AI-Planning/pddl-generators/tree/main/goldminer) | IPC-2008 Learning Track generator by Madhu Srinivasan |
| `grid` | [pddl-generators/grid](https://github.com/AI-Planning/pddl-generators/tree/main/grid) | IPP domain collection / AIPS-1998 (Albert Ludwigs University Freiburg) |
| `grippers` | [pddl-generators/gripper](https://github.com/AI-Planning/pddl-generators/tree/main/gripper) | IPP domain collection / IPC-2011 Learning Track (Albert Ludwigs University Freiburg) |
| `hanoi` | [pddl-generators/hanoi](https://github.com/AI-Planning/pddl-generators/tree/main/hanoi) | IPP domain collection (Albert Ludwigs University Freiburg) |
| `logistics` | [pddl-generators/logistics98](https://github.com/AI-Planning/pddl-generators/tree/main/logistics98) | IPP domain collection / AIPS-1998 (Albert Ludwigs University Freiburg) |
| `random_hanoi` | Custom generator (`benchmarks/random_hanoi/generator/`) | Randomized initial/goal Towers of Hanoi generator (based on [pddl-generators/hanoi](https://github.com/AI-Planning/pddl-generators/tree/main/hanoi)) |
| `rovers` | [pddl-generators/rovers](https://github.com/AI-Planning/pddl-generators/tree/main/rovers) | IPC-2002 generator by Derek Long and Maria Fox |
| `satellite` | [pddl-generators/satellite](https://github.com/AI-Planning/pddl-generators/tree/main/satellite) | IPC-2002 generator by Derek Long and Maria Fox |
| `swap` | Custom generator (`benchmarks/swap/generator/`) | Role swap / agent assignment generator developed for ACPBench |
| `visitall` | [pddl-generators/visitall](https://github.com/AI-Planning/pddl-generators/tree/main/visitall) | IPC-2011 / IPC-2014 generator by Nir Lipovetzky and Albert Ludwigs University Freiburg |

## License

This project is licensed under the MIT License.

The original PDDL generators under `benchmarks/*/generator/` are taken as is, with their original licenses attached in their respective directories and source files. In case of any ambiguity or confusion, please refer to the original source links in the [References](#references) section.
