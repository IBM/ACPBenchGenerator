import time
from PDDL2NL.domains import get_translator
from PDDL2NL.utils.pddl_utils import is_unsolvable_new_goal
from PDDL2NL.utils.translation_util import _list_to_string, choose_action_templates, get_action_description, get_invalid_action_templates, mcq_options, remove_trailing_dot, thoughts_list_to_string
from PDDL2NL.utils.tarski_utils import bfs, get_lifted_actions_desc, random_path, get_applicable_actions, random_path_no_loops
from PDDL2NL.utils.tarskilite import entails
from tarski.fstrips.fstrips import AddEffect # type: ignore


"""
Choosing "wrong" answers from relaxed unreachable, actions with mutex preconditions, and actions from a different problem (invalid).
Preferred option is mutex precondition, then relaxed unreachable.
Use invalid to fill up to 3. 
"""
def generate_action_reachability_for_problem_state_mcq(P, state, action_templates, domain, example_id, random):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    
    wrong_options = []
    if P.mutex_pre_actions:
        get_k = min(3, len(P.mutex_pre_actions))
        select_a = random.sample(P.mutex_pre_actions, k=get_k)
        wrong_options.extend([remove_trailing_dot(get_action_description(a[0], template, P)) for a in select_a])
        # print(f"Got {len(wrong_options)} mutex precondition actions")

    if len(wrong_options) < 3 and len(P.relaxed_unreachable_actions_groundings.keys()) > 0:
        select_a = P.get_random_unreachable_action_groundings(random, 3 - len(wrong_options))
        wrong_options.extend([remove_trailing_dot(get_action_description(a[0], template, P)) for a in select_a])
        # print(f"Got {len(select_a)} relaxed unreachable actions")

    if len(wrong_options) < 3:
        # Now adding invalid actions to fill up to 3
        get_k = min(3 - len(wrong_options), len(P.actions))
        select_a =  random.sample(list(P.actions), k=get_k )
        invalid_template = choose_action_templates(get_invalid_action_templates(domain), random)
        wrong_options.extend([remove_trailing_dot(get_action_description(a.name, invalid_template, P)) for a in select_a])
        # print(f"Got {len(select_a)} invalid actions")

    if len(wrong_options) < 2:
        # Should not happen
        return []

    thoughts = []
    actions = generate_action_reachability_for_problem_state_reachable(P, state, random)
    #     
    if actions is None or len(get_applicable_actions(P, state)) == 0:
        # sink
        # Skipping creating an example in this case
        return []
        choices, options, answer_id = mcq_options([], wrong_options, random)
        thoughts.append(f"Verify if there is a sequence of actions which transforms the current state into a state where the precondition of any of the actions hold.")
        thoughts.append("There are no such sequences of actions, for any of the options.")
    else:
        answer = remove_trailing_dot(get_action_description(actions[-1], template, P))
        choices, options, answer_id = mcq_options([answer], wrong_options, random)

        thoughts.append(f"Verify if there is a sequence of actions which transforms the current state into a state where the precondition of the action \"{answer}\" hold.")
        action_descriptions = [remove_trailing_dot(get_action_description(a, template, P)) for a in actions[:-1]]

        action_descriptions = ',\n'.join(action_descriptions)
        thoughts.append(f"The following sequence of actions would transition to such a state:\n{action_descriptions}.")
    thoughts.append(f"Therefore, the answer is {answer_id}.")
        
    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "reachable_action_mc",
                   "context": current_state,
                   "inputs": f"Which of the following actions can eventually be applied?\n{options}",
                   "question": "Which action is reachable from this state?",
                   "choices":choices,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": answer_id}
    return [example]

def generate_action_reachability_for_problem_state_bool(P, state, action_templates, domain, example_id, random):
    examples = []
    # 
    actions = generate_action_reachability_for_problem_state_reachable(P, state, random)
    if actions is not None:
        examples.append(generate_reachable_action_task_bool(P, state, actions, action_templates, domain, example_id+"_p", random))

    negative_options = []
    if len(get_applicable_actions(P, state)) == 0:
        negative_options.append("sink")
    if actions is not None:
        negative_options.append("invalid")
    if len(P.relaxed_unreachable_actions_groundings.keys()) > 0:
        negative_options.append("relaxed_unreachable")
    if P.mutex_pre_actions is not None and len(P.mutex_pre_actions) > 0:
        negative_options.append("mutex_prec")

    if len(negative_options) == 0:
        return []
    
    while True:
        # Randomly choose what negative example to generate 
        r = random.choice(negative_options)
        if r == "invalid":
            a = random.choice(actions)
            examples.append(generate_invalid_action_task_bool(P, state, a, action_templates, domain, example_id+"_n", random))            
        elif r == "mutex_prec":
            (a, mutex) = random.choice(P.mutex_pre_actions)
            examples.append(generate_mutex_precondition_action_task_bool(P, state, a, mutex, action_templates, domain, example_id+"_n", random))            
        elif r == "relaxed_unreachable":
            unreach = P.get_random_unreachable_action_groundings(random, k=1)
            if len(unreach) > 0:
                (a, upre) = unreach[0]
                # (a, upre) = random.choice(P.relaxed_unreachable_actions)
                examples.append(generate_relaxed_unreachable_action_task_bool(P, state, a, set(upre), action_templates, domain, example_id+"_n", random))            
        elif r == "sink":
            # The state is a sink, all actions are unreachable
            a = random.choice(list(P.actions))
            examples.append(generate_sink_action_task_bool(P, state, a, action_templates, domain, example_id+"_n", random))            
        break
    return examples


