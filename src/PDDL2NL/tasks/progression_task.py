from PDDL2NL.domains import get_translator
from PDDL2NL.utils.translation_util import _list_to_string, choose_action_templates, get_action_description, remove_trailing_dot, thoughts_list_to_string, mcq_options
from PDDL2NL.utils.tarski_utils import get_lifted_atoms_desc, get_random_applicable_action, random_path
from PDDL2NL.utils.tarskilite import fix_name, progress


def random_random_applicable_action(P, state, random):
    a = get_random_applicable_action(P, state, random, lifted_random=True)
    if a is None:
        return None, None
    return a, progress(state,a)
    

def generate_progression_for_problem_state_mcq(P, state, action_templates, domain, example_id, random):
    # actions, resulting_state = random_path(P, state, random, depth=1)
    # if len(actions) == 0:
    #     # No applicable actions
    #     return []
    # action = actions[0]
    
    action, resulting_state = random_random_applicable_action(P, state, random)
    if action is None:
        return []

    # We randomly choose atoms from four sets (when not empty) 
    yes_atoms = set()
    no_atoms = set()
    # Yes/Yes
    target_atoms = resulting_state & state
    if len(target_atoms) > 0:
        pre_atoms = action.pres & target_atoms
        if len(pre_atoms) > 0:
            # Give preference to precondition
            yes_atoms.add(random.choice(list(pre_atoms)))
        else:
            yes_atoms.add(random.choice(list(target_atoms)))

    # Yes/No
    target_atomsyn = state - resulting_state
    if len(target_atomsyn) > 0:
        no_atoms.add(random.choice(list(target_atomsyn)))

    # No/Yes
    target_atomsny = resulting_state - state
    if len(target_atomsny) > 0:
        yes_atoms.add(random.choice(list(target_atomsny)))

    # No/No
    target_atomsnn = set()
    for symbol in P.fluent_symbols():
        relaxed_reachable = (set([fix_name(x) for x in P.get_grounded_atoms(symbol).dump()]) - resulting_state) - state
        target_atomsnn |= relaxed_reachable
    if len(target_atomsnn) > 0:
        if len(target_atomsyn) > 0 or len(target_atomsnn) == 1:
            no_atoms.add(random.choice(list(target_atomsnn)))
        else:
            no_atoms.update(set(random.sample(list(target_atomsnn), k=2)))


    # if len(yes_atoms | no_atoms) < 2 or len(no_atoms) == 0:
    #     return []
    
    # if len(no_atoms) == 1 and len(yes_atoms) < 2:
    #     return []
    # Simplifying the condition 
    if len(yes_atoms) == 0 or len(yes_atoms | no_atoms) < 3:
        return []
    
    # print(f"Yes options {len(yes_atoms)}, No options {len(no_atoms)} (out of {len(target_atomsyn)} YN atoms and {len(target_atomsnn)} NN atoms)")
    return [generate_progression_task_mcq(P, state, action_templates, domain, f"{example_id}", random, action, list(yes_atoms), list(no_atoms))]


def generate_progression_for_problem_state_bool(P, state, action_templates, domain, example_id, random):
    # actions, resulting_state = random_path(P, state, random, depth=1)
    # if len(actions) == 0:
    #     # No applicable actions
    #     return []
    # action = actions[0]

    action, resulting_state = random_random_applicable_action(P, state, random)
    if action is None:
        return []

    examples = []
    # Yes/Yes
    target_atoms = resulting_state & state
    if len(target_atoms) > 0:
        question_atom = random.choice(list(target_atoms))
        examples.append(generate_progression_task_bool(P, state, action_templates, domain, f"{example_id}_yy", random, action, question_atom, True))

    # Yes/No
    target_atoms = state - resulting_state
    if len(target_atoms) > 0:
        question_atom = random.choice(list(target_atoms))
        examples.append(generate_progression_task_bool(P, state, action_templates, domain, f"{example_id}_yn", random, action, question_atom, False))

    # No/Yes
    target_atoms = resulting_state - state
    if len(target_atoms) > 0:
        question_atom = random.choice(list(target_atoms))
        examples.append(generate_progression_task_bool(P, state, action_templates, domain, f"{example_id}_ny", random, action, question_atom, True))

    # No/No
    target_atoms = set()
    for symbol in P.fluent_symbols():
        relaxed_reachable = (set([fix_name(x) for x in P.get_grounded_atoms(symbol).dump()]) - resulting_state) - state
        target_atoms |= relaxed_reachable
    if len(target_atoms) > 0:
        question_atom = random.choice(list(target_atoms))
        examples.append(generate_progression_task_bool(P, state, action_templates, domain, f"{example_id}_nn", random, action, question_atom, False))
    return examples


