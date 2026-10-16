from PDDL2NL.domains import get_translator
from PDDL2NL.utils.translation_util import _list_to_string, _nth, choose_action_templates, get_action_description, remove_trailing_dot, thoughts_list_to_string, mcq_options
from PDDL2NL import utils as ut
from PDDL2NL.utils.tarski_utils import get_applicable_actions, get_lifted_actions_desc, goal_met
import time

def generate_examples_action_justification_for_problem_state_mcq(P, state, plan, action_templates, domain, example_id, random):
    if len(plan) == 0:
        return []

    examples = []  #pick one single and one pair

    plan = plan_to_action_plan(P, plan)
    #truncate the plan
    plan = _truncate_plan(P, plan)

    #consider single action
    occurence_dic, invalid_plan = _remove_one_and_validate(P,  plan)

    if (occurence_dic != {} and len(invalid_plan) >= 3): 
        action = random.choice(list(occurence_dic.keys()))
        occurence = random.choice(occurence_dic[action])
        examples.extend(generate_action_justification_task_mcq(P, state, plan, action_templates, domain, f"{example_id}_yy", random, invalid_plan, action, occurence, None))    

    if len(examples) > 0:
        return examples
    
    #consider immediate pairs of actions
    valid_plan, invalid_plan = _remove_two_and_validate(P,  plan)

    if (len(valid_plan) > 0 and len(invalid_plan) >= 3):
        valid_pair = random.choice(valid_plan)
        examples.extend(generate_action_justification_task_mcq(P, state, plan, action_templates, domain, f"{example_id}_yx", random, invalid_plan, None, None, valid_pair))    

    if len(examples) > 0:
        return examples
    
    # Try to extend the plan with a pair of invertible actions
    new_plan, _ = _add_invertible_to_plan(P, plan, random)
    if new_plan is None:
        return examples
    
    valid_plan, invalid_plan = _remove_two_and_validate(P,  new_plan)
    if (len(valid_plan) > 0 and len(invalid_plan) >= 3):
        valid_pair = random.choice(valid_plan)
        examples.extend(generate_action_justification_task_mcq(P, state, new_plan, action_templates, domain, f"{example_id}_yx", random, invalid_plan, None, None, valid_pair))    

    return  examples



def generate_examples_action_justification_for_problem_state_bool(P, state, plan, action_templates, domain, example_id, random):
    if len(plan) == 0:
        return []

    examples = []  #adding one positive, one negative one for pair and one for single (4 total per plan)
    plan = plan_to_action_plan(P, plan)
    #truncate the plan
    plan = _truncate_plan(P, plan)

    #consider single action
    occurence_dic, invalid_plan = _remove_one_and_validate(P,  plan)
    added_negative_example = False
    #single case
    if len(invalid_plan) > 0 :
        # all actions that can't be removed 
        action = random.choice(invalid_plan)
        examples.extend(generate_action_justification_task_bool(P, state, plan, action_templates, domain, f"{example_id}_yn", random, action, None, None, valid = False))
        added_negative_example = True   
        
    if occurence_dic != {}:  #all actions that can be removed with their occurence number
        action = random.sample(list(occurence_dic), 1)[0]
        occurence = random.choice(occurence_dic[action])
        examples.extend(generate_action_justification_task_bool(P, state, plan, action_templates, domain, f"{example_id}_yi", random, action, occurence, None, valid = True))

    # One positive and one negative are enough
    if len(examples) == 2:
        return examples

    #consider immediate pairs of actions
    valid_plan, invalid_plan = _remove_two_and_validate(P,  plan)
    if len(invalid_plan) > 0 and not added_negative_example : # pairs of actions that can't be removed
        pair = random.choice(invalid_plan)
        examples.extend(generate_action_justification_task_bool(P, state, plan, action_templates, domain, f"{example_id}_yv", random, None, None, pair, valid = False))   
    
    if len(examples) == 2:
        return examples

    if len(valid_plan) > 0: #pairs of actions that can be removed
        pair = random.choice(valid_plan)
        examples.extend(generate_action_justification_task_bool(P, state, plan, action_templates, domain, f"{example_id}_yz", random, None, None, pair, valid = True))   
    else:
        # Try another positive case - adding invertible actions to a valid plan
        new_plan, pair = _add_invertible_to_plan(P, plan, random)
        if new_plan is not None:
            examples.extend(generate_action_justification_task_bool(P, state, new_plan, action_templates, domain, f"{example_id}_yz", random, None, None, pair, valid = True))   

    return examples


