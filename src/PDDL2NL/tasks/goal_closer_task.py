import os
import PDDL2NL.utils as ut
from PDDL2NL.domains import get_translator
from PDDL2NL.utils.tarski_utils import generate_optimal_plans_for_problem_state, get_lifted_actions_desc
from PDDL2NL.utils.translation_util import _list_to_string, choose_action_templates, get_action_description, remove_trailing_dot, thoughts_list_to_string, mcq_options
from PDDL2NL.utils import tarskilite as tl


# def generate_optimal_plans_for_problem_state(P, state, num_plans, timeout):
#     import tempfile
#     with tempfile.NamedTemporaryFile() as domain_temp, \
#          tempfile.NamedTemporaryFile() as problem_temp:
        
#         create_tmp_dom_prob_replace_init(P, state, domain_temp, problem_temp)
#         plans = generate_top_q_plans(domain=str(domain_temp.name), problem=str(problem_temp.name), num_plans=num_plans, quality_bound=1.0, timeout=timeout)
#         # print(plans)
#         if plans is None or len(plans['plans']) == 0:
#             return None
#         return plans['plans']


# def generate_a_plan_for_problem_state(P, state, timeout):
#     import tempfile
#     with tempfile.NamedTemporaryFile() as domain_temp, \
#          tempfile.NamedTemporaryFile() as problem_temp:
        
#         create_tmp_dom_prob_replace_init(P, state, domain_temp, problem_temp)
#         plans = generate_agile_plan(domain=str(domain_temp.name), problem=str(problem_temp.name), timeout=timeout)
#         # print(plans)
#         if plans is None or len(plans['plans']) == 0:
#             return None
#         return plans['plans']


def generate_pos_neg(P, state, random, timeout):
    applicable_actions = ut.tlu.get_applicable_actions(P, state)
    # print(f"Applicable actions: {applicable_actions}")
    if len(applicable_actions) == 0:
        # Sink, skipping
        return None, None, None

    if tl.entails(state, P.goal):
        # print("Current state is a goal state: ", state, P.goal)
        return None, None, None
    # Split the applicable actions into the positive and negative
    # Goal directed progress in state s are actions a such that c*(s) = c*(s[a]) + 1, meaning a is taking us one step closer to the goal.
    plans = generate_optimal_plans_for_problem_state(P, state, num_plans=50, timeout=timeout)
    # print(plans)
    if plans is None:
        return None, None, None

    pos_app = set()
    app_actions_list = [a.name.lower() for a in applicable_actions]
    for plan in plans:
        action = plan["actions"][0]
        
        assert action.lower() in app_actions_list, f"{action} is not in {applicable_actions}"
        a = applicable_actions[app_actions_list.index(action.lower())]
        pos_app.add(a)
    maybe_app = list(set(applicable_actions) - pos_app)
    # print(f"Found {len(pos_app)} actions that start an optimal plan")
    neg_app = set()
    state_len = len(plans[0]["actions"])

    # We only need to choose 3 negative. Choosing randomly, adding
    num_planning_trials = 0
    while len(neg_app) < 3 and len(maybe_app) > 0 and num_planning_trials < 3:
        # randomly choose an action from maybe_app
        i = random.randrange(len(maybe_app))
        action = maybe_app[i]
        maybe_app.pop(i)

        # find a single optimal plan
        t = tl.progress(state, action)
        if t == state:
            continue
        # print(f"Running a planner for negative examples")
        plans_t = generate_optimal_plans_for_problem_state(P, t, num_plans=1, timeout=timeout)
        num_planning_trials += 1
        if plans_t is None:
            continue
        t_len = len(plans_t[0]["actions"])
        if state_len - t_len == 1:
            pos_app.add(action)
        else:
            neg_app.add(action)

    return pos_app, neg_app, len(plans[0]["actions"])

