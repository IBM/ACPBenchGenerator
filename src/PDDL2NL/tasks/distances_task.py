import time
from PDDL2NL.domains import get_translator
from PDDL2NL.utils.tarskilite import entails, progress
from PDDL2NL.utils.translation_util import _list_to_string, choose_action_templates, remove_trailing_dot
from PDDL2NL.utils.tarski_utils import generate_optimal_plans_for_problem_state, get_applicable_actions, get_lifted_actions_desc, state_as_sorted_tuple
import uuid

def generate_problem_distances(P, state, action_templates, domain, example_id, random):
    if entails(state, P.goal):
        return []
    # skipping dead ends as well
    applicable_actions = set(get_applicable_actions(P, state))
    if len(applicable_actions) == 0:
        return []

    start = time.time()
    translator = get_translator(domain)()
    template = choose_action_templates(action_templates[domain], random)


    goal_description = translator.get_problem_goal_description(P, P.goal)
    lifted_actions = get_lifted_actions_desc(P, template)

    # actions_description = "The available actions with their meaning in parentheses are: " + _list_to_string(lifted_actions) + "."
    actions_description = "The available actions are: " + _list_to_string(lifted_actions) + "."
    problem_description = ""

    init = translator.get_domain_description() 
    if len(init) > 0:
        problem_description += init + " \n"
    obj_desc = translator.get_objects_description(P) 
    if len(obj_desc) > 0:
        problem_description += obj_desc + " \n"
    static_desc = translator.get_static_atoms_description(P) 
    if len(static_desc) > 0:
        problem_description += static_desc + " \n"
    
    plans = generate_optimal_plans_for_problem_state(P, state, num_plans=100, timeout=60)
    # print(plans)
    if plans is None or len(plans) == 0:
        return []
    # print(f"Found {len(plans)} plans.")
    # print(plans)

    examples = []
    opt = len(plans[0]["actions"])
    d, p = P.PDDL_pddl_parser()
    init_description = remove_trailing_dot(translator.get_atoms_description(P, state))

    # Getting states from plans
    states = set()
    for plan in plans:
        plan_id = uuid.uuid4()
        s = state
        state_index = 0
        opt = len(plan["actions"])
        examples.append(get_example(P, domain, example_id, plan_id, state_index, problem_description, init_description, goal_description, state, plan["actions"], opt, actions_description, d, p))
        for action in plan["actions"]:
            applicable_actions = get_applicable_actions(P, s)
            app_actions_list = [a.name.lower() for a in applicable_actions]
            assert action.lower() in app_actions_list, f"{action} is not in {applicable_actions}"
            a = applicable_actions[app_actions_list.index(action.lower())]
            s = progress(s, a)
            # if entails(s, P.goal):
            #     break
            opt -= 1
            state_index += 1
            init_description = remove_trailing_dot(translator.get_atoms_description(P, s))
            examples.append(get_example(P, domain, example_id, plan_id, state_index, problem_description, init_description, goal_description, s, plan["actions"][state_index:], opt, actions_description, d, p))

            # t = state_as_sorted_tuple(s)
            # states.add(tuple((t, opt)))
    # for s, opt in states:
    #     s = set(s)
    #     init_description = remove_trailing_dot(translator.get_atoms_description(P, s))
    #     examples.append(get_example(P, domain, example_id, problem_description, init_description, goal_description, s, opt, actions_description, d, p))
    print(f"{domain}_{P.problem.name}_{example_id} generated {len(examples)} entries in {time.time()-start}s")
    return examples

def get_example(P, domain, example_id, plan_id, state_index, problem_description, init_description, goal_description, state, actions, opt, actions_description, d, p):
    return {"id": f"{domain}_{P.problem.name}_{example_id}_{plan_id}_{state_index}",
                    "group": "distances_generation",
                    "plan_id": f"{plan_id}",
                    "problem": problem_description,
                    "state_description": init_description,
                    "goal_description": goal_description,
                    "state": [f"({f.strip()})" for f in state],
                    "goal": [f"({f.strip()})" for f in P.goal],
                    "plan": [f"({a.strip()})" for a in actions],
                    "goal_distance": opt,
                    "actions": actions_description,
                    "PDDL_domain" : str(d),
                    "PDDL_problem" : str(p)
                    }