#truncate a plan so that only at most 2 actions are made after the goal is reached
#return the truncated plan, the plan itself if no extra actions are made after the goal is reached.
def truncate_plan(P, plan):
    goal_not_met_yet = True
    #find the index where goal is met
    for i in range(0, len(plan)+1):
        if (i == len(plan)):
            return plan
        plancopy = plan[:i]
        valid = is_valid_plan(P, plancopy)
        if (valid and not goal_not_met_yet):  #this could be just one step after the goal is reached and is a valid plan
            #print("goal met once, looking for another place where goal can be met and truncating")
            return plancopy
        if valid and goal_not_met_yet: #goal is reached, just keep 2 extra actions
            goal_not_met_yet = False
            if (len(plan)-i < 3):  #can't remove more than 2 actions, return the original plan
                return plan
            else:
                possible_plan = plan[:i+2]
                if is_valid_plan(P, possible_plan): #it is possible to not be able to truncate
                    return plan[:i+2]             

# TODO: understand the desired behavior:
# Say the sequence of states is s0->g1->s2->s3->g4->s5>g6, where do we want to truncate, after g1 or after g4
def _truncate_plan(P, plan):
    goal_was_already_observed = False
    #find the index where goal is met
    current_state = P.init
    for i in range(0, len(plan)+1):
        if (i == len(plan)):
            return plan
        if goal_met(current_state, P):
            if goal_was_already_observed:  #this could be just one step after the goal is reached and is a valid plan
                #print("goal met once, looking for another place where goal can be met and truncating")
                return plan[:i]
            else: #goal is reached, just keep 2 extra actions
                goal_was_already_observed = True
                if (len(plan) <= i + 2):  #can't remove more than 2 actions, return the original plan
                    return plan
                else:
                    # Check that taking the next two actions is still a valid plan
                    n_state = ut.tl.progress(current_state, plan[i])
                    if goal_met(n_state, P):
                        return plan[:i+1]
                    nn_state = ut.tl.progress(n_state, plan[i+1])
                    if goal_met(nn_state, P):
                        return plan[:i+2]
        current_state = ut.tl.progress(current_state, plan[i])      

# removes all actions from the plan and returns
# occurence_dic: list of actions together with their occurence/instance number where after removing them the plan was still valid
# invalid_plan: list of actions such that after removing them from the plan, the plan is no longer valid
def remove_one_and_validate(P, plan):
    occurence_dic = {}
    invalid_plan = []
    #for each action, remove the action and test if the plan is still valid
    for i in range(0, len(plan)):
        action = plan[i]
        plancopy = plan[:i] + plan[i+1:]
        valid = is_valid_plan(P, plancopy)
        if valid:
            if action in occurence_dic:
                occurence_dic[action].append(get_occurence_number(i, action, plan)) 
            else:
                occurence_dic[action] = [get_occurence_number(i, action, plan)]
        else:
            invalid_plan.append(action)

    return occurence_dic, invalid_plan


def _remove_one_and_validate(P, plan):
    occurrences = _get_occurence_by_index(plan)
    occurrence_dic = {}
    invalid_plan = []
    #for each action, remove the action and test if the plan is still valid
    current_state = P.init
    for i in range(0, len(plan)):
        action = plan[i]
        # Checking suffix 
        if _is_valid_state_plan(P, current_state, plan[i+1:]):
            if action not in occurrence_dic:
                occurrence_dic[action] = []
            occurrence_dic[action].append(occurrences[i]) 
        else:
            invalid_plan.append(action)
        current_state = ut.tl.progress(current_state, action)

    return occurrence_dic, invalid_plan
#removes all immediate pairs of actions from the plan and returns two sets:
#valid_plan: list of actions pairs such that after removing these two actions, the plan was still valid
#invalid_plan: list of actions pairs such that such that after removing these two actions, the plan was no longer valid
def remove_two_and_validate(P, plan):
    valid_plan = []
    invalid_plan = []
    #for each two subsequent actions, remove both of the actions and test if the plan is still valid
    for i in range(0, len(plan)-1): 
        actions = plan[i:i+2]
        plancopy = plan[:i] + plan[i+2:] 
        valid = is_valid_plan(P, plancopy)
        if valid:
            valid_plan.append(actions)
        else:
            invalid_plan.append(actions)

    return valid_plan, invalid_plan

def _remove_two_and_validate(P, plan):
    valid_plan = []
    invalid_plan = []
    #for each two subsequent actions, remove both of the actions and test if the plan is still valid
    current_state = P.init
    for i in range(0, len(plan)-1): 
        actions = plan[i:i+2]
        if _is_valid_state_plan(P, current_state, plan[i+2:]):
            valid_plan.append(actions)
        else:
            invalid_plan.append(actions)

        current_state = ut.tl.progress(current_state, plan[i])
    return valid_plan, invalid_plan