def generate_progression_task_mcq(P, state, action_templates, domain, example_id, random, action, yes_atoms, no_atoms):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    action_description = remove_trailing_dot(get_action_description(action, template, P))

    yes_atoms_description = [remove_trailing_dot(translator.get_atoms_description(P, atom)) for atom in yes_atoms]
    no_atoms_description = [remove_trailing_dot(translator.get_atoms_description(P, atom)) for atom in no_atoms]
    choices, options, answer_id = mcq_options(yes_atoms_description, no_atoms_description, random)

    thoughts = []
    if len(yes_atoms) == 0:
        thoughts.append(f"Check which of the facts hold after performing the action \"{action_description}\".")
        thoughts.append(f"None of these facts hold after performing the action.")
    elif len(yes_atoms) == 1:
        # If a single atom, just return the positive thought
        question_atom_in_state = yes_atoms[0] in state
        # question_atom_description = remove_trailing_dot(translator.get_atoms_description(P, yes_atoms))
        thoughts = generate_thought(P, translator, action_description, yes_atoms, action, question_atom_in_state, True,state)
    else:
        # If two atoms, if both are either in state or not, generate a single positive thought
        question_first_atom_in_state = yes_atoms[0] in state
        question_second_atom_in_state = yes_atoms[1] in state
        if question_first_atom_in_state == question_second_atom_in_state:
            # question_atom_description = remove_trailing_dot(translator.get_atoms_description(P, yes_atoms))
            thoughts = generate_thought(P, translator, action_description, yes_atoms, action, question_first_atom_in_state, True, state)
        else:
            # merging thoughts
            # question_atom_description = remove_trailing_dot(translator.get_atoms_description(P, yes_atoms[0]))
            first_thoughts = generate_thought(P, translator, action_description, yes_atoms[0], action, question_first_atom_in_state, True,state)
            # question_atom_description = remove_trailing_dot(translator.get_atoms_description(P, yes_atoms[1]))
            second_thoughts = generate_thought(P, translator, action_description, yes_atoms[1], action, question_second_atom_in_state, True, state)
            second_to_last = remove_trailing_dot(first_thoughts[-2]) + " and " + second_thoughts[-2].split(f'The action \"{action_description}\"')[1]
            last = remove_trailing_dot(first_thoughts[-1]) + " and " + second_thoughts[-1]

            thoughts = first_thoughts[:-2] + second_thoughts[:-2] + [second_to_last] + [last] 
    # Add the last thought
    thoughts.append(f"Therefore, the answer is {answer_id}.")

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "progression_mcq",
                   "context": current_state,
                   "inputs": f"Which of the following facts hold after performing the action \"{action_description}\" in the current state?\n{options}",
                   "question": f"Which fact will hold after performing the action \"{action_description}\" in the current state?",
                   "choices": choices,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": answer_id}
    return example

def generate_progression_task_bool(P, state, action_templates, domain, example_id, random, action, question_atom, holds_next_state):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    action_description = get_action_description(action, template, P)
    question_atom_description = remove_trailing_dot(translator.get_atoms_description(P, question_atom))
    question_atom_in_state = question_atom in state
    answer = "yes" if holds_next_state else "no"
    thoughts = generate_thought(P, translator, action_description, question_atom, action, question_atom_in_state, holds_next_state, state)
    thoughts.append(f"Therefore, the answer is {answer}.")
    input = ""
    if (isinstance(question_atom, list) or  isinstance(question_atom, set) ) and len(question_atom) > 1:
        input = f"Will the following facts hold after performing the action \"{action_description}\" in the current state: {question_atom_description}?"
    else:
        input = f"Will the fact \"{question_atom_description}\" hold after performing the action \"{action_description}\" in the current state?"
    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "progression_bool",
                   "context": current_state,
                   "inputs": input,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": answer}
    return example