def generate_action_reachability_for_problem_state_reachable(P, state, random):
    # Given a state, we generate a random sequence of actions
    for i in range(10):
        depth = random.randint(3,4)
        actions, resulting_state = random_path_no_loops(P, state, random, depth=depth)
        if len(actions) > 0 and not entails(state, actions[-1].pres): 
            break
    if len(actions) == 0 or entails(state, actions[-1].pres): 
        return None
    return actions
    

def generate_action_reachability_for_problem_state_mutex_preconditions(P, state, random):
    pass


def generate_reachable_action_task_bool(P, state, actions, action_templates, domain, example_id, random):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)

    action_desc = remove_trailing_dot(get_action_description(actions[-1], template, P))
    thoughts = []
    thoughts.append(f"Verify if there is a sequence of actions which transforms the current state into a state where the precondition of the action \"{action_desc}\" hold.")
    seq_descriptions = [remove_trailing_dot(get_action_description(a, template, P)) for a in actions[:-1]]

    seq_descriptions = ',\n'.join(seq_descriptions)
    thoughts.append(f"The following sequence of actions would transition to such a state:\n{seq_descriptions}.")
    thoughts.append(f"Therefore, the answer is yes.")

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "reachable_action_bool",
                   "context": current_state,
                   "inputs": f"Is it possible to transition to a state where the action \"{action_desc}\" can be applied?",
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "yes" }
    return example

def generate_invalid_action_task_bool(P, state, action, action_templates, domain, example_id, random):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)

    invalid_template = choose_action_templates(get_invalid_action_templates(domain), random)

    action_desc = remove_trailing_dot(get_action_description(action, invalid_template, P))
    thoughts = []
    thoughts.append(f"Verify if there is a sequence of actions which transforms the current state into a state where the precondition of the action \"{action_desc}\" hold.")
    thoughts.append(f"The action is invalid in the problem and will never be applicable.")
    thoughts.append(f"Therefore, the answer is no.")

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "reachable_action_bool",
                   "context": current_state,
                   "inputs": f"Is it possible to transition to a state where the action \"{action_desc}\" can be applied?",
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "no" }
    return example

def generate_sink_action_task_bool(P, state, action, action_templates, domain, example_id, random):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)
    action_desc = remove_trailing_dot(get_action_description(action, template, P))
    thoughts = []
    thoughts.append(f"Verify if there is a sequence of actions which transforms the current state into a state where the precondition of the action \"{action_desc}\" hold.")
    thoughts.append(f"No action is applicable in the current state and thus the state can not change.")
    thoughts.append(f"Therefore, the answer is no.")

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "reachable_action_bool",
                   "context": current_state,
                   "inputs": f"Is it possible to transition to a state where the action \"{action_desc}\" can be applied?",
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "no" }
    return example

def generate_relaxed_unreachable_action_task_bool(P, state, action, upre, action_templates, domain, example_id, random):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)

    # print(f"Action {action.name} precondition: {action.pres}, unreachable preconditions: {upre}")
    partial_state_description = remove_trailing_dot(translator.get_atoms_description(P, action.pres))
    unreachable_pre = remove_trailing_dot(translator.get_atoms_description(P, upre))
    template = choose_action_templates(action_templates[domain], random)
    action_desc = remove_trailing_dot(get_action_description(action, template, P))
    thoughts = []
    thoughts.append(f"Verify if there is a sequence of actions which transforms the current state into a state where the precondition of the action \"{action_desc}\" hold.")
    thoughts.append(f"Action preconditions are \"{partial_state_description}\".") 
    thoughts.append(f"The fact(s) \"{unreachable_pre}\" are not reachable even by a simple iterative procedure that accumulates all facts made true by applicable actions.")
    thoughts.append(f"Therefore, the answer is no.")

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "reachable_action_bool",
                   "context": current_state,
                   "inputs": f"Is it possible to transition to a state where the action \"{action_desc}\" can be applied?",
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "no" }
    return example

