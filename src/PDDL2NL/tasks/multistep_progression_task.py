from PDDL2NL.domains import get_translator
from PDDL2NL.utils.translation_util import choose_action_templates, get_action_description, remove_trailing_dot, thoughts_list_to_string, mcq_options
from PDDL2NL.utils.tarski_utils import get_random_applicable_action, random_path, random_path_no_loops
from PDDL2NL.utils.tarskilite import fix_name, progress


def state_seq_for_path(state, actions):
    s = state
    seq = []
    seq.append(s)
    for a in actions:
        s = progress(s,a)
        seq.append(s)
    return seq

def get_yes_yes_atoms(P, state, actions, target_atoms):
    # Option 1 (preferred): a fact that is deleted in the sequence and then added
    candidate_atoms = set()
    state_seq = state_seq_for_path(state, actions)[1:-1]
    if len(state_seq) > 0:
        for i, s in reversed(list(enumerate(state_seq))):
            candidate_atoms |= target_atoms - s

    # Option 2: fact that is not deleted by any action (give preference to preconditions)
    pre_atoms = set()
    for a in actions:
        pre_atoms |= a.pres

    rest_atoms = target_atoms - candidate_atoms
    pre_atoms &= rest_atoms
    if len(pre_atoms) > 0:
        return candidate_atoms, pre_atoms  
    else:
        return candidate_atoms, rest_atoms


def get_yes_yes_action(P, state, actions, atom):
    # Option 1 (preferred): a fact that is deleted in the sequence and then added
    state_seq = state_seq_for_path(state, actions)[1:-1]
    if len(state_seq) > 0:
        for i, s in reversed(list(enumerate(state_seq))):
            if atom not in s:                
                assert(atom in actions[i+1].adds)
                return actions[i+1]


def get_last_deleting_action(P, state, actions, atom):
    # A fact is deleted in the sequence and never added

    state_seq = state_seq_for_path(state, actions)[1:-1]
    if len(state_seq) == 0:
        # There is just one action, it must be the one deleting the fact
        assert(atom in actions[0].dels)
        return actions[0]
    
    for i, s in reversed(list(enumerate(state_seq))):
        if atom in s:
            assert(atom in actions[i+1].dels)
            return actions[i+1]

    # Here, it must be Yes/No and the first action
    assert(atom in state)
    assert(atom in actions[0].dels)
    return actions[0]



def get_no_yes_action(P, state, actions, atom):
    # A fact is added in the sequence and never deleted
    state_seq = state_seq_for_path(state, actions)[1:-1]
    if len(state_seq) == 0:
        # There is just one action, it must be the one adding the fact
        assert(atom in actions[0].adds)
        return actions[0]
    
    for i, s in reversed(list(enumerate(state_seq))):
        if atom not in s:
            assert(atom in actions[i+1].adds)
            return actions[i+1]

    # It must be the first action
    assert(atom in actions[0].adds)
    return actions[0]


def get_no_no_atoms(P, state, actions, resulting_state, random):
    state_seq = state_seq_for_path(state, actions)[1:-1]
    if len(state_seq) > 0:
        atoms = state | resulting_state
        target_atomsnn = set()
        for s in state_seq:
            target_atomsnn |= s - atoms
        if len(target_atomsnn) > 0:
            return target_atomsnn, None

    target_atomsnn = set()
    for symbol in P.fluent_symbols():
        relaxed_reachable = (set([fix_name(x) for x in P.get_grounded_atoms(symbol).dump()]) - resulting_state) - state
        target_atomsnn |= relaxed_reachable
    return None, target_atomsnn



