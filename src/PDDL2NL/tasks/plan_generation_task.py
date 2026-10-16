from PDDL2NL.domains import get_translator
from PDDL2NL.utils.tarskilite import entails, progress
from PDDL2NL.utils.translation_util import _list_to_string, choose_action_templates, get_action_description, get_pddl_domain, remove_trailing_dot, thoughts_list_to_string
from PDDL2NL.utils.tarski_utils import generate_a_plan_for_problem, generate_a_plan_for_problem_state, generate_agile_plan, generate_an_optimal_plan_for_problem, get_applicable_actions
import tempfile


def get_real_plan(P, plan, state):
    real_plan = []
    s = state
    for action in plan:
        applicable_actions = get_applicable_actions(P, s)
        app_actions_list = [a.name.lower() for a in applicable_actions]
        assert action.lower() in app_actions_list, f"{action} is not in {applicable_actions}"
        a = applicable_actions[app_actions_list.index(action.lower())]
        s = progress(s, a)
        real_plan.append(a)
    return real_plan

def get_plan_partial_order(P, plan, state):
    # Getting a sequential plan and finding the pairs of actions that must be in that order (one provides precondition for the other)
    # Returns a list of index pairs
    pairs = {}
    atoms = {}
    # print("Generating POCL for a plan")
    s = set(list(state)[:])
    for i, a in enumerate(plan):
        for p in a.adds - s:
            atoms[p] = i
            # print(f"Action {i}.{a.name} achieves atom {p}")
        s = progress(s, a)
        for p in a.pres:
            if p in atoms:
                # print(f"Action {i}.{a.name} precondition {p} is achieved by action {atoms[p]}")
                if atoms[p] not in pairs:
                    pairs[atoms[p]] = i
    goals = set()
    for p in P.goal:
        if p in atoms:
            goals.add(atoms[p])
            # assert atoms[p] not in pairs, f"{atoms[p]}.{plan[atoms[p]].name}, indices: {pairs}"
            # if atoms[p] not in pairs:
            # pairs[atoms[p]] = -1
    return pairs, goals


def generate_plan_for_problem_state(P, state, action_templates, domain, example_id, random, timeout):
    if entails(state, P.goal):
        # print("Current state is a goal state: ", state, P.goal)
        return []
    # skipping dead ends as well
    applicable_actions = set(get_applicable_actions(P, state))
    if len(applicable_actions) == 0:
        # Sink, skipping
        return []

    # d, p = P.PDDL_replace_init(state)
    d, p = P.PDDL_replace_init_pddl_parser(state)

    # plans = generate_a_plan_for_problem(d, p, timeout)
    plans = generate_an_optimal_plan_for_problem(d, p, timeout)
    # print(plans)
    if plans is None or len(plans) == 0:
        return []
    plan = plans[0]["actions"]
    plan_desc = [f"({f})" for f in plan]
    real_plan = get_real_plan(P, plan, state)
    causal_links, goals = get_plan_partial_order(P, real_plan, state)

    thoughts = []
    thoughts.append("Each action on a plan is there for achieving either the goal or some following action precondition.")
    # print(f"Plan: {plan_desc}")
    for i, a in enumerate(real_plan):
        # assert i in causal_links
        j = None
        if i in causal_links:
            j = causal_links[i]
        achieves_goals = i in goals

        if j:
            if achieves_goals:
                thoughts.append(f"The action ({real_plan[i].name}) achieves goal fact(s) as well as preconditions of the action ({real_plan[j].name}).")
            else:
                thoughts.append(f"The action ({real_plan[i].name}) achieves preconditions of the action ({real_plan[j].name}).")
            # print(f"{i}.{real_plan[i].name} (add: {real_plan[i].adds}) -> {j}.{real_plan[j].name} (pre: {real_plan[j].pres})")
        else:
            assert achieves_goals, f"{i}  - State: {state}, Goal: {P.goal}, Plan: {plan}, causal links: {causal_links}, goals: {goals}"
            thoughts.append(f"The action ({real_plan[i].name}) achieves goal fact(s).")
            # print(f"{i}.{real_plan[i].name} (add: {real_plan[i].adds}) -> goal {P.goal}")
    # print("-------------------------------------------------------------")
    thoughts.append(f'Therefore one possible plan is {plan_desc}.')

    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    lifted_actions = []
    template = choose_action_templates(action_templates[domain], random)

    for aname, a in P.problem.actions.items():
        n = aname + " " + " ".join([str(par) for par in a.parameters])
        desc = remove_trailing_dot(get_action_description(n, template, P))

        # lifted_actions.append(f"{n.lower()} ({desc})")
        lifted_actions.append(f"({n.lower()}) - {desc}")

    # actions_description = "The available actions with their meaning in parentheses are: " + _list_to_string(lifted_actions) + "."
    actions_description = "The available actions are: " + _list_to_string(lifted_actions) + "."
    goal_description = translator.get_problem_goal_description(P, P.goal)

    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                    "group": "plan_generation",
                    "context": current_state+ " "+ goal_description + " " + actions_description,
                    "inputs": f'Generate a plan, a sequence of actions that is applicable to the current state and achieves the goal.',
                    "example_plan" : plan,
                    "targets": thoughts_list_to_string(thoughts),
                    "PDDL_domain" : str(d),
                    "PDDL_problem" : str(p)
                    }
    return [example]
