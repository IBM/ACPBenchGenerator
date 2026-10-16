from abc import ABC, abstractmethod
import itertools
import os
import json

def _num_obj_str(name, objects):
    import inflect
    plural = inflect.engine().plural(name)
    return f'{len(objects[name])} {(plural if len(objects[name]) > 1 else name)}'

def _is_are(i):
    if isinstance(i, list):
        return "are" if len(i) > 1 else "is"
    elif isinstance(i, int):
        return "are" if i > 1 else "is"

def _list_to_string(arr, or_delim=False):
    if len(arr) == 0:
        return ""
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] + (" or " if or_delim else " and ") + arr[1]
    return ", ".join(arr[:-1]) + (", or " if or_delim else ", and ") + arr[-1]

def thoughts_list_to_string(thoughts):
    assert(len(thoughts)>0)
    counter = 1
    res = ""
    for thought in thoughts:
        res += f"Step {counter}:\n{thought}\n"
        counter += 1
    # Removing the last "\n"
    return res[:-1]

def remove_trailing_dot(name):
    if len(name)  > 0:
        fixed_name = name.rstrip()
        if fixed_name[-1] == ".":
            return fixed_name[:-1]
    return name

def _nth(occurrence):
    d = {1: "1st", 2: "2nd", 3: "3rd"}
    if occurrence in d:
        return d[occurrence]
    return f'{str(occurrence)}th'

def _get_predicate(grounded_atom):
    return grounded_atom.split()[0]

class ProblemTranslator(ABC):
    
    @abstractmethod
    def get_domain_description(self):
        pass
    
    # @abstractmethod
    def get_domain_goal_description(self):
        pass
    
    # @abstractmethod
    def get_problem_goal_description(self, P, goal):
        return "The goal is to reach a state where the following facts hold: "+ self.get_atoms_description(P, list(goal)) + "."
    
    @abstractmethod
    def get_objects_description(self, P):
        pass
    
    @abstractmethod
    def get_static_atoms_description(self, P, just_atoms=False):
        pass
    
    @abstractmethod
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        pass
    
    def get_state_description(self, P, state):
        return self.get_fluent_atoms_description(P, state)
    
    def get_problem_description(self, P, state):
        description = ""
        init = self.get_domain_description() 
        if len(init) > 0:
            description += init + " \n"
        obj_desc = self.get_objects_description(P) 
        if len(obj_desc) > 0:
            description += obj_desc + " \n"
        static_desc = self.get_static_atoms_description(P) 
        if len(static_desc) > 0:
            description += static_desc + " \n"
        fluent_desc = self.get_fluent_atoms_description(P, state) 
        if len(fluent_desc) > 0:
            description += fluent_desc + " \n"
        if len(description) > 1:
            return description[:-2]
        return description  
    
    def get_atoms_description(self, P, grounded_atoms):
        if isinstance(grounded_atoms, list) or isinstance(grounded_atoms,set):
            descriptions = []
            for atom in grounded_atoms:
                des = self.get_atom_description(P, atom).strip() 
                if des.endswith("."):
                    des = des[:-1].strip()
                descriptions.append(des)
            return _list_to_string(descriptions)
        else:
            des = self.get_atom_description(P, grounded_atoms) 
            if des.endswith("."):
                des = des[:-1].strip()
            return des

    # @abstractmethod
    def get_atom_description(self, P, grounded_atom):
        return self.get_fluent_atoms_description(P, [grounded_atom], just_atoms=True) 
    
    def get_negated_atoms_description(self, P, grounded_atoms):
        if isinstance(grounded_atoms, list) or isinstance(grounded_atoms,set):
            descriptions = []
            for atom in grounded_atoms:
                des = self.get_negated_atom_description(P, atom).strip() 
                if des.endswith("."):
                    des = des[:-1].strip()
                descriptions.append(des)
            return _list_to_string(descriptions)
        else:
            des = self.get_negated_atom_description(P, grounded_atoms) 
            if des.endswith("."):
                des = des[:-1].strip()
            return des
        
    def get_negated_atom_description(self, P, grounded_atom):
        atom_desc = self.get_atom_description(P,grounded_atom)
        return f"Following facts do not hold: {atom_desc}"


def get_action_description_rnd(action, action_templates, P, random):
    if isinstance(action, str):
        temp = action.split()
    else:
        temp = action.name.split()
    action_name = temp[0]
    parameters = temp[1:]
    template = random.choice(action_templates[action_name.lower()])
    vars = [i for (i,j) in P.problem.actions[action_name].parameters.variables.items()]
    vars = sorted(enumerate(vars), key=lambda x : len(x[1]), reverse=True) 
    for k, i in vars:
        template = template.replace(f"{i}",parameters[k])
    return template.replace("{","").replace("}","").strip()

def get_action_description(action, action_templates, P):
    if isinstance(action, str):
        temp = action.split()
    else:
        temp = action.name.split()
    action_name = temp[0]
    parameters = temp[1:]
    template = action_templates[action_name.lower()]
    vars = [i for (i,j) in P.problem.actions[action_name].parameters.variables.items()]
    vars = sorted(enumerate(vars), key=lambda x : len(x[1]), reverse=True) 
    for k, i in vars:
        template = template.replace(f"{i}",parameters[k])
    return template.replace("{","").replace("}","").strip()

def get_pddl_domain(domain):
    return open(get_pddl_domain_file(domain),'r').read()

def get_pddl_domain_file(domain):
    dirname = os.path.dirname(__file__)
    return f'{dirname}/../../../benchmarks/{domain}/domain.pddl'


def get_invalid_action_templates(domain):
    dirname = os.path.dirname(__file__)
    templates = json.load(open(f'{dirname}/../../../benchmarks/invalid_action_templates.json','r'))
    return templates[domain]

def choose_action_templates(action_templates, random):
    ret = {}
    for action_name, val in action_templates.items():
        ret[action_name] = random.choice(val)
    return ret

def mcq_options(correct_options : list, incorrect_options : list, random):
    # Making four possible answers to choose from
    options = correct_options + incorrect_options
    # Rewritten to remove the "None of the above" option
    if len(correct_options) != 1 or len(incorrect_options) != 3:
        # Add options
        for i,j in itertools.combinations(range(len(options)), 2):
            options.append(_list_to_string([f"{options[i]}", f"{options[j]}"]))

    # Randomly choosing an option among correct_answers 
    correct_answers = set([_list_to_string(correct_options)]) | set(correct_options)
    correct_answer = random.choice(list(correct_answers))
    wrong_answers = [x for x in options if x not in correct_answers]
    assert len(wrong_answers) >= 3, f"Wrong number of wrong options: {wrong_answers}, the correct options are {correct_options} and incorrect ones are {incorrect_options}" 

    options = [correct_answer] + random.sample(wrong_answers, k=3)
    random.shuffle(options)

    option_ids=["A","B","C","D"]
    answer_id = f"{option_ids[options.index(correct_answer)]}"
    choices = {"text": options,"label": option_ids}
    options_with_labels = " \n".join([ f"{i}. {j}." for i, j in zip(option_ids, options)])
    return choices, options_with_labels, answer_id    
    
    