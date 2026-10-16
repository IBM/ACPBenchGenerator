import time
from PDDL2NL.domains import get_translator
from PDDL2NL.utils.pddl_utils import is_unsolvable_new_goal
from PDDL2NL.utils.translation_util import _list_to_string, choose_action_templates, get_action_description, get_pddl_domain, mcq_options, remove_trailing_dot, thoughts_list_to_string
from PDDL2NL.utils.tarski_utils import bfs, get_applicable_actions, get_lifted_atoms_desc, random_path
from PDDL2NL import utils as ut
from PDDL2NL.utils.tarskilite import entails, fix_name, parse_lmg_variables
import itertools
from tarski.fstrips.fstrips import AddEffect # type: ignore
from tarski.grounding.common import StateVariableLite # type: ignore
# from PDDL2NL.utils.cpddl_util import get_LMGs_with_counting_variables
import re

"""
Non reachable atom reason_code : 
1: 'lifted_atom_not_in_add_effect', single_atom
2: 'mutex', two_atoms
3: 'not_delete_relaxed_reachable', single_atom
other

"""
def generate_reachability_for_problem_state_mcq(P, state, action_templates, domain, example_id, random, plan_depth=2):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    
    unreachable_partial_state_descriptions = []
    # Returns up to three options
    partial_states_lifted = generate_reachability_for_problem_state_unreachable_lifted(P, state, action_templates, domain, example_id, random)
    partial_states_relaxed  =  generate_reachability_for_problem_state_unreachable_relaxed(P, state, action_templates, domain, example_id, random)
    while len(unreachable_partial_state_descriptions) < 3:
        # remove_trailing_dot(translator.get_atoms_description(P, partial_state))
        if partial_states_lifted is not None and len(partial_states_lifted)>0:
            partial_state, _, _, _ = partial_states_lifted[0]
            del partial_states_lifted[0]
            unreachable_partial_state_descriptions.append(remove_trailing_dot(translator.get_atoms_description(P, partial_state)))

        if len(unreachable_partial_state_descriptions) == 3:
            break
        if partial_states_relaxed is not None and len(partial_states_relaxed)>0:
            partial_state, _, _, _ = partial_states_relaxed[0]
            del partial_states_relaxed[0]
            unreachable_partial_state_descriptions.append(remove_trailing_dot(translator.get_atoms_description(P, partial_state)))

        if len(unreachable_partial_state_descriptions) == 3:
            break
        # generating on demand 
        partial_state_mutex, _, _, _  =  generate_reachability_for_problem_state_unreachable_mutex(P, state, action_templates, domain, example_id, random)
        if partial_state_mutex is not None:
            unreachable_partial_state_descriptions.append(remove_trailing_dot(translator.get_atoms_description(P, partial_state_mutex)))

    reachable_partial_state, is_reachable, actions, reason_code_and_atom  =  generate_reachability_for_problem_state_reachable(P, state, action_templates, domain, example_id, random, plan_depth=plan_depth)
    if reachable_partial_state is None:
        # Not creating an option in this case
        return []
        choices, options, answer_id = mcq_options([], unreachable_partial_state_descriptions, random)
    else:
        reachable_partial_state_description = remove_trailing_dot(translator.get_atoms_description(P, reachable_partial_state))
        choices, options, answer_id = mcq_options([reachable_partial_state_description], unreachable_partial_state_descriptions, random)
    # print(options)
    thoughts = []
    if reachable_partial_state is None:
        thoughts.append(f"Verify if there is a sequence of actions which transforms the current state into a state where any of the facts holds.")
        thoughts.append(f"There are no such sequences.")
    else:
        if len(reachable_partial_state) > 1:
            thoughts.append(f"Verify if the following facts hold in the current state: \n{reachable_partial_state_description}.")
            thoughts.append(f"These facts do not hold.")
            thoughts.append(f"Verify if there is a sequence of actions which transforms the current state into a state where these facts hold.")
        else:
            thoughts.append(f"Verify if the following fact holds in the current state: \n{reachable_partial_state_description}.")
            thoughts.append(f"The fact does not hold.")
            thoughts.append(f"Verify if there is a sequence of actions which transforms the current state into a state where the fact holds.")
        template = choose_action_templates(action_templates[domain], random)
        action_descriptions = [remove_trailing_dot(get_action_description(a, template, P)) for a in actions]

        action_descriptions = ',\n'.join(action_descriptions)
        thoughts.append(f"The following sequence of actions would transition to such a state:\n{action_descriptions}.")
    thoughts.append(f"Therefore, the answer is {answer_id}.")
        
    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "reachable_atom_mc",
                   "context": current_state,
                   "inputs": f"Which of the following options can hold in a state that can potentially be reached?\n{options}",
                   "question": "Which fact is reachable from this state?",
                   "choices":choices,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": answer_id}
    return [example]

