import os
import PDDL2NL.utils as ut
from PDDL2NL.domains import get_translator
from PDDL2NL.utils.tarski_utils import get_lifted_actions_desc
from PDDL2NL.utils.translation_util import _list_to_string, choose_action_templates, get_action_description, remove_trailing_dot, thoughts_list_to_string, mcq_options
from PDDL2NL.utils import tarskilite as tl

def generate_applicable_actions_for_problem_state_mcq(P, state, action_templates, domain, example_id, random):
    applicable_actions = ut.tlu.get_applicable_actions(P, state)
    if len(applicable_actions) == 0:
        # Sink, skipping
        return [] 
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    # Regressively select an applicable action for answer 
    select_lifted_action = random.choice(list(set([i.name.split()[0] for i in applicable_actions])))
    selected_applicable_action = random.choice([i for i in applicable_actions if i.name.split()[0] == select_lifted_action]) 
    precondition_description = remove_trailing_dot(translator.get_atoms_description(P,list(selected_applicable_action.pres)))
    answer = remove_trailing_dot(get_action_description(selected_applicable_action, template, P))
    inapplicable = list(P.actions - set(applicable_actions))
    if len(inapplicable) < 2:
        return []
    if len(inapplicable) > 3:
        inapplicable = random.sample(inapplicable,k=3)
    
    # print(inapplicable)
    # print(answer)
    not_applicable_actions = [remove_trailing_dot(get_action_description(i, template, P)) for i in inapplicable]
    
    choices, options, answer_id = mcq_options([answer], not_applicable_actions, random)
    
    # options = not_applicable_actions+[answer]
    # random.shuffle(options)
    # option_ids=["A","B","C","D"]
    # answer_id = option_ids[options.index(answer)]
    # choices = {"text": options,"label": option_ids}
    # options = " \n".join([ f"{i}. {j}." for i, j in zip(option_ids, options)])
    thoughts =  [f"In order to apply the action \"{answer}\", the following fact(s) must hold in this state: \n{precondition_description}.", 
                 f"These facts hold in the mentioned state, so the action \"{answer}\" is applicable.", 
                 f"Therefore, the answer is {answer_id}."]
    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "applicable_actions_mc",
                   "context": current_state,
                   "inputs": f"Which of the following actions will be applicable in this state?\n{options}",
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "question":  "Which action will be applicable in this state?",
                   "choices": choices,
                   "answer": answer_id}
    return [example]


def generate_applicable_actions_for_problem_state_bool(P, state, action_templates, domain, example_id, random):
    applicable_actions = set(ut.tlu.get_applicable_actions(P, state))
    if len(applicable_actions) == 0:
        # Sink, skipping
        return [] 
    lifted_actions = set([str(a) for a in P.problem.actions])

    non_applicable_actions = P.actions - applicable_actions
    if len(non_applicable_actions) == 0:
        # All actions are applicable, skipping
        return [] 

    app_actions_by_lifted_name = dict()
    inapp_actions_by_lifted_name = dict()

    for a in applicable_actions:
        name = a.name.split()[0]
        if name not in app_actions_by_lifted_name:
            app_actions_by_lifted_name[name] = []
        app_actions_by_lifted_name[name].append(a)

    for a in non_applicable_actions:
        name = a.name.split()[0]
        if name not in inapp_actions_by_lifted_name:
            inapp_actions_by_lifted_name[name] = []
        inapp_actions_by_lifted_name[name].append(a)

    examples = []

    # Choose one applicable action randomly
    name = random.choice(list(app_actions_by_lifted_name.keys()))
    app = random.choice(app_actions_by_lifted_name[name])
    a_name=app.name.replace(" ", "_")
    examples.append(generate_applicable_actions_bool(P, state, action_templates, domain, f"{example_id}_{a_name}_app", random, app))

    name = random.choice(list(inapp_actions_by_lifted_name.keys()))
    inapp = random.choice(inapp_actions_by_lifted_name[name])
    a_name=inapp.name.replace(" ", "_")
    examples.append(generate_applicable_actions_bool(P, state, action_templates, domain, f"{example_id}_{a_name}_inapp", random, inapp))

    # for a in lifted_actions:
    #     if len(actions_by_lifted_name[a]["applicable"]) > 0:
    #         app = random.choice(actions_by_lifted_name[a]["applicable"])
    #         examples.append(generate_applicable_actions_bool(P, state, action_templates, domain, f"{example_id}_{a}_app", random, app))
    #     if len(actions_by_lifted_name[a]["inapplicable"]) > 0:
    #         inapp = random.choice(actions_by_lifted_name[a]["inapplicable"])
    #         examples.append(generate_applicable_actions_bool(P, state, action_templates, domain, f"{example_id}_{a}_inapp", random, inapp))
    return examples