#Get the action accurance for this plan at this index
# Example: plan={a, b, a, e, d, a, f} index = 2, occurence = 2, at index 0, occurence = 1
def get_occurence_number(index, action, plan): 
    count = 0
    i = 0
    for a in plan:
        if (action == a and i <= index):
            count += 1
        i += 1
    return count


def _get_occurence_by_index(plan): 
    d = {}
    ret = []
    for a in plan:
        if a.name not in d:
            d[a.name] = 0
        d[a.name] += 1
        ret.append(d[a.name])
    return ret


#Checking to see if the plan is valid or not
def is_valid_plan(P, plan):
    current_state = P.init
    for action in plan:
        action = str(action).lower()
        applicable_actions = get_applicable_actions(P, current_state)
        app_actions_list = [a.name.lower() for a in applicable_actions]
        if action not in app_actions_list:
            return False
        a = applicable_actions[app_actions_list.index(action)]
        current_state = ut.tl.progress(current_state, a)
    
    if (not goal_met(current_state, P)):
        return False
    
    return True


def _is_valid_plan(P, plan):
    return _is_valid_state_plan(P, P.init, plan)

def _is_valid_state_plan(P, current_state, plan):
    t = current_state.copy()
    for a in plan:
        if not ut.tl.entails(t, a.pres):
            return False
        t = ut.tl.progress(t, a)    
    return goal_met(t, P)



def plan_to_action_plan(P, plan):
    current_state = P.init
    action_plan = []
    for action in plan:
        action = action.name.lower()
        applicable_actions = get_applicable_actions(P, current_state)
        app_actions_list = [a.name.lower() for a in applicable_actions]
        if action not in app_actions_list:
            print(f"Action missing: {action}")
            print(f"From action list {app_actions_list}")
            return False
        a = applicable_actions[app_actions_list.index(action)]
        action_plan.append(a)
        current_state = ut.tl.progress(current_state, a)
    
    assert (goal_met(current_state, P))
    return action_plan


def _add_invertible_to_plan(P, plan, random):
    current_state = P.init
    # Try to add a pair of invertible at the current state
    applicable_actions = get_applicable_actions(P, current_state)
    for x in applicable_actions:
        Y = P.get_invertible_actions(x)
        if len(Y) > 0:
            y = random.choice(Y)
            act_y = P.action(y)
            test_plan = [x,act_y] + plan
            if _is_valid_plan(P, test_plan):
                return test_plan, [x, act_y]
    for i, a in enumerate(plan):
        current_state = ut.tl.progress(current_state, a)
        # Try to add a pair of invertible at the current state
        applicable_actions = get_applicable_actions(P, current_state)
        for x in applicable_actions:
            Y = P.get_invertible_actions(x)
            if len(Y) > 0:
                y = random.choice(Y)
                act_y = P.action(y)
                test_plan = plan[:i] + [x,act_y] + plan[i:]
                if _is_valid_plan(P, test_plan):
                    return test_plan, [x, act_y]

    return None, None



