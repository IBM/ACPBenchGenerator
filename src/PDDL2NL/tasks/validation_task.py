import json
from PDDL2NL.domains import get_translator
from PDDL2NL.utils.translation_util import _list_to_string, choose_action_templates, get_action_description, get_invalid_action_templates, remove_trailing_dot, thoughts_list_to_string, mcq_options
from PDDL2NL.utils.tarski_utils import get_inapplicable_actions, get_lifted_actions_desc, random_path, get_random_invalid_action_name
from PDDL2NL.utils.tarskilite import fix_name, progress, entails


def generate_validation_for_problem_state_mcq(P, state, plan, action_templates, domain, example_id, random):
    if len(plan) == 0:
        return []

    # We generate one positive and three negative cases.
    examples = []
    examples.extend(generate_validation_task_mcq(P, state, plan, None, action_templates, domain, f"{example_id}_yy", random, applicable = True, goal_reached=True, invalid=False))    

    negative_examples = []
    new_seq, last_valid_idx = replace_suffix(P, state, plan, random)
    negative_examples.extend(generate_validation_task_mcq(P, state, new_seq, last_valid_idx, action_templates, domain, f"{example_id}_yn", random, applicable=True, goal_reached=False, invalid=False))

    new_seq, last_valid_idx = make_inapplicable(P, state, plan, random)
    negative_examples.extend(generate_validation_task_mcq(P, state, new_seq, last_valid_idx, action_templates, domain, f"{example_id}_nn", random, applicable=False, goal_reached=False, invalid=False))

    # new_seq, last_valid_idx = make_invalid(P, plan, random)
    ind = random.randint(0,len(plan)-1)
    negative_examples.extend(generate_validation_task_mcq(P, state, plan, ind - 1, action_templates, domain, f"{example_id}_inv", random, applicable=False, goal_reached=False, invalid=True))

    if len(negative_examples) > 0:
        examples.append(random.choice(negative_examples))
    return examples


def generate_validation_for_problem_state_bool(P, state, plan, action_templates, domain, example_id, random):
    if len(plan) == 0:
        return []

    # We generate one positive and three negative cases.
    examples = []
    last_valid_idx = None
    examples.extend(generate_validation_task_applicable_bool(P, state, plan, last_valid_idx, action_templates, domain, f"{example_id}_ya", random, applicable = True))    
    examples.extend(generate_validation_task_valid_bool(P, state, plan, last_valid_idx, action_templates, domain, f"{example_id}_yi", random, invalid= False))
    examples.extend(generate_validation_task_goal_bool(P, state, plan, last_valid_idx, action_templates, domain, f"{example_id}_yg", random, goal_reached= True))

    new_seq, last_valid_idx = replace_suffix(P, state, plan, random)
    examples.extend(generate_validation_task_goal_bool(P, state, new_seq, last_valid_idx, action_templates, domain, f"{example_id}_ng", random, goal_reached=False))

    new_seq, last_valid_idx = make_inapplicable(P, state, plan, random)
    examples.extend(generate_validation_task_applicable_bool(P, state, new_seq, last_valid_idx, action_templates, domain, f"{example_id}_na", random, applicable=False))

    # new_seq, last_valid_idx = make_invalid(P, plan, random)
    ind = random.randint(0,len(plan)-1)
    examples.extend(generate_validation_task_valid_bool(P, state, new_seq, ind - 1, action_templates, domain, f"{example_id}_ni", random, invalid=True))
    return examples