def generate_applicable_actions_bool(P, state, action_templates, domain, example_id, random, action):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    action_description = remove_trailing_dot(get_action_description(action, template, P))
    precondition_description = remove_trailing_dot(translator.get_atoms_description(P,list(action.pres)))
    applicable = tl.entails(state, action.pres)

    answer = "yes" if applicable else "no"
    thoughts =  []
    thoughts.append(f"In order to apply the action \"{action_description}\", the following fact(s) must hold in this state:\n{precondition_description}.")

    # thought = ""
    if applicable:        
        thoughts.append(f"These facts hold in the mentioned state, so the action is applicable.")
        # thought =  f"Step 1:\nIn order to apply the action \"{action_description}\", the following fact(s) must hold in this state:\n{precondition_description}\nStep 2:\nThese facts hold in the mentioned state, so the action is applicable."
    else:
        unsatisfied_pres = list(action.pres - state)
        unsat_description = translator.get_atoms_description(P,unsatisfied_pres)
        thoughts.append(f"The following fact(s) do not hold in the mentioned state:\n{unsat_description} \nSo, the action is not applicable.")
        # thought = f"Step 1:\nIn order to apply the action {action_description}, the following fact(s) must hold in this state:\n{precondition_description}\nStep 2:\nThese facts do not hold in the mentioned state:\n{unsat_description} \nSo, the action is not applicable."

    thoughts.append(f"Therefore, the answer is {answer}.")
    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "applicable_actions_bool",
                   "context": current_state,
                   "inputs": f"Is the following action applicable in this state: \n{action_description}?",
                   "targets":thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": answer}
    return example


def generate_applicable_actions_for_problem_state_gen(P, state, num_actions_bound, action_templates, domain, example_id, random):
    applicable_actions = ut.tlu.get_applicable_actions(P, state)
    if len(applicable_actions) == 0:
        # Sink, skipping
        return [] 
    if len(applicable_actions) > num_actions_bound:
        # Too many actions, skipping
        return [] 

    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)

    lifted_actions = get_lifted_actions_desc(P, template)
    # actions_description = "The available actions with their meaning in parentheses are: " + _list_to_string(lifted_actions) + "."
    actions_description = "The available actions are: " + _list_to_string(lifted_actions) + "."

    applicable_actions_desc = [f"({a.name.lower()})" for a in applicable_actions]

    action = applicable_actions[0]
    action_description = remove_trailing_dot(get_action_description(action, template, P))
    precondition_description = remove_trailing_dot(translator.get_atoms_description(P,list(action.pres)))

    thoughts =  []
    thoughts.append(f"In order for an action to be applicable, its preconditions must hold in the state.")
    thoughts.append(f"For example, the preconditions of action \"{action_description}\" are \"{precondition_description}\", and they hold in the state.")
    thoughts.append(f'Therefore, the answer is [{", ".join(applicable_actions_desc)}].')

    d, p = P.PDDL_replace_init_pddl_parser(state)
    # For scoring the answer, we can use something like Jaccard 
    examples = [{"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "applicable_actions_gen",
                   "context": current_state+ " " + actions_description,
                   "inputs": f"Generate the list of all ground actions that are applicable in this state.",
                   "answer": applicable_actions_desc,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p)
                }]

    return examples
