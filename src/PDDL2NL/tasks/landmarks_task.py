from pathlib import Path
from PDDL2NL.domains import get_translator
from PDDL2NL.utils.pddl_utils import check_is_landmark
from PDDL2NL.utils.translation_util import _list_to_string, choose_action_templates, get_action_description, remove_trailing_dot, thoughts_list_to_string, mcq_options
from PDDL2NL.utils.tarski_utils import create_tmp_dom_prob_replace_init, generate_agile_plan, generate_top_q_plans, get_applicable_actions, generate_landmarks, get_lifted_atoms_desc, random_trace_no_loops, generate_plans
from PDDL2NL.utils.tarskilite import entails, fix_name, progress
import time


    

def generate_landmarks_for_state(state, goal, tmp_domain_file, tmp_problem_file):
    # Compute the landmarks
    # print("Computing landmarks for problem in ", tmp_domain_file, tmp_problem_file)
    landmarks = generate_landmarks(tmp_domain_file, tmp_problem_file)
    # print("Landmarks result error: ", landmarks["planner_error"])
    # Skip disjunctive, skip negated atoms, skip those that are true in init or goal
    ret = []
    goal_land = []
    init_land = []
    for l in landmarks["landmarks"]:
        if l["disjunctive"] == 'True': 
            continue
        for f in l["facts"]:
            name = f
            if f.startswith("Atom"):
                name = fix_name(f[5:])

                if name not in goal | state:
                    ret.append(name)
                elif name in goal - state:
                    goal_land.append(name)
                else:
                    init_land.append(name)

    return ret, init_land, goal_land

def generate_non_landmarks_for_state(P, state, tmp_domain_file, tmp_problem_file, timeout):
    # s_time = time.time()
    plans = generate_top_q_plans(domain=tmp_domain_file, problem=tmp_problem_file, num_plans=20, quality_bound=1.0, timeout=timeout)
    # e_time = time.time()
    # print(f" {len(plans['plans'])} Plans generated in {e_time - s_time:0.2f} seconds.")
    if plans is None or len(plans['plans']) == 0:
        return None, None
        # # Try a satisficing planner first
        # plans = generate_agile_plan(domain=tmp_domain_file, problem=tmp_problem_file, timeout=timeout)
        # if plans is None or len(plans['plans']) == 0:
        #     return None, None
    atoms = P.fluents.copy()
    ret_plans = []
    for plan in plans['plans']:
        plan_atoms = get_atoms_along_plan(P, state, plan["actions"])
        atoms &= plan_atoms 
        ret_plans.append(tuple((plan_atoms, plan["actions"])))

    potential = atoms | state | P.goal
    not_landmarks = P.fluents - potential
    return not_landmarks, ret_plans

def get_atoms_along_plan(P, state, plan):
    current_state = state
    atoms = set()

    for action in plan:
        applicable_actions = get_applicable_actions(P, current_state)
        app_actions_list = [a.name.lower() for a in applicable_actions]
        assert action.lower() in app_actions_list, f"{action} is not in {applicable_actions}"
        a = applicable_actions[app_actions_list.index(action.lower())]
        current_state = progress(current_state, a)
        atoms |= current_state
    return atoms


def generate_reachable_atoms_on_random_path(P, state, random):
    atoms = set()
    for i in range(10):
        states = random_trace_no_loops(P, state, random, depth=3)
        for s in states:
            atoms |= (s - (state | P.goal))
        if len(atoms) > 2:
            break
    if len(atoms) == 0:
        return None
    return atoms