def generate_mutex_precondition_action_task_bool(P, state, action, mutex, action_templates, domain, example_id, random):
    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)

    partial_state_description = remove_trailing_dot(translator.get_atoms_description(P, action.pres))
    mutex_description = remove_trailing_dot(translator.get_atoms_description(P, mutex))
    template = choose_action_templates(action_templates[domain], random)
    action_desc = remove_trailing_dot(get_action_description(action, template, P))
    thoughts = []
    thoughts.append(f"Verify if there is a sequence of actions which transforms the current state into a state where the precondition of the action \"{action_desc}\" hold.")
    thoughts.append(f"Action preconditions are \"{partial_state_description}\".") 
    thoughts.append(f"These facts are not reachable together, as they include mutually exclusive facts \"{mutex_description}\".")
    thoughts.append(f"Therefore, the answer is no.")

    d, p = P.PDDL_replace_init_pddl_parser(state)
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "reachable_action_bool",
                   "context": current_state,
                   "inputs": f"Is it possible to transition to a state where the action \"{action_desc}\" can be applied?",
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p),
                   "answer": "no" }
    return example


def get_unreachable_lifted_actions(P, state):
    # Go over actions, find lifted atoms not in add effects. 
    # The groundings of these atoms that can be true must be true in the state. 
    # Find actions that have preconditions on the predicate that don't hold in the state
    add_names = [ eff.atom.predicate.name for _, action in P.problem.actions.items() for eff in action.effects if isinstance(eff, AddEffect)]
    preds = [p for p in P.fluent_symbols() if p.name not in add_names]
    if len(preds) == 0:
        return []
    
    preds_names = set([f.name for f in preds])
    # print(preds_names)
    actions = []
    for a in P.actions:
        for p in a.pres:
            p_name = p.split(" ")[0]
            if p_name in preds_names and p not in state:
                actions.append((a, p))
                break
        
    return actions

def check_unreachable_planner(d, p, maybe):
    # checking one by one, stopping when found
    for a in maybe:
        goal = f'(and {" ".join([f"({atom})" for atom in a.pres])})'
        # print(f"Checking unsolvability of the composed goal {goal}")
        if is_unsolvable_new_goal(str(d), str(p), goal):
            return a
    return None


def sample_actions(actions, random, n):
    u = random.sample(list(actions), k=n) if len(actions) > n else list(actions)
    return [f"({f.name})" for f in u]