def generate_action_justification_task_mcq(P, state, plan, action_templates, domain, example_id, random, invalid_plan, action, occurence, pair):
    if plan is None:
        return []

    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)

    plan_description = [remove_trailing_dot(get_action_description(action, template, P)) for action in plan]
    plan_description = ", ".join(plan_description)
    goal_description = translator.get_problem_goal_description(P, P.goal)
    thoughts = []
    question = ""
    choices = ""
    wrong_options = []

    if action and occurence: #single action
        action_desc = remove_trailing_dot(get_action_description(action, template, P))

        for wrong_option in invalid_plan:
            wrong_options.extend([remove_trailing_dot(get_action_description(wrong_option, template, P))])
        wrong_options = [x for x in wrong_options if x != action_desc]

        if len(wrong_options) < 2:
            return []
        if len(wrong_options) > 3:
            wrong_options = random.sample(wrong_options, k=3)
        
        choices, options, answer_id = mcq_options([action_desc], wrong_options, random)

        if len([x for x in plan if x == action]) > 1:
            action_occur = f"The {_nth(occurence)} instance of the action"
        else:
            action_occur = "The action"

        inputs = f"Given the plan: \"{plan_description}\"; which of the following actions can be removed from this plan and still have a valid plan? \n{options}"
        question = f"Given the plan: \"{plan_description}\"; which action can be removed from this plan?"
        thoughts.append(f"A valid plan is a sequence of actions that is executable from the current state and achieves the goal. ")
        thoughts.append(f"{action_occur} \"{action_desc}\" can be removed from the plan and still have a valid plan.")
        thoughts.append(f"Therefore, the answer is {answer_id}.")
    
    else: #pair
        action_desc = remove_trailing_dot(get_action_description(pair[0], template, P)) + " and " + remove_trailing_dot(get_action_description(pair[1], template, P))

        for wrong_option in invalid_plan:
            wrong_option_des = remove_trailing_dot(get_action_description(wrong_option[0], template, P)) + " and " + remove_trailing_dot(get_action_description(wrong_option[1], template, P))
            wrong_options.extend([wrong_option_des])
        wrong_options = [x for x in wrong_options if x != action_desc]

        if len(wrong_options) > 3:
            wrong_options = random.sample(wrong_options, k=3)

        choices, options, answer_id = mcq_options([action_desc], wrong_options, random)
 

        inputs = f"Given the plan: \"{plan_description}\"; which of the following pairs of consecutive actions can be removed from this plan and still have a valid plan? \n{options}"
        question = f"Given the plan: \"{plan_description}\"; which pair of consecutive actions can be removed from this plan?"
        thoughts.append(f"A valid plan is a sequence of actions that is executable from the current state and achieves the goal. ")
        if P.check_invertible(pair[0], pair[1]):
            thoughts.append(f"Consecutive actions \"{action_desc}\" invert each other and therefore can be removed from the plan and still have a valid plan.")
        else:
            thoughts.append(f"Consecutive actions \"{action_desc}\" can be removed from the plan and still have a valid plan.")

        thoughts.append(f"Therefore, the answer is {answer_id}.")


    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "action_justification_mcq",
                   "context": current_state + " " +  goal_description,
                   "inputs": inputs,
                   "question": question,
                   "choices": choices,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": answer_id}
    return [example]
   



def generate_action_justification_task_bool(P, state, plan, action_templates, domain, example_id, random, action, occurence, pair, valid):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    plan_description = [remove_trailing_dot(get_action_description(action, template, P)) for action in plan]
    plan_description = ", ".join(plan_description)
    goal_description = translator.get_problem_goal_description(P, P.goal)
    thoughts = []

    if pair:
        action_desc = remove_trailing_dot(get_action_description(pair[0], template, P)) + " and " + remove_trailing_dot(get_action_description(pair[1], template, P))
        inputs = f"Given the plan: \"{plan_description}\"; can the following pair of consecutive actions be removed from this plan and still have a valid plan: \n{action_desc}?"
        thoughts.append(f"A valid plan is a sequence of actions that is executable from the current state and achieves the goal. ")
        
        if valid:
            if P.check_invertible(pair[0], pair[1]):
                thoughts.append(f"Consecutive actions \"{action_desc}\" invert each other and therefore can be removed from the plan and still have a valid plan.")
            else:
                thoughts.append(f"Consecutive actions \"{action_desc}\" can be removed from the plan and still have a valid plan.")
            thoughts.append(f"Therefore, the answer is yes.")

        else: 
            thoughts.append(f"Consecutive actions \"{action_desc}\" cannot be removed from the plan and still have a valid plan.")
            thoughts.append(f"Therefore, the answer is no.")

    else:
        action_desc = remove_trailing_dot(get_action_description(action, template, P))
        inputs = f"Given the plan: \"{plan_description}\"; can the following action be removed from this plan and still have a valid plan: \n{action_desc}?"
        thoughts.append(f"A valid plan is a sequence of actions that is executable from the current state and achieves the goal. ")


        if (action and occurence and valid): #single action, also ensuring that it is valid
            if len([x for x in plan if x == action]) > 1:
                action_occur = f"The {_nth(occurence)} instance of the action"
            else:
                action_occur = "The action"

            thoughts.append(f"{action_occur} \"{action_desc}\" can be removed from the plan and still have a valid plan.")
            thoughts.append(f"Therefore, the answer is yes.")

        else:
            thoughts.append(f"\"{action_desc}\" cannot be removed from the plan and still have a valid plan.")
            thoughts.append(f"Therefore, the answer is no.")

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "action_justification_bool",
                   "context": current_state + " " +  goal_description,
                   "inputs": inputs,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "yes" if valid else "no"}     

    return [example]