def generate_landmarks_for_problem_state_mcq(P, state, action_templates, domain, example_id, random, timeout):
    if entails(state, P.goal):
        # print("Current state is a goal state: ", state, P.goal)
        return []
    import tempfile
    with tempfile.NamedTemporaryFile() as domain_temp, \
         tempfile.NamedTemporaryFile() as problem_temp:

        # Create the files
        create_tmp_dom_prob_replace_init(P, state, domain_temp, problem_temp)

        s_time = time.time()
        landmarks, init_land, goal_land = generate_landmarks_for_state(state, P.goal, tmp_domain_file=str(domain_temp.name), tmp_problem_file=str(problem_temp.name))
        l_time = time.time() - s_time

        if len(landmarks) == 0:
            # No non-trivial landmarks
            # print("No non-trivial landmarks")
            if len(goal_land) > 0:
                landmarks = goal_land
                # print("Using goal landmarks instead") 
            elif len(init_land) > 0:
                print("No goal landmarks, but there are init landmarks - should not happen!")
                return []
            else:
                print("Init: ", state)
                print("Goal: ", P.goal)
                return []
        if landmarks[0] in ["dummy val1", "dummy val2"]:
            # Unsolvable task (Fast Downward translator creates a dummy unsolvable task), neither positive or negative example is created
            print("Unsolvable task, no landmarks")
            return []

        # print(f"Total of {len(landmarks)} landmarks")
        s_time = time.time()
        q_atoms, _ = generate_non_landmarks_for_state(P,state, tmp_domain_file=str(domain_temp.name), tmp_problem_file=str(problem_temp.name), timeout=timeout)
        nl_time = time.time() - s_time
        # print(f"{example_id} landmarks/non-landmarks generated in {l_time:0.2f}/{nl_time:0.2f} seconds.")
        s_time = time.time()
        if q_atoms is None:
            print("No non-landmark facts")
            return []

        q_atoms = q_atoms - set(landmarks)
        # print(f"Total of {len(q_atoms)} non-landmarks")
        if len(q_atoms) < 2:
            return []
        
        # We randomly choose atoms from four sets (when not empty) 
        yes_atoms = set()
        no_atoms = set()
        # if not trivial_landmarks or random.random() < 0.8:
        # Disabling the non-of-the-above option
        yes_atoms.add(random.choice(list(landmarks)))

        if len(q_atoms) < 3:
            no_atoms = q_atoms
        else:
            no_atoms = random.sample(list(q_atoms), k=3)

        return [generate_landmarks_task_mcq(P, state, action_templates, domain, f"{example_id}", random, list(yes_atoms), list(no_atoms))]


def generate_landmarks_for_problem_state_bool(P, state, action_templates, domain, example_id, random, timeout):
    if entails(state, P.goal):
        # print("Current state is a goal state: ", state, P.goal)
        return []
    import tempfile
    with tempfile.NamedTemporaryFile() as domain_temp, \
         tempfile.NamedTemporaryFile() as problem_temp:

        # Create the files
        create_tmp_dom_prob_replace_init(P, state, domain_temp, problem_temp)

        examples = []
        landmarks, init_land, goal_land = generate_landmarks_for_state(state, P.goal, tmp_domain_file=str(domain_temp.name), tmp_problem_file=str(problem_temp.name))
        if len(landmarks) > 0:
            # print("Landmarks:", landmarks)
            question_atom = random.choice(list(landmarks))
            # print("Selected:", question_atom)
            if question_atom in ["dummy val1", "dummy val2"]:
                # Unsolvable task (Fast Downward translator creates a dummy unsolvable task), neither positive or negative example is created
                return [] 
        else:
            question_atom = random.choice(list(goal_land))

        examples.append(generate_landmarks_task_bool(P, state, action_templates, domain, f"{example_id}_y", random, None, question_atom, True))

        q_atoms, plans_pairs = generate_non_landmarks_for_state(P,state, tmp_domain_file=str(domain_temp.name), tmp_problem_file=str(problem_temp.name), timeout=timeout) 
        if q_atoms is None:
            return examples
        q_atoms = q_atoms - set(landmarks)
        if len(q_atoms) > 0:
            # print(q_atoms)
            question_atom = random.choice(list(q_atoms))
            for atoms, plan in plans_pairs:
                if question_atom not in atoms:  
                    examples.append(generate_landmarks_task_bool(P, state, action_templates, domain, f"{example_id}_n", random, plan, question_atom, False))
                    break
        return examples


def generate_landmarks_task_mcq(P, state, action_templates, domain, example_id, random, yes_atoms, no_atoms):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)

    yes_atoms_description = [remove_trailing_dot(translator.get_atoms_description(P, atom)) for atom in yes_atoms]
    no_atoms_description = [remove_trailing_dot(translator.get_atoms_description(P, atom)) for atom in no_atoms]
    choices, options, answer_id = mcq_options(yes_atoms_description, no_atoms_description, random)

    thoughts = []
    thoughts.append("A fact is a landmark if it must hold at some point along any plan.")
    if len(yes_atoms) > 0:
        thoughts.append(f'The fact \"{yes_atoms_description[0]}\" can be found by a simple procedure that traces back such atoms from the goal.')
    else:
        thoughts.append('None of the mentioned facts hold along all plans.')
    thoughts.append(f"Therefore, the answer is {answer_id}.")

    goal_description = translator.get_problem_goal_description(P, P.goal)

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "landmarks_mcq",
                   "context": current_state +" "+ goal_description,
                   "inputs": f"Which of the following facts is a landmark (must hold at some point along any plan) for the current state?\n{options}",
                   "question": f"Which fact must hold at some point on any way to the goal from the current state?",
                   "choices": choices,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": answer_id}
    return example