def generate_multistep_progression_for_problem_state_mcq(P, state, depth, action_templates, domain, example_id, random):
    actions, resulting_state = random_path_no_loops(P, state, random, depth=depth)
    if len(actions) == 0:
        # No applicable actions
        return []

    # We randomly choose atoms from four sets (when not empty) 
    yes_atoms = set()
    no_atoms = set()

    actions_by_atom = {}
    # Aim at getting three negative examples first.
    # Yes/No
    target_atomsyn = state - resulting_state
    if len(target_atomsyn) > 0:
        num = min(3, len(target_atomsyn))
        atoms = set(random.sample(list(target_atomsyn),k=num))
        no_atoms |= atoms
        for atom in atoms:
            actions_by_atom[atom] = get_last_deleting_action(P, state, actions, atom)

    if len(no_atoms) < 3:
        # Adding the rest from No/No
        opt1, opt2 = get_no_no_atoms(P, state, actions, resulting_state, random)
        target_atomsnn = opt1 if opt1 is not None else opt2

        num = min(3-len(no_atoms), len(target_atomsnn))
        atoms = set(random.sample(list(target_atomsnn),k=num))
        no_atoms |= atoms
        if opt1 is not None:
            for atom in atoms:
                actions_by_atom[atom] = get_last_deleting_action(P, state, actions, atom)

    if len(no_atoms) < 2:
        return []

    # Yes/Yes
    target_atoms = resulting_state & state
    if len(target_atoms) > 0:
        opt1, opt2 = get_yes_yes_atoms(P, state, actions, target_atoms)
        if len(opt1) > 0:
            atom = random.choice(list(opt1))
            actions_by_atom[atom] = get_yes_yes_action(P, state, actions, atom)
            yes_atoms.add(atom)
        elif len(opt2) > 0:
            yes_atoms.add(random.choice(list(opt2)))

    if len(yes_atoms) == 0:
        # No/Yes
        target_atomsny = resulting_state - state
        if len(target_atomsny) > 0:
            atom = random.choice(list(target_atomsny))
            actions_by_atom[atom] = get_no_yes_action(P, state, actions, atom)
            yes_atoms.add(atom)

 
    if len(yes_atoms) == 0 or len(yes_atoms | no_atoms) < 3:
        return []
    
    # print(f"Yes options {len(yes_atoms)}, No options {len(no_atoms)} (out of {len(target_atomsyn)} YN atoms and {len(target_atomsnn)} NN atoms)")
    return [generate_progression_task_mcq(P, state, actions, action_templates, domain, f"{example_id}", random, actions_by_atom, list(yes_atoms), list(no_atoms))]


def generate_multistep_progression_for_problem_state_bool(P, state, depth, action_templates, domain, example_id, random):
    actions, resulting_state = random_path_no_loops(P, state, random, depth=depth)
    if len(actions) == 0:
        # No applicable actions
        return []

    examples = []

    # Yes/Yes
    target_atoms = resulting_state & state
    if len(target_atoms) > 0:

        opt1, opt2 = get_yes_yes_atoms(P, state, actions, target_atoms)
        if len(opt1) > 0:
            question_atom = random.choice(list(opt1))
            action = get_yes_yes_action(P, state, actions, question_atom)
            examples.append(generate_progression_task_bool(P, state, actions, action_templates, domain, f"{example_id}_yy", random, action, question_atom, True))
        elif len(opt2) > 0:
            question_atom = random.choice(list(opt2))
            examples.append(generate_progression_task_bool(P, state, actions, action_templates, domain, f"{example_id}_yy", random, None, question_atom, True))

    # No/Yes
    target_atomsny = resulting_state - state
    if len(target_atomsny) > 0:
        question_atom = random.choice(list(target_atomsny))
        action = get_no_yes_action(P, state, actions, question_atom)
        examples.append(generate_progression_task_bool(P, state, actions, action_templates, domain, f"{example_id}_ny", random, action, question_atom, True))


    # Yes/No
    target_atomsyn = state - resulting_state
    if len(target_atomsyn) > 0:
        question_atom = random.choice(list(target_atomsyn))
        action = get_last_deleting_action(P, state, actions, question_atom)
        examples.append(generate_progression_task_bool(P, state, actions, action_templates, domain, f"{example_id}_yn", random, action, question_atom, False))

    # No/No
    opt1, opt2 = get_no_no_atoms(P, state, actions, resulting_state, random)
    target_atomsnn = opt1 if opt1 is not None else opt2
    question_atom = random.choice(list(target_atomsnn))
    action = get_last_deleting_action(P, state, actions, question_atom) if opt1 is not None else None
    examples.append(generate_progression_task_bool(P, state, actions, action_templates, domain, f"{example_id}_nn", random, action, question_atom, False))

    return examples