def generate_action_reachability_for_problem_state_gen(P, state, action_templates, domain, example_id, random):
    if len(get_applicable_actions(P, state)) == 0:
        # Skipping sinks
        return []
    start = time.time()

    unreachable = set()
    unreachable_relaxed_actions = set()
    unreachable_mutex_actions = set()
    unreachable_lifted_actions = set()

    reachable = bfs(P, timeout=10, actions=True)
    maybe = set(P.actions) - reachable
    total = P.get_total_num_groundings()
    # print(f"Total actions: {total}, delete relaxed reachable {len(P.action_map.keys())}, reachable by BFS: {len(reachable)}, rest: {len(maybe)}")

    # We first try to find unreachable actions among relaxed reachable
    d, p = P.PDDL_replace_init_pddl_parser(state)
    proved_unreachable = None
    if len(maybe) > 0 and len(unreachable) == 0:
        # print(f"All: {len(P.action_map.keys())}, reachable: {len(reachable)}, unreachable lifted: {len(unreachable_lifted_actions)}, unreachable relaxed: {len(unreachable_relaxed_actions)}, unreachable mutex: {len(unreachable_mutex_actions)}, rest: {len(maybe)}")
        # print(maybe)
        maybe_actions = list(maybe)
        if len(maybe_actions) > 20:
            maybe_actions = random.sample(maybe_actions, k=20)

        proved_unreachable = check_unreachable_planner(d, p, maybe_actions)
        if proved_unreachable is not None:
            # print(f'Proved unreachable: {proved_unreachable.name}')
            maybe = []
            unreachable.add(proved_unreachable)

    exec_order = ["unreachable_relaxed", "unreachable_lifted", "unreachable_mutex"]
    random.shuffle(exec_order)

    unreachable_relaxed = []
    unreachable_lifted = []
    unreachable_mutex = []
    for r in exec_order:
        # if len(maybe) == 0 or len(unreachable) > 0:
        if len(unreachable) > 0:
            break
        if r == "unreachable_relaxed":
            unreachable_relaxed_actions = set()
            if len(P.relaxed_unreachable_actions_groundings.keys()) > 0:
                action_name = random.choice(list(P.relaxed_unreachable_actions_groundings.keys()))
                grounding = random.choice(P.relaxed_unreachable_actions_groundings[action_name])
                unreachable_relaxed.append(P.get_unreachable_action(action_name, grounding))
                unreachable_relaxed_actions.add(unreachable_relaxed[-1][0])
            maybe -= unreachable_relaxed_actions
            unreachable |= unreachable_relaxed_actions
        elif r == "unreachable_lifted":
            unreachable_lifted = get_unreachable_lifted_actions(P, state)
            if len(unreachable_lifted) > 1:
                unreachable_lifted = random.sample(unreachable_lifted, k=1)
            unreachable_lifted_actions = set([a for a, _ in unreachable_lifted])            
            maybe -= unreachable_lifted_actions
            unreachable |= unreachable_lifted_actions
        elif r == "unreachable_mutex":
            unreachable_mutex_actions = set()
            if P.mutex_pre_actions is not None and len(P.mutex_pre_actions) > 0:
                unreachable_mutex = P.mutex_pre_actions
                if len(unreachable_mutex) > 1:
                    unreachable_mutex = random.sample(unreachable_mutex, k=1)
                unreachable_mutex_actions =  set([a for a, _ in unreachable_mutex])
            maybe -= unreachable_mutex_actions
            unreachable |= unreachable_mutex_actions
        

    thoughts = [f"An action can never become applicable in any potentially reachable state if its preconditions do not hold in the current state and there is no sequence of actions which transforms the current state into a state where they hold."]
    if len(unreachable) == 0:
        if len(maybe) > 0:
            # Skipping those we don't know about
            # print("Case 0")
            return []
        else:
            thoughts.append("All actions are either applicable in the current state or their preconditions are reachable by an action sequence.")
            thoughts.append("Therefore, the answer is None.")            
            # print("Case 1")
    else:
        # If proved unreachable
        if proved_unreachable is not None:
            ans = proved_unreachable
            pre = [f"({f})" for f in proved_unreachable.pres]

            thoughts.append(f"The action {ans.name.lower()} is not applicable in the current state and its preconditions {_list_to_string(pre)} are exhaustively proved unreachable.")
            # print("Case 2")
        # Only one of unreachable_lifted, unreachable_relaxed, unreachable_mutex is not empty (each of them contains at most one element)
        elif len(unreachable_relaxed) > 0:
            # unreachable_relaxed
            ans, pre = unreachable_relaxed[0]
            pre = [f"({f})" for f in pre]
            thoughts.append(f"The action ({ans.name.lower()}) is not applicable in the current state and its precondition(s) {_list_to_string(pre)} are not reachable even by a simple iterative procedure that accumulates all facts made true by applicable actions.")
            # print("Case 3")
        elif len(unreachable_lifted) > 0:
            # unreachable_lifted
            ans, pre = unreachable_lifted[0]
            pre = [f"({f})" for f in pre]
            thoughts.append(f"The action ({ans.name.lower()}) is not applicable in the current state and its precondition(s) {_list_to_string(pre)}  are not made true by any of the actions in the problem.")
            # print("Case 4")
        elif len(unreachable_mutex) > 0:
            # unreachable_mutex
            ans, pre = unreachable_mutex[0]
            pre = [f"({f})" for f in pre]
            thoughts.append(f"The action ({ans.name.lower()}) is not applicable in the current state and its preconditions include mutually exclusive facts {_list_to_string(pre)}.")
            # print("Case 5")
        thoughts.append(f"Therefore, a possible answer is ({ans.name.lower()}).")


    translator = get_translator(domain)()
    current_state = translator.get_problem_description(P, state)
    template = choose_action_templates(action_templates[domain], random)

    lifted_actions = get_lifted_actions_desc(P, template)

    actions_description = "The available actions are: " + _list_to_string(lifted_actions) + "."

    unreachable = [f"({a.name.lower()})" for a in unreachable]
    # if len(unreachable) > 0:
    #     print(f'Got unreachable actions: {unreachable}')

    # d, p = P.PDDL_replace_init(state)
    d, p = P.PDDL_replace_init_pddl_parser(state)
    print(f"{domain}_{P.problem.name}_{example_id} in {time.time()-start}s")
    example = {"id": f"{domain}_{P.problem.name}_{example_id}",
                   "group": "reachable_action_gen",
                   "context": current_state + " " + actions_description,
                   "inputs": f"What action can never become applicable, in any state reachable from the current state?",
                   "answer": unreachable,
                   "targets": thoughts_list_to_string(thoughts),
                   "PDDL_domain" : str(d),
                   "PDDL_problem" : str(p)       
            }
    return [example]