def generate_examples_action_justification_for_problem_state_gen(P, state, plan, action_templates, domain, example_id, random):
    if len(plan) == 0:
        return []

    examples = []  
    plan = plan_to_action_plan(P, plan)
    #truncate the plan
    plan = _truncate_plan(P, plan)

    #consider single action
    occurence_dic, neg_act = _remove_one_and_validate(P,  plan)

    pos_act = []
    # dict to list
    for a, occ in  occurence_dic.items():
        pos_act.extend([[f"({a.name.lower()})", str(i)] for i in occ])

    #consider immediate pairs of actions
    valid_plan, invalid_plan = _remove_two_and_validate(P,  plan)

    for t in valid_plan:
        pos_act.append([f"({a.name.lower()})" for a in t] + ["-1"])

    neg_act = [f"({a.name.lower()})" for a in neg_act]
    neg_act = sorted(list(set(neg_act)))
    neg_act.extend(invalid_plan)
    if len(pos_act) > 0:
        examples.extend(generate_action_justification_task_gen(P, state, plan, action_templates, domain, f"{example_id}_r", random, pos_act, neg_act))   
    else:
        # Try another positive case - adding invertible actions to a valid plan
        new_plan, pair = _add_invertible_to_plan(P, plan, random)
        if new_plan is not None:
            pos_act = [f"({a.name.lower()})" for a in pair] + ["-1"]
            examples.extend(generate_action_justification_task_gen(P, state, new_plan, action_templates, domain, f"{example_id}_e", random, [pos_act], []))
    return examples


def get_reduced_plan(plan, toremove, occurrence=None):
    if len(toremove) > 1:
        for i, a in enumerate(plan):
            if a.name == toremove[0].name and plan[i+1].name == toremove[1].name:
                return plan[:i] + plan[i+2:]
    else:
        assert occurrence is not None
        assert occurrence > 0
        cnt = 0
        for i, a in enumerate(plan):
            if a.name == toremove[0].name:
                cnt += 1
                if cnt == occurrence:
                    return plan[:i] + plan[i+1:]
    return None


def generate_action_justification_task_gen(P, state, plan, action_templates, domain, example_id, random, pos, neg):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    # plan_description = [remove_trailing_dot(get_action_description(action, template, P)) for action in plan]
    plan_description = [f"({action.name.lower()})" for action in plan]
    plan_description = " ".join(plan_description)
    goal_description = translator.get_problem_goal_description(P, P.goal)

    actions_description = "The available actions are: " + _list_to_string(get_lifted_actions_desc(P, template)) + "."

    # inputs = f"Given the plan: \"{plan_description}\"; what single action or a pair of consecutive actions can be removed from this plan and still have a valid plan, if any?"
    inputs = f"Simplify the plan \"{plan_description}\" by removing either a single action or a pair of consecutive actions, while still maintaining a valid plan. Provide the resulting simplified plan."

    thoughts =  []
    thoughts.append(f"A valid plan is a sequence of actions that is executable from the current state and achieves the goal. ")
    t = pos[0]
    # print(t)
    if len(t) > 2:
        fa = P.get_action_or_none(t[0]) 
        sa = P.get_action_or_none(t[1])
        assert fa is not None
        assert sa is not None
        
        # print(fa, sa)
        # action_desc = remove_trailing_dot(get_action_description(fa, template, P)) + " and " + remove_trailing_dot(get_action_description(sa, template, P))
        action_desc = f"({fa.name.lower()}) and ({sa.name.lower()})"
        if P.check_invertible(fa, sa):
            thoughts.append(f"Consecutive actions \"{action_desc}\" invert each other and therefore can be removed from the plan and still have a valid plan.")
        else:
            thoughts.append(f"Consecutive actions \"{action_desc}\" can be removed from the plan and still have a valid plan.")

        reduced_plan = get_reduced_plan(plan, [fa, sa])
    else:
        action = P.get_action_or_none(t[0])
        # action_desc = remove_trailing_dot(get_action_description(action, template, P))
        action_desc = f"({action.name.lower()})"
        occurrence = int(t[1])
        # print(f"Occurrence: {occurrence}")
        if len([x for x in plan if x == action]) > 1:
            action_occur = f"The {_nth(occurrence)} instance of the action"
        else:
            action_occur = "The action"
            occurrence = 1

        thoughts.append(f"{action_occur} \"{action_desc}\" can be removed from the plan and still have a valid plan.")
        reduced_plan = get_reduced_plan(plan, [action], occurrence=occurrence)

    reduced_plan_description = [f"({action.name.lower()})" for action in reduced_plan]
    reduced_plan_description = " ".join(reduced_plan_description)
    thoughts.append(f"Therefore, a possible answer is [{reduced_plan_description}].")


    # d, p = P.PDDL_replace_init(state)
    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "action_justification_gen",
                   "context": current_state + " " +  actions_description + " " +  goal_description,
                   "inputs": inputs,
                   "answer": pos,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p)
              }     

    return [example]