def generate_validation_task_mcq(P, state, plan, last_valid_idx, action_templates, domain, example_id, random, applicable, goal_reached, invalid):
    if plan is None:
        return []
    translator = get_translator(domain)()
    template = choose_action_templates(action_templates[domain], random)

    current_state = translator.get_problem_description(P, state)
    goal_description = translator.get_problem_goal_description(P, P.goal)
    plan_description = [remove_trailing_dot(get_action_description(action, template, P)) for action in plan]
    if invalid:
        invalid_template = choose_action_templates(get_invalid_action_templates(domain), random)
        invalid_action_description = remove_trailing_dot(get_action_description(plan[last_valid_idx+1], invalid_template, P))
        plan_description[last_valid_idx+1] = invalid_action_description

    all_options = ["The sequence is applicable, but does not achieve the goal", "The sequence is a plan", "The sequence is not applicable", "The sequence is not valid"]
    yes_description = []
    no_description = []
    thoughts = ["For a sequence of actions to be a plan, all actions should be valid, applicable in sequence, and achieve the goal."]
    if invalid:
        yes_description.append(all_options[3])
        no_description.extend(all_options[:3])
        thoughts.append(f"The action \"{plan_description[last_valid_idx+1]}\" is not valid in this problem.")
    elif not applicable:
        yes_description.append(all_options[2])
        no_description.extend(all_options[:2]+all_options[3:])
        if last_valid_idx < 0:
            thoughts.append(f"The first action \"{plan_description[0]}\" is not applicable.")
        else:
            thoughts.append(f"The action \"{plan_description[last_valid_idx+1]}\" is not applicable after \"{plan_description[last_valid_idx]}\" is applied.")
    elif goal_reached:
        yes_description.append(all_options[1])
        no_description.extend(all_options[:1]+all_options[2:])
        thoughts.append(f"The action sequence is applicable and it achieves the goal.")
    else:
        yes_description.append(all_options[0])
        no_description.extend(all_options[1:])
        projected_state = state
        for i in range(len(plan)):
            projected_state = progress(projected_state, plan[i])
        unachieved_goals = P.goal - projected_state
        atoms_description = remove_trailing_dot(translator.get_atoms_description(P, unachieved_goals))
        thoughts.append(f"The action sequence is applicable, but the following goal fact(s) are not achieved: {atoms_description}.")
    choices, options, answer_id = mcq_options(yes_description, no_description, random)
    thoughts.append(f"Therefore, the answer is {answer_id}.")
    joint_plan_description = ", \n".join(plan_description)

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "validation_mcq",
                   "context": current_state+ " "+ goal_description,
                   "inputs": f'Which of the following claims is true with regard to the current state and the following sequence of actions: \"{joint_plan_description}\"?\n{options}',
                   "question": f"Is the following sequence of actions applicable in the current state: and does it achieve the goal? \"{joint_plan_description}\" ",
                   "choices": choices,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": answer_id}
    return [example]


def generate_validation_task_valid_bool(P, state, plan, last_valid_idx, action_templates, domain, example_id, random, invalid):
    if plan is None:
        return []
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)

    goal_description = translator.get_problem_goal_description(P, P.goal)
    plan_description = [remove_trailing_dot(get_action_description(action, template, P)) for action in plan]
    if invalid:
        invalid_template = choose_action_templates(get_invalid_action_templates(domain), random)
        invalid_action_description = remove_trailing_dot(get_action_description(plan[last_valid_idx+1], invalid_template, P))
        plan_description[last_valid_idx+1] = invalid_action_description

    thoughts = ["For a sequence of actions to be valid, all actions should be valid."]
    if invalid:
        thoughts.append(f"The action \"{plan_description[last_valid_idx+1]}\" is not valid in this problem.")
    else:
        thoughts.append(f"All the actions in the sequence are valid in this problem.")
    thoughts.append(f'Therefore, the answer is {"yes" if not invalid else "no"}.')
    joint_plan_description = ", \n".join(plan_description)
    input = f'Is the following sequence of actions valid in this problem? \"{joint_plan_description}\" '

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "validation_bool",
                   "context": current_state +" "+ goal_description,
                   "inputs": input,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "yes" if not invalid else "no"}
    return [example]