def generate_reachability_for_problem_state_bool(P, state, action_templates, domain, example_id, random, plan_depth=2):
    examples = []
    # 
    partial_state, is_reachable, actions, reason_code_and_atom  =  generate_reachability_for_problem_state_reachable(P, state, action_templates, domain, example_id, random, plan_depth)
    if partial_state is not None:
        examples.append(generate_reachable_atom_task(P, state, action_templates, domain, example_id+"_p", partial_state, is_reachable, actions, random, reason_code_and_atom))
    
    negative_examples = []
    partial_states = generate_reachability_for_problem_state_unreachable_lifted(P, state, action_templates, domain, example_id, random)
    if partial_states is not None and len(partial_states)>0:
        negative_examples.append(partial_states[0])
    
    partial_state, is_reachable, actions, reason_code_and_atom  =  generate_reachability_for_problem_state_unreachable_mutex(P, state, action_templates, domain, example_id, random)
    if partial_state is not None:
        negative_examples.append((partial_state, is_reachable, actions, reason_code_and_atom))
    
    partial_states = generate_reachability_for_problem_state_unreachable_relaxed(P, state, action_templates, domain, example_id, random)
    if partial_states is not None and len(partial_states)>0:
        negative_examples.append(partial_states[0])
    
    if len(negative_examples) > 0:
        partial_state, is_reachable, actions, reason_code_and_atom   = random.choice(negative_examples)
        examples.append(generate_reachable_atom_task(P, state, action_templates, domain, example_id+"_n", partial_state, is_reachable, actions, random, reason_code_and_atom))
    return examples


def generate_reachability_for_problem_state_reachable(P, state, action_templates, domain, example_id, random, plan_depth=2, timeout=30):
    if plan_depth == 0:
        # Return original problem.
        P, plans = ut.tlu.get_task_plans(P.domain_file, P.problem_file, 1, timeout=timeout)
        if len(plans) > 0:
            return P.goal, True, plans[0], None 
        return P.goal, False, None, ('4', P.goal) 
    
    # Given a state, we generate a random sequence of actions, get the resulting state. [partial_state - a subset of (resulting state - state), new atom]
    for i in range(10):
        actions, resulting_state = random_path(P, state, random, depth=plan_depth)
        partial_state = resulting_state - state
        if len(partial_state) > 0:
            break
    if len(partial_state) == 0:
        return None, None, None, None
    if len(partial_state) > 1:
        partial_state = set(random.sample(list(partial_state), k=2))
    return partial_state, True, actions, None
    # return [generate_reachable_atom_task(P, state, action_templates, domain, example_id, partial_state, True, actions, random, None)]
    

def get_unreachable_lifted(P, state):
    # Go over actions, find lifted atoms not in add effects. Find those groundings that don't hold in the state
    add_names = [ eff.atom.predicate.name for _, action in P.problem.actions.items() for eff in action.effects if isinstance(eff, AddEffect)]
    preds = [p for p in P.fluent_symbols() if p.name not in add_names]
    if len(preds) == 0:
        return []
    
    all_groundings = [fix_name(str(StateVariableLite(symbol, binding).to_atom())) for symbol in preds for binding in itertools.product(*[s.domain() for s in symbol.domain])]
    missing_groundings = set(all_groundings) - state
    return list(missing_groundings)


def generate_reachability_for_problem_state_unreachable_lifted(P, state, action_templates, domain, example_id, random):
    # Go over actions, find lifted atoms not in add effects. Find those groundings that don't hold in the state
    add_names = [ eff.atom.predicate.name for _, action in P.problem.actions.items() for eff in action.effects if isinstance(eff, AddEffect)]
    preds = [p for p in P.fluent_symbols() if p.name not in add_names]
    if len(preds) == 0:
        return None
    
    all_groundings = [fix_name(str(StateVariableLite(symbol, binding).to_atom())) for symbol in preds for binding in itertools.product(*[s.domain() for s in symbol.domain])]
    missing_groundings = set(all_groundings) - state
    if len(missing_groundings) == 0:
        return None

    partial_states = []
    chosen_atoms = set()
    for i in range(3):
        atom = set()
        choose_from = list(missing_groundings - chosen_atoms)
        if len(choose_from) == 0:
            break
        atom.add(random.choice(choose_from))
        chosen_atoms |= atom
        reason_code_and_atom = (1, atom)
        partial_state = atom.copy()
        if random.random() < 0.5:
            partial_state.add(random.choice(list(state)))
        partial_states.append((partial_state,False, None, reason_code_and_atom))        
    return partial_states
    # return [generate_reachable_atom_task(P, state, action_templates, domain, example_id, partial_state, False, None, random, reason_code_and_atom)]
    