def generate_thought(P, translator, action_description, question_atom, action, question_atom_in_state, holds_next_state, current_state=None):

    # thoughts = []
    # current_state_desc = translator.get_atoms_description(P,current_state)
    # thoughts.append(f"At the start: {current_state_desc}.")
    
    # addeffect_description = remove_trailing_dot(translator.get_atoms_description(P, list(action.adds)))
    # deleffect_description = remove_trailing_dot(translator.get_negated_atoms_description(P, list(action.dels)))
    # # V1: After action <act_desc>, <addeffects>, further <deleffects>
    # if len(action.adds) > 0 and  len(action.dels) > 0:
    #     thoughts.append(f"After action \"{action_description}\",  {deleffect_description}. Further, {addeffect_description}.")
    # elif len(action.adds) > 0 and  len(action.dels) == 0:
    #     thoughts.append(f"After action \"{action_description}\",  {addeffect_description}.")
    # elif len(action.adds) == 0 and  len(action.dels) > 0:
    #     thoughts.append(f"After action \"{action_description}\",  {deleffect_description}.")
    # elif len(action.adds) == 0 and  len(action.dels) == 0:
    #     thoughts.append(f"Action \"{action_description}\" has no effects.") 
    

    # #V2: Action action <action_desc>, <next_state>
    # # next_state = current_state.copy()
    # # next_state = next_state - action.dels
    # # next_state = next_state.union(set(action.adds))
    # # next_state_desc = translator.get_atoms_description(P,next_state)
    # # thoughts.append(f"After action \"{action_description}\",  {next_state_desc}.")
    
    # if holds_next_state:
    #     question_atom_description = remove_trailing_dot(translator.get_atoms_description(P, question_atom))
    #     thoughts.append(f"So, {question_atom_description}.")
    #     # thoughts.append(f"Therefore, the answer is yes.")            
    # else:
    #     question_atom_description = remove_trailing_dot(translator.get_negated_atoms_description(P, question_atom))
    #     thoughts.append(f"So, {question_atom_description}.")
    #     # thoughts.append(f"Therefore, the answer is no.")            

    # return thoughts

    # V0: AAAI version 
    thoughts = []
    question_atom_description = remove_trailing_dot(translator.get_atoms_description(P, question_atom))
    if question_atom_in_state:
        thoughts.append(f"The following fact(s) hold in the current state:\n{question_atom_description}.")
        if len(action.dels) > 0:
            deleffect_description = remove_trailing_dot(translator.get_atoms_description(P, list(action.dels)))
            thoughts.append(f"The action \"{action_description}\" deletes the following fact(s):\n{deleffect_description}.")
        else:
            thoughts.append(f"The action \"{action_description}\" does not delete any facts.")
        if holds_next_state:
            thoughts.append(f"Fact(s) \"{question_atom_description}\" are not deleted.")
            # thoughts.append(f"Therefore, the answer is yes.")            
        else:
            thoughts.append(f"Fact(s) \"{question_atom_description}\" are deleted.")
            # thoughts.append(f"Therefore, the answer is no.")            
    else:
        thoughts.append(f"The following fact(s) do not hold in the current state:\n{question_atom_description}.")
        if len(action.adds) > 0:
            addeffect_description = remove_trailing_dot(translator.get_atoms_description(P, list(action.adds)))
            thoughts.append(f"The action \"{action_description}\" adds the following fact(s):\n{addeffect_description}.")
        else:
            thoughts.append(f"The action \"{action_description}\" does not add any facts.")
        if holds_next_state:
            thoughts.append(f"Fact(s) \"{question_atom_description}\" are added.")         
            # thoughts.append(f"Therefore, the answer is yes.")            
        else:
            thoughts.append(f"Fact(s) \"{question_atom_description}\" are not added.")
            # thoughts.append(f"Therefore, the answer is no.")            

    return thoughts