def generate_goal_closer_mcq(P, state, action_templates, domain, example_id, random, timeout):
    pos_app, neg_app, _ = generate_pos_neg(P, state, random, timeout)
    if pos_app is None:
        return []
    
    if len(pos_app) == 0 or len(neg_app) < 2:
        return []

    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    goal_description = translator.get_problem_goal_description(P, P.goal)

    pos = random.choice(list(pos_app))
    answer = remove_trailing_dot(get_action_description(pos, template, P))
    if len(neg_app) > 3:
        neg = random.sample(list(neg_app),k=3)
    else:
        neg = list(neg_app)

    negative_actions = [remove_trailing_dot(get_action_description(i, template, P)) for i in neg]
    
    choices, options, answer_id = mcq_options([answer], negative_actions, random)
    
    thoughts =  [f"In order for an action to take us closer to the goal, it should start an optimal plan.", 
                 f"The action \"{answer}\" starts an optimal plan.", 
                 f"Therefore, the answer is {answer_id}."]
    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "goal_closer_mcq",
                   "context": current_state+" "+ goal_description,
                   "inputs": f"Which of the following actions takes us closer to the goal?\n{options}",
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "choices": choices,
                   "answer": answer_id}
    return [example]


def generate_goal_closer_bool(P, state, action_templates, domain, example_id, random, timeout):
    pos_app, neg_app, _ = generate_pos_neg(P, state, random, timeout)
    if pos_app is None:
        return []
    
    if len(pos_app) == 0 or len(neg_app) == 0:
        return []


    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    goal_description = translator.get_problem_goal_description(P, P.goal)

    pos = random.choice(list(pos_app))
    answer = remove_trailing_dot(get_action_description(pos, template, P))

    examples = []

    thoughts =  [f"In order for an action to take us closer to the goal, it should start an optimal plan.", 
                 f"The action \"{answer}\" starts an optimal plan.", 
                 f"Therefore, the answer is yes."]
    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}_pos",
                   "group": "goal_closer_bool",
                   "context": current_state+" "+ goal_description,
                   "inputs": f"Does the following action take us closer to the goal?\n{answer}",
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "yes"}
    examples.append(example)

    neg = random.choice(list(neg_app))
    answer = remove_trailing_dot(get_action_description(neg, template, P))

    thoughts =  [f"In order for an action to take us closer to the goal, it should start an optimal plan.", 
                 f"The action \"{answer}\" does not start an optimal plan.", 
                 f"Therefore, the answer is no."]
    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}_neg",
                   "group": "goal_closer_bool",
                   "context": current_state+" "+ goal_description,
                   "inputs": f"Does the following action take us closer to the goal?\n{answer}",
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "no"}
    examples.append(example)
    return examples

def generate_goal_closer_gen(P, state, action_templates, domain, example_id, random, timeout):
    # plans = generate_a_plan_for_problem_state(P, state, timeout)
    # if plans is None or len(plans) == 0:
    #     return []
    
    pos_app, neg_app, cost = generate_pos_neg(P, state, random, timeout)
    if pos_app is None:
        return []
    
    applicable_actions = ut.tlu.get_applicable_actions(P, state)
    maybe_actions = set(applicable_actions) - pos_app - neg_app

    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    goal_description = translator.get_problem_goal_description(P, P.goal)

    lifted_actions = get_lifted_actions_desc(P, template)

    # actions_description = "The available actions with their meaning in parentheses are: " + _list_to_string(lifted_actions) + "."
    actions_description = "The available actions are: " + _list_to_string(lifted_actions) + "."

    yes_desc = ["(" + a.name.lower() + ")" for a in pos_app]
    no_desc = ["(" + a.name.lower() + ")" for a in neg_app]
    maybe_desc = ["(" + a.name.lower() + ")" for a in maybe_actions]

    thoughts =  [f"In order for an action to take us closer to the goal, it should start an optimal plan.", 
                 f"Some actions that start optimal plan are {_list_to_string(yes_desc)}.", 
                 f"Therefore, some of the possible answers are {_list_to_string(yes_desc, or_delim=True)}."]

    # d, p = P.PDDL_replace_init(state)
    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}_pos",
                   "group": "goal_closer_gen",
                   "context": current_state+ " "+ goal_description + " " + actions_description,
                #    "inputs": f"What action take us closer to the goal?",
                   "inputs": f"What is the next action that takes us towards the goal?",
                   "answer": {"yes": yes_desc, 
                              "no": no_desc,
                              "maybe": maybe_desc, 
                              "opt": str(cost)},
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p)                              
                }

    return [example]