def generate_reachability_for_problem_state_unreachable_mutex(P, state, action_templates, domain, example_id, random):
    fluent_symbols_list = [ i.name for i in P.fluent_symbols()] 
    # Find Lifted Mutex Groups
    # lmgs = get_LMGs_with_counting_variables(P.domain_file, P.problem_file)
    lmgs = P.lmgs
    if len(lmgs) == 0:
        return None, None, None, None 
    
    # Chose two atoms from a LMG at random such that atleast one has a counting variable 
    partial_state_obtained = False
    while_count = 5
    while not partial_state_obtained and while_count > 0:
        while_count = while_count -1 
        

        lmg = random.choice(lmgs)
        counting_variables,fixed_variables, all_variables = parse_lmg_variables(lmg)
    
        # Select one with counted variable 
        regexp = re.compile(r'C.:')
        atom_idx1 = random.choice([ i for i, lifted_atom in enumerate(lmg) if regexp.search(" ".join(lifted_atom)) ])

        # Select any
        atom_idx2 = random.choice(range(len(lmg)))

        # Chose a grounded atom 
        grounded_atoms = list(P.get_grounded_atoms(P.fluent_symbols()[fluent_symbols_list.index(lmg[atom_idx1][0])]).__iter__())
        if len(grounded_atoms) == 0:
            return None, None, None, None 
        first_grounded_atom = grounded_atoms[random.choice(range(len(grounded_atoms)))]

        # parse variables and assign binding identified w.r.t  1st atom    
        bindings = {}
        for i, binding in enumerate(first_grounded_atom.binding):
            if (atom_idx1, i) in fixed_variables:
                bindings[fixed_variables[(atom_idx1, i)]] = binding
            elif (atom_idx1, i) in counting_variables:
                bindings[counting_variables[(atom_idx1, i)]] = binding
        for k, v in fixed_variables.items():
            if not ":" in v:
                bindings[v] = [ i  for i in P.problem.language.constants() if i.name == v ][0]
                
        # Filter choices for second grounded atom based on bindings
        if lmg[atom_idx2][0] == lmg[atom_idx1][0]:
            grounded_atoms.remove(first_grounded_atom)
        else:
            grounded_atoms = list(P.get_grounded_atoms(P.fluent_symbols()[fluent_symbols_list.index(lmg[atom_idx2][0])]).__iter__())
        valid_mutexes = []
        for ga in grounded_atoms:
            valid = True 
            for i, variable in enumerate(lmg[atom_idx2][1:]):
                if (atom_idx2,i) in fixed_variables and fixed_variables[(atom_idx2,i)] in bindings and ga.binding[i].name != bindings[fixed_variables[(atom_idx2,i)]].name:
                    valid = False
                    break 
            if valid:
                valid_mutexes.append(ga)
        if len(valid_mutexes) == 0:
            # print("No Valid Mutexes")
            continue
        # Randomly select a second atom
        second_grounded_atom = random.choice(valid_mutexes)
        partial_state_obtained = True
    
    if not partial_state_obtained:
        print("lmg", lmg)
        return None, None, None, None 
    partial_state = [str(first_grounded_atom).replace("("," ").replace(","," ").replace(")",""),  str(second_grounded_atom).replace("("," ").replace(","," ").replace(")","")]
    reason_code_and_atom = (2, partial_state)
    return partial_state, False, None, reason_code_and_atom
    # return [generate_reachable_atom_task(P, state, action_templates, domain, example_id, partial_state, False, None, random, reason_code_and_atom)]
    

def get_unreachable_relaxed(P, state):
    # Find relaxed unreachable atoms, choose one
    all_unreachable = []
    for symbol in P.fluent_symbols():
        all_groundings = [fix_name(str(StateVariableLite(symbol, binding).to_atom()))  for binding in itertools.product(*[s.domain() for s in symbol.domain])]
        relaxed_reachable = [fix_name(x) for x in P.get_grounded_atoms(symbol).dump()]
        relaxed_unreachable = set(all_groundings) - set(relaxed_reachable)
        if len(relaxed_unreachable) > 0:
            all_unreachable.extend(list(relaxed_unreachable))

    return all_unreachable