def generate_progression_for_problem_state_gen(P, state, action_templates, domain, example_id, random):
    action, resulting_state = random_random_applicable_action(P, state, random)
    if action is None:
        return []
    if state == resulting_state:
        return []

    examples = []
    examples.append(generate_single_progression_task_gen(P, state, action_templates, domain, example_id, random, action, resulting_state - state, state - resulting_state))
    # # Yes/No
    # target_atoms = state - resulting_state
    # if len(target_atoms) > 0:
    #     examples.append(generate_progression_task_gen(P, state, action_templates, domain, f"{example_id}_yn", random, action, target_atoms, False))

    # # No/Yes
    # target_atoms = resulting_state - state
    # if len(target_atoms) > 0:
    #     examples.append(generate_progression_task_gen(P, state, action_templates, domain, f"{example_id}_ny", random, action, target_atoms, True))

    return examples


# def generate_progression_task_gen(P, state, action_templates, domain, example_id, random, action, atoms, pos):
#     translator = get_translator(domain)()
#     current_state = translator.get_problem_description(P, state)
#     template = choose_action_templates(action_templates[domain], random)
#     action_description = get_action_description(action, template, P)
#     # question_atoms_description = [remove_trailing_dot(translator.get_atoms_description(P, atom)) for atom in atoms]
#     question_atoms_description = [f"({atom.strip()})" for atom in atoms]
    
#     lifted_atoms = get_lifted_atoms_desc(P, translator)
#     atoms_description = "The available propositions are: " + _list_to_string(lifted_atoms) + "."

#     if pos:
#         input = f"What propositions are false in the current state but will become true after performing the action \"{action_description}\"?"
#     else:
#         input = f"What propositions are true in the current state and will become false after performing the action \"{action_description}\"?"
#     example = {"id": f"{domain}_{P.problem.name}_{example_id}",
#                    "group": "progression_gen",
#                    "context": current_state + " " + atoms_description,
#                    "inputs": input,
#                    "answer": question_atoms_description}
#     return example


def generate_single_progression_task_gen(P, state, action_templates, domain, example_id, random, action, pos_atoms, neg_atoms):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    action_description = get_action_description(action, template, P)
    # question_atoms_description = [remove_trailing_dot(translator.get_atoms_description(P, atom)) for atom in atoms]
    question_atoms_description_pos = [f"({atom.strip()})" for atom in pos_atoms]
    question_atoms_description_neg = [f"({atom.strip()})" for atom in neg_atoms]
    
    lifted_atoms = get_lifted_atoms_desc(P, translator)
    atoms_description = "The available propositions are: " + _list_to_string(lifted_atoms) + "."

    thoughts = []
    if len(action.adds) == 0:
        thoughts.append(f"The action \"{action_description}\" does not make any facts true.")
    elif len(pos_atoms) == 0:
        thoughts.append(f"The facts made true by action \"{action_description}\" already hold in the state.")
    else:
        thoughts.append(f"The fact(s) {_list_to_string(question_atoms_description_pos)} do not hold in the current state and are made true by action \"{action_description}\".")
    if len(action.dels) == 0:
        thoughts.append(f"The action \"{action_description}\" does not make any facts false.")
    elif len(neg_atoms) == 0:
        thoughts.append(f"The facts made false by action \"{action_description}\" do not hold in the state.")
    else:
        thoughts.append(f"The fact(s) {_list_to_string(question_atoms_description_neg)} hold in the current state and are made false by action \"{action_description}\".")
    thoughts.append(f"Therefore, the answer is {question_atoms_description_pos}, {question_atoms_description_neg}.")

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "progression_gen",
                   "context": current_state + " " + atoms_description,
                   "inputs": f"Break down the outcomes of performing the action \"{action_description}\" into two lists, positive effects and negative effects. Positive effects are the propositions that are false in the current state but will become true after performing the action. Negative effects are the propositions that are true in the current state and will become false after performing the action.",
                   "answer": { "pos": question_atoms_description_pos, "neg": question_atoms_description_neg},
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p)           
                }
    return example