def generate_progression_task_mcq(P, state, actions, action_templates, domain, example_id, random, actions_by_atom, yes_atoms, no_atoms):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    actions_description = [remove_trailing_dot(get_action_description(action, template, P)) for action in actions]

    yes_atoms_description = [remove_trailing_dot(translator.get_atoms_description(P, atom)) for atom in yes_atoms]
    no_atoms_description = [remove_trailing_dot(translator.get_atoms_description(P, atom)) for atom in no_atoms]
    choices, options, answer_id = mcq_options(yes_atoms_description, no_atoms_description, random)

    thoughts = []
    assert(len(yes_atoms) == 1)

    # If a single atom, just return the positive thought
    question_atom_in_state = yes_atoms[0] in state
    # question_atom_description = remove_trailing_dot(translator.get_atoms_description(P, yes_atoms))
    action = actions_by_atom.get(yes_atoms[0], None)
    relevant_atoms = set(yes_atoms + no_atoms)
    thoughts = generate_thought(P, translator, actions, actions_description, relevant_atoms, yes_atoms[0], action, question_atom_in_state, True, state)
    # Add the last thought
    thoughts.append(f"Therefore, the answer is {answer_id}.")

    str_actions_description = ", ".join(actions_description)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "ms_progression_mcq",
                   "context": current_state,
                   "inputs": f"Which of the following facts hold after performing the action sequence \"{str_actions_description}\" in the current state?\n{options}",
                   "question": f"Which fact will hold after performing the action sequence \"{str_actions_description}\" in the current state?",
                   "choices": choices,
                   "targets": thoughts_list_to_string(thoughts),
                   "answer": answer_id}
    return example

def generate_progression_task_bool(P, state, actions, action_templates, domain, example_id, random, action, question_atom, holds_next_state):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    actions_description = [remove_trailing_dot(get_action_description(action, template, P)) for action in actions]

    question_atom_description = remove_trailing_dot(translator.get_atoms_description(P, question_atom))
    question_atom_in_state = question_atom in state
    answer = "yes" if holds_next_state else "no"

    relevant_atoms = set([question_atom])
    thoughts = generate_thought(P, translator, actions, actions_description, relevant_atoms, question_atom, action, question_atom_in_state, holds_next_state, state)
    thoughts.append(f"Therefore, the answer is {answer}.")
    str_actions_description = ", ".join(actions_description)

    input = ""
    if (isinstance(question_atom, list) or  isinstance(question_atom, set) ) and len(question_atom) > 1:
        input = f"Will the following facts hold after performing the action sequence \"{str_actions_description}\" in the current state: {question_atom_description}?"
    else:
        input = f"Will the fact \"{question_atom_description}\" hold after performing the action sequence \"{str_actions_description}\" in the current state?"
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "ms_progression_bool",
                   "context": current_state,
                   "inputs": input,
                   "targets": thoughts_list_to_string(thoughts),
                   "answer": answer}
    return example


def get_facts_desc(P, pos_facts, neg_facts, translator):
    result = ""
    if len(pos_facts) > 0:
        result += remove_trailing_dot(translator.get_atoms_description(P, pos_facts))
        if len(neg_facts) > 0:
            result += ", "
    if len(neg_facts) > 0:
        result += remove_trailing_dot(translator.get_negated_atoms_description(P, neg_facts))
    return result


def get_desc(P, state, atoms, translator):
    pos_state = state & atoms
    neg_state = atoms - state
    return get_facts_desc(P, list(pos_state), list(neg_state), translator)

def generate_thought(P, translator, actions, actions_description, relevant_atoms, question_atom, action, question_atom_in_state, holds_next_state, current_state=None):
    # Version 1 that does not use the action that caused the change explicitly, but the entire sequence of actions.  
    thoughts = []
    res = get_desc(P, current_state, relevant_atoms, translator)
    thoughts.append(f"At the start: {res}.")
    
    for i, a in enumerate(actions):
        action_description = actions_description[i]
        adds = list(a.adds & relevant_atoms)
        dels = list(a.dels & relevant_atoms)
        if len(adds) > 0 or len(dels) > 0:
            res = get_facts_desc(P, adds, dels, translator)
            thoughts.append(f"After action \"{action_description}\",  {res}.")
    
    res = get_desc(P, current_state, relevant_atoms, translator)
    if len(relevant_atoms) > 1:
        # MCQ
        pos_atoms = set([question_atom])
        neg_atoms = relevant_atoms - pos_atoms
    else:    
        pos_atoms = set()
        neg_atoms = set()
        if holds_next_state:
            pos_atoms.add(question_atom)
        else:
            neg_atoms.add(question_atom)
    res = get_facts_desc(P, list(pos_atoms), list(neg_atoms), translator)
    thoughts.append(f"So, {res}.")

    return thoughts

    # V0: AAAI version 
    thoughts = []
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