def generate_reachability_for_problem_state_unreachable_relaxed(P, state, action_templates, domain, example_id, random):
    # Find relaxed unreachable atoms, choose one
    all_unreachable = {}
    for symbol in P.fluent_symbols():
        all_groundings = [fix_name(str(StateVariableLite(symbol, binding).to_atom()))  for binding in itertools.product(*[s.domain() for s in symbol.domain])]
        relaxed_reachable = [fix_name(x) for x in P.get_grounded_atoms(symbol).dump()]
        relaxed_unreachable = set(all_groundings) - set(relaxed_reachable)
        if len(relaxed_unreachable) > 0:
            all_unreachable[symbol] = relaxed_unreachable

    if len(all_unreachable.keys()) == 0:
        return None
    
    partial_states = []
    chosen_atoms = set()
    for i in range(3):
        symbol = random.choice(list(all_unreachable.keys()))
        atoms = set()
        choose_from = list(all_unreachable[symbol] - chosen_atoms)
        if len(choose_from) == 0:
            break
        atoms.add(random.choice(choose_from))                     
        chosen_atoms |= atoms
        reason_code_and_atom = (3, atoms)
        partial_state = atoms.copy()
        if random.random() < 0.5:
            partial_state.add(random.choice(list(state)))
        partial_states.append((partial_state,False, None, reason_code_and_atom))        
        
    return partial_states
    # return [generate_reachable_atom_task(P, state, action_templates, domain, example_id, partial_state, False, None, random, reason_code_and_atom)]
    

def generate_reachable_atom_task(P, state, action_templates, domain, example_id, partial_state, is_reachable, actions, random, reason_code_and_atom):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    # Regressively select an applicable action for answer 
    partial_state_description = remove_trailing_dot(translator.get_atoms_description(P, partial_state))
    thoughts = [f"Verify if the following fact(s) hold in current state or if there is a sequence of actions which transforms the current state into a state where they hold:\n{partial_state_description}."]
    if is_reachable:
        template = choose_action_templates(action_templates[domain], random)
        action_descriptions = ',\n'.join([remove_trailing_dot(get_action_description(a, template, P)) for a in actions ])
        
        thoughts.append(f"The following sequence of actions would transition to such a state:\n{action_descriptions}.")
        thoughts.append("Therefore, the answer is yes.")
    else:
        reason_atom_description = remove_trailing_dot(translator.get_atoms_description(P, reason_code_and_atom[1]))
        thoughts.append("These facts do not hold in the current state.")
        if reason_code_and_atom[0] ==  1:
            thoughts.append(f"The fact {reason_atom_description} is not made true by any of the actions in the problem.")
        elif reason_code_and_atom[0] ==  2:   
            thoughts.append(f"These facts are mutually exclusive:\n{reason_atom_description}. Therefore, they cannot hold together in any reachable state.")
        elif reason_code_and_atom[0] ==  3:   
            thoughts.append(f"The fact {reason_atom_description} is not reachable even by a simple iterative procedure that accumulates all facts made true by applicable actions.")
        else:
            thoughts.append(f"There is no sequence of actions that would transition the current state to such a state.")
        thoughts.append("Therefore, the answer is no.")
        
    d, p = P.PDDL_replace_init_pddl_parser(state, set(partial_state))
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "reachable_atom_bool",
                   "context": current_state,
                   "inputs": f"Is it possible to transition to a state where the following holds: \n{partial_state_description}?",
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "yes" if is_reachable else "no",
                   "sample_plan": [ a.name for a in actions] if is_reachable else "",
                   "n_objects": len(p.objects),
                   "n_facts": len(state),
                   "plan_length": len(actions) if is_reachable else None
                   }
    
    # objects, #facts in state, plan, plan-length, initial-problem file, pddl-init-state, increase plan-length. 
    return example

def check_unreachable_planner_slice(d, p, maybe):
    # If maybe is larger than 100, check by slices of 100
    chnk_size = 1
    if len(maybe) > chnk_size:
        for i in range(0, len(maybe), chnk_size):
            unreach = check_unreachable_planner_slice(d, p, maybe[i:i + chnk_size])
            if len(unreach) > 0:
                return unreach
                    

    if len(maybe) == 0:
        return []
    if len(maybe) > 1:
        maybe_goal = f'(or {" ".join([f"({atom})" for atom in maybe])})'
    else:
        maybe_goal = f'({maybe[0]})'

    # print(f"Checking unsolvability of the composed goal {maybe_goal}")
    if is_unsolvable_new_goal(str(d), str(p), maybe_goal):
        return maybe
    if len(maybe) <= 1:
        return []
    # splitting and checking
    l = len(maybe) // 2
    unreach = check_unreachable_planner_slice(d, p, maybe[:l])
    if len(unreach) > 0:
        return unreach
    unreach = check_unreachable_planner_slice(d, p, maybe[l:])
    if len(unreach) > 0:
        return unreach
    return []

