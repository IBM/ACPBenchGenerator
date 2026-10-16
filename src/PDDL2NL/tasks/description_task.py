from PDDL2NL.domains import get_translator
from PDDL2NL.utils.tarskilite import entails
from PDDL2NL.utils.translation_util import _list_to_string, choose_action_templates, remove_trailing_dot
from PDDL2NL.utils.tarski_utils import get_applicable_actions, get_lifted_actions_desc

def generate_problem_description(P, action_templates, domain, example_id, random):
    # TODO: ensure it never happens and remove
    if entails(P.init, P.goal):
        print("Initial state is a goal state: ", P.init, P.goal)
        return []
    # skipping dead ends as well
    applicable_actions = set(get_applicable_actions(P, P.init))
    if len(applicable_actions) == 0:
        print("Initial state is a sink state: ", P.init)
        return []

    translator = get_translator(domain)()
    template = choose_action_templates(action_templates[domain], random)

    init_description = remove_trailing_dot(translator.get_atoms_description(P, P.init))
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
    

    examples = []

    d, p = P.PDDL_pddl_parser()

    examples.append({"id": f"{domain}_{P.problem.name}_{example_id}",
                    "group": "description_generation",
                    "problem": problem_description,
                    "init_state": init_description,
                    "goal": goal_description,
                    "actions": actions_description,
                    "PDDL_domain" : str(d),
                    "PDDL_problem" : str(p)
                    })
    return examples