def generate_landmarks_task_bool(P, state, action_templates, domain, example_id, random, plan, question_atom, is_landmark):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)

    # print(question_atom)
    atom_description = remove_trailing_dot(translator.get_atom_description(P, question_atom))
    # print(atom_description)

    thoughts = []
    thoughts.append("A fact is a landmark if it must hold at some point along any plan.")
    if is_landmark:
        thoughts.append(f'The fact \"{atom_description}\" can be found by a simple procedure that traces back such atoms from the goal.')
        thoughts.append(f"Therefore, the answer is yes.")
    else:
        assert(plan is not None)
        real_plan = [P.action_map[a] for a in plan]
        template = choose_action_templates(action_templates[domain], random)

        action_descriptions = ", \n".join([remove_trailing_dot(get_action_description(a, template, P)) for a in real_plan])
        thoughts.append(f'The fact \"{atom_description}\" is not achieved along the following plan\n{action_descriptions}.')
        thoughts.append(f"Therefore, the answer is no.")

    goal_description = translator.get_problem_goal_description(P, P.goal)

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "landmarks_bool",
                   "context": current_state +" "+ goal_description,
                   "inputs": f"Is the following fact a landmark (must hold at some point along any plan) for the current state?\n{atom_description}",
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "yes" if is_landmark else "no"}
    # print(example)
    return example


def generate_landmarks_for_problem_state_gen(P, state, action_templates, domain, example_id, random, timeout):
    if entails(state, P.goal):
        # print("Current state is a goal state: ", state, P.goal)
        return []
    import tempfile
    with tempfile.NamedTemporaryFile() as domain_temp, \
         tempfile.NamedTemporaryFile() as problem_temp:

        # Create the files
        d, p = create_tmp_dom_prob_replace_init(P, state, domain_temp, problem_temp)

        examples = []
        landmarks, init_land, goal_land = generate_landmarks_for_state(state, P.goal, tmp_domain_file=str(domain_temp.name), tmp_problem_file=str(problem_temp.name))
        # print("Landmarks:", landmarks, "Init landmarks:", init_land, "Goal landmarks:", goal_land)
        # if len(landmarks) == 0:
        #     return []

        if len(landmarks) > 0 and landmarks[0] in ["dummy val1", "dummy val2"]:
            landmarks = []

        q_atoms, _ = generate_non_landmarks_for_state(P,state, tmp_domain_file=str(domain_temp.name), tmp_problem_file=str(problem_temp.name), timeout=timeout) 
        if q_atoms:
            q_atoms -= set(landmarks)
        else:
            q_atoms = set()
        # print("Non-landmarks:", q_atoms)

        maybe = P.fluents - set(landmarks) - q_atoms - state - P.goal
        if len(maybe) > 0 and len(maybe) <= 10:
            # Checking for landmarks
            land_count = 0
            non_land_count = 0
            for atom in maybe:
                if check_is_landmark(str(d).lower(), str(p).lower(), f"({atom.strip()})"):
                    # Adding to landmarks
                    landmarks.append(atom)
                    land_count += 1
                else:
                    q_atoms.add(atom)
                    non_land_count += 1
            maybe = []
            print(f"Number of landmarks changed is land: {land_count}, non land: {non_land_count}.")

        if len(maybe) > 0:
            # Can't process, too many maybes
            return []
        q_atoms = list(q_atoms)

        
        examples.append(generate_landmarks_task_gen(P, state, action_templates, domain, example_id, landmarks, list(q_atoms)))
        return examples


def generate_landmarks_task_gen(P, state, action_templates, domain, example_id, landmarks, q_atoms):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)

    lifted_atoms = get_lifted_atoms_desc(P, translator)
    atoms_description = "The available propositions are: " + _list_to_string(lifted_atoms) + "."

    goal_description = translator.get_problem_goal_description(P, P.goal)

    yes_desc = [f"({a.strip()})" for a in landmarks]
    no_desc = [f"({a.strip()})" for a in q_atoms]


    thoughts = []
    thoughts.append("A fact is a landmark if it must hold at some point along any plan.")
    if len(yes_desc) > 0:
        thoughts.append(f'The fact(s) {_list_to_string(yes_desc)} can be found by a simple procedure that traces back such atoms from the goal.')
        thoughts.append(f"Therefore, possible answers are {_list_to_string(yes_desc, or_delim=True)}.")
    else:
        thoughts.append(f'For each of the facts that do not hold in the initial state or goal, there is a plan along which the fact is not achieved.')
        thoughts.append('Therefore there are no non-trivial fact landmarks and the answer is None.')

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "landmarks_gen",
                   "context": current_state +" "+ goal_description + " " + atoms_description,
                   "inputs": f"Generate a non-trivial fact landmark, one that does not hold in the initial state or goal.",
                   "answer": {"yes": yes_desc, 
                              "no": no_desc},
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p)           
                }
    # print(example)
    return example