def check_unreachable_planner_serial(d, p, maybe):
    for atom in maybe:
        maybe_goal = f'({atom})'
        if is_unsolvable_new_goal(str(d), str(p), maybe_goal):
            return [atom]

    return []

def sample_atoms(atoms, random, n):
    u = random.sample(list(atoms), k=n) if len(atoms) > n else atoms
    return [f"({f})" for f in u]

def generate_reachability_for_problem_state_gen(P, state, action_templates, domain, example_id, random, plan_depth=2):
    start = time.time()
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)

    unreachable_lifted = set(get_unreachable_lifted(P, state))
    unreachable_relaxed = set(get_unreachable_relaxed(P, state))

    d, p = P.PDDL_replace_init_pddl_parser(state)
    reachable = bfs(P, timeout=5)
    maybe = P.fluents - reachable - unreachable_lifted - unreachable_relaxed
    unreachable = list(unreachable_lifted | unreachable_relaxed)
    proved_unreachable = []
    # If there are no unreachable, but there are maybe, we can test those separately
    if len(maybe) > 0 and len(unreachable) == 0:
        # Check all together. If unsolvable, then none of them are reachable. 
        # proved_unreachable = check_unreachable_planner_slice(d, p, list(maybe))
        maybe = list(maybe)
        if len(maybe) > 20:
            maybe = random.sample(maybe, k=20)
        maybe.sort()
        proved_unreachable = check_unreachable_planner_serial(d, p, maybe)
        if len(proved_unreachable) > 0:
            unreachable.extend(proved_unreachable)
            maybe = []

        # print(f"Reachable: {len(reachable)}, unreachable: {len(unreachable)}, Unknown whether reachable: {len(maybe)}")
        # if len(maybe) > 0:
        #     print(maybe)

    if len(unreachable) > 50:
        unreachable = random.sample(unreachable, k=50)

    lifted_atoms = get_lifted_atoms_desc(P, translator)
    atoms_description = "The available propositions are: " + _list_to_string(lifted_atoms) + "."

    thoughts = [f"A proposition can never hold in any potentially reachable state if it does not hold in the current state and there is no sequence of actions which transforms the current state into a state where it holds."]
    if len(unreachable) == 0:
        if len(maybe) > 0:
            # Skipping those we don't know about
            # print("Case 0")
            return []
        else:
            thoughts.append("All propositions either hold in the current state or reachable by an action sequence.")
            thoughts.append("Therefore, the answer is None.")            
            # print("Case 1")
    else:
        # If proved unreachable
        if len(proved_unreachable) > 0:
            u = sample_atoms(proved_unreachable, random, 5)
            thoughts.append(f"The proposition(s) {_list_to_string(u)} do not hold in the current state and are exhaustively proved unreachable.")
            # print("Case 2")
        # If both unreachable_lifted and unreachable_relaxed not empty, choose one randomly 
        elif len(unreachable_lifted) > 0 and (len(unreachable_relaxed) == 0 or random.random() < 0.5):
            # unreachable_lifted
            u = sample_atoms(unreachable_lifted, random, 5)
            thoughts.append(f"The proposition(s) {_list_to_string(u)} do not hold in the current state and are not made true by any of the actions in the problem.")
            # print("Case 3")
        else:
            # unreachable_relaxed
            u = sample_atoms(unreachable_relaxed, random, 5)
            thoughts.append(f"The proposition(s) {_list_to_string(u)} are not reachable even by a simple iterative procedure that accumulates all facts made true by applicable actions.")
            # print("Case 4")
        thoughts.append(f"Therefore, possible answers are {_list_to_string(u, or_delim=True)}.")

    # d, p = P.PDDL_replace_init(state)
    # if "notvalidated" in str(p):
    #     print("notvalidated exists")
    # else:
    #     print("NOT THERE")
    print(f"{domain}_{P.problem.name}_{example_id} in {time.time()-start}s")
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "reachable_atom_gen",
                   "context": current_state + " " + atoms_description,
                   "inputs": "What proposition can never hold in any potentially reachable state?",
                   "answer": unreachable,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p)               
            }
    return [example]