def generate_validation_task_applicable_bool(P, state, plan, last_valid_idx, action_templates, domain, example_id, random, applicable):
    if plan is None:
        return []
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)

    goal_description = translator.get_problem_goal_description(P, P.goal)
    plan_description = [remove_trailing_dot(get_action_description(action, template, P)) for action in plan]
    thoughts = ["For a sequence of actions to be applicable in the current state, all actions should be valid and each action should be applicable after the previous one is applied."]
    thoughts.append(f"All the actions in the sequence are valid in this problem.")
    if applicable:
        thoughts.append(f"The action sequence is applicable in the current state.")
    else:
        if last_valid_idx < 0:
            thoughts.append(f"The first action \"{plan_description[0]}\" is not applicable.")
        else:
            thoughts.append(f"The action \"{plan_description[last_valid_idx+1]}\" is not applicable after \"{plan_description[last_valid_idx]}\" is applied.")

    thoughts.append(f'Therefore, the answer is {"yes" if applicable else "no"}.')
    joint_plan_description = ", \n".join(plan_description)
    input = f'Is the following sequence of actions applicable in the current state? \"{joint_plan_description}\" '

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "validation_bool",
                   "context": current_state+" "+ goal_description,
                   "inputs": input,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "yes" if applicable else "no"}
    return [example]


def generate_validation_task_goal_bool(P, state, plan, last_valid_idx, action_templates, domain, example_id, random, goal_reached):
    if plan is None:
        return []
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    goal_description = translator.get_problem_goal_description(P, P.goal)
    template = choose_action_templates(action_templates[domain], random)
    plan_description = [remove_trailing_dot(get_action_description(action, template, P)) for action in plan]
    thoughts = ["For a sequence of actions to be a plan, it should be applicable in the current state, all actions should be valid, and the resulting state should entail the goal."]
    thoughts.append(f"All the actions in the sequence are valid in this problem.")
    thoughts.append(f"The action sequence is applicable in the current state.")
    if goal_reached:
        thoughts.append(f"The action sequence achieves the goal.")
    else:
        projected_state = state
        for i in range(len(plan)):
            projected_state = progress(projected_state, plan[i])
        unachieved_goals = P.goal - projected_state
        atoms_description = remove_trailing_dot(translator.get_atoms_description(P, unachieved_goals))
        thoughts.append(f"However, the following goal fact(s) are not achieved: {atoms_description}.")

    thoughts.append(f'Therefore, the answer is {"yes" if goal_reached else "no"}.')
    joint_plan_description = ", \n".join(plan_description)
    input = f'Is the following sequence of actions a plan for the current state?  \"{joint_plan_description}\"'

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "validation_bool",
                   "context": current_state+" "+ goal_description,
                   "inputs": input,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "yes" if goal_reached else "no"}
    return [example]

def replace_suffix(P, state, plan, random):
    # Randomly choose a suffix length to replace with a random path
    suff_len = random.randint(0,len(plan))
    prefix_len = len(plan) - suff_len
    projected_state = state
    for i in range(prefix_len):
        projected_state = progress(projected_state, plan[i])
    
    for i in range(10): # try 10 times and fail
        actions, resulting_state = random_path(P, projected_state, random, depth=suff_len)
        # Check goal
        if not entails(resulting_state, P.goal):
            return plan[:prefix_len] + actions, prefix_len
    return None, None

def replace_with_inapplicable(P, state, plan, random):
    # Randomly choose a state index to replace an action in with inapplicable one
    state_ind = random.randint(0,len(plan))

    projected_states = [state]
    for i in range(state_ind):
        projected_states.append(progress(projected_states[-1], plan[i]))
        
    for i in range(len(projected_states)-2, -1, -1):
        actions = get_inapplicable_actions(P, projected_states[i])
        if len(actions) > 0:
            action = random.choice(actions)
            return plan[:i] + [action] + plan[i+1:], i-1
    return None, None

def make_inapplicable(P, state, plan, random):
    projected_states = [state]
    for i in range(len(plan)):
        projected_states.append(progress(projected_states[-1], plan[i]))
        
    for i in range(len(projected_states)-2, -1, -1):
        actions = get_inapplicable_actions(P, projected_states[i])
        if len(actions) > 0:
            action = random.choice(actions)
            return plan[:i] + [action], i-1
    return None, None

