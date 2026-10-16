import math
from PDDL2NL.domains import get_translator
from PDDL2NL.utils.tarskilite import entails, progress
from PDDL2NL.utils.translation_util import _list_to_string, choose_action_templates, get_action_description, get_pddl_domain, remove_trailing_dot
from PDDL2NL.utils.tarski_utils import generate_agile_plan, get_applicable_actions, get_random_applicable_action, random_path
import tempfile

def generate_transitions_for_problem_state(P, state, action_templates, domain, num_transitions, example_id, random):
    if entails(state, P.goal):
        # print("Current state is a goal state: ", state, P.goal)
        return []
    # skipping dead ends as well
    applicable_actions = set(get_applicable_actions(P, state))
    if len(applicable_actions) == 0:
        # Sink, skipping
        return []

    translator = get_translator(domain)()
    template = choose_action_templates(action_templates[domain], random)

    transitions = set()
    num_tries, max_failed_tries = 0, 10
    
    depth = int(math.sqrt(num_transitions))
    while len(transitions) < num_transitions and num_tries < max_failed_tries:
        current = state
        num_before = len(transitions)
        for j in range(depth):
            a = get_random_applicable_action(P, current, random)
            if a is None:
                break
            next = progress(current, a)
            if next == current:
                continue
            s_desc = remove_trailing_dot(translator.get_atoms_description(P, current))
            a_desc = remove_trailing_dot(get_action_description(a, template, P))
            t_desc = remove_trailing_dot(translator.get_atoms_description(P, next))
            transitions.add(tuple((s_desc, a_desc, t_desc, tuple(list(current)), a.name, tuple(list(next)))))
            current = next
        if len(transitions) == num_before:
            num_tries +=1
    examples = []

    for i, tr in enumerate(transitions):

        examples.append({"id": f"{domain}_{P.problem.name}_{example_id}_{i}",
                        "group": "transition_generation",
                        "from_state": tr[0],
                        "to_state": tr[2],
                        "action": tr[1],
                        "from_state_symbolic": tr[3],
                        "to_state_symbolic": tr[5],
                        "action_symbolic": tr[4]
                        })
    return examples