def make_invalid(P, plan, random):
    # Randomly choose an action to replace
    ind = random.randint(0,len(plan)-1)
    a = get_random_invalid_action_name(P, random)
    if a is None:
        return None, None
    new_action = plan[ind]
    new_action.name = a
    return plan[:ind] + [new_action] + plan[ind+1:], ind-1


def generate_validation_for_problem_state_gen(P, state, plan, action_templates, domain, example_id, random):
    if plan is None or len(plan) == 0:
        return []

    new_seq, last_valid_idx = replace_with_inapplicable(P, state, plan, random)
    if not new_seq:
        return []
    
    translator = get_translator(domain)()
    template = choose_action_templates(action_templates[domain], random)

    current_state = translator.get_problem_description(P, state)
    goal_description = translator.get_problem_goal_description(P, P.goal)

    lifted_actions = get_lifted_actions_desc(P, template)
    actions_description = "The available actions are: " + _list_to_string(lifted_actions) + "."

    # plan_description = ", \n".join([remove_trailing_dot(get_action_description(action, template, P)) for action in new_seq])
    plan_description = ["(" + a.name.lower() + ")" for a in new_seq]
    applicable_prefix_description = plan_description[:last_valid_idx+1] if last_valid_idx >= 0 else []
    plan_description_str = " ".join(plan_description)
    applicable_prefix_description_str = " ".join(applicable_prefix_description)

    thoughts = ["For a sequence of actions to be applicable in the current state, all actions should be valid and each action should be applicable after the previous one is applied."]

    IDX_THRESHOLD = 2
    # Two variants, using 
    if last_valid_idx > IDX_THRESHOLD:
        # The actions a1, a2, …, ak are applicable in the current state, resulting in state […]. Action ak+1 is not applicable in the resulting state, since its precondition x does not hold. Therefore, the answer is k+1.

        projected_state = state
        for i in range(last_valid_idx+1):
            projected_state = progress(projected_state, new_seq[i])

        state_desc = remove_trailing_dot(translator.get_atoms_description(P, projected_state))
        thoughts.append(f"The sequence of actions {applicable_prefix_description_str} is applicable in the current state, resulting in the state where {state_desc}.")
    else:
        # The action a1 is applicable in the current state, resulting in state […]. Action a2 is applicable in the resulting state, resulting in state […]. …. Action ak is applicable in the resulting state, resulting in state […]. Action ak+1 is not applicable in the resulting state, since its precondition x does not hold. Therefore, the answer is k+1.
        projected_state = state
        for i in range(last_valid_idx+1):
            current = "current" if i == 0 else "resulting" 
            projected_state = progress(projected_state, new_seq[i])
            state_desc = remove_trailing_dot(translator.get_atoms_description(P, projected_state))
            thoughts.append(f"The action \"{plan_description[0]}\" is applicable in the {current} state, resulting in the state where {state_desc}.")
            

    if last_valid_idx < 0:
        current = "current"
        assert last_valid_idx == -1, f"Last valid index: {last_valid_idx}"
    else:
        current = "resulting"
    missing_prec = new_seq[last_valid_idx+1].pres - projected_state
    assert len(missing_prec) > 0, f"The preconditions {new_seq[last_valid_idx+1].prec} should not hold in the state {projected_state}."
    invalid_prec_desc = remove_trailing_dot(translator.get_atoms_description(P, missing_prec))
    thoughts.append(f"The action \"{plan_description[last_valid_idx+1]}\" is not applicable in the {current} state, since its precondition(s) {invalid_prec_desc} do not hold.")
    thoughts.append(f"Therefore, the answer is {last_valid_idx + 1}.")

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "validation_gen",
                   "context": current_state+ " "+ goal_description + " " + actions_description,
                   "inputs": f'What is the first inapplicable action in the next sequence of actions: \"{plan_description_str}\"?',
                   "targets": thoughts_list_to_string(thoughts),
                   "answer" : last_valid_idx + 1,
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p)
            }
    return [example]