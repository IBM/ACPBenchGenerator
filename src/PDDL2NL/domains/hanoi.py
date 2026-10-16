from PDDL2NL.utils.translation_util import ProblemTranslator, _list_to_string, _is_are
import random

class HanoiTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        return """There are three pegs and few disks of different sizes stacked on the first peg. The disks are numbered from 1
smallest to largest. Disk moves in this puzzle should follow:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one stack and placing it on top of another stack.
3. A larger disk may not be placed on top of a smaller disk. 

The goal is to move the entire stack to the third peg."""
    
    def get_objects_description(self, P):
        number_of_disks = len(P.problem.language.constants())
        return f"There are {number_of_disks-3} disks."
    
    def get_static_atoms_description(self, P, just_atoms=False):
        # TODO
        return ""
    
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        # TODO
        description = "Currently, "
        if just_atoms:
            description = "" 
        # Adding description for disks on each other.
        on_list =  [f.replace("on ", "").split() for f in state if "on " in f]
        if len(on_list) > 0:
            description += f'The disks are stacked as follows: {_list_to_string([f"{on_atom[0]} is on {on_atom[1]}" for on_atom in on_list])}. \n'
        
        #Handle clear
        clear_list =  [f.replace("clear ", "").split() for f in state if "clear " in f]
        if len(clear_list) > 0:
            description += f'Following pegs and/or disks are clear: {_list_to_string([f"{clear_atom[0]}" for clear_atom in clear_list])}.'
        
        return description
    
    def get_atom_description(self, P, grounded_atom):
        # clear/1, ontable/1, handempty/0, holding/1, on/2
        if 'clear' in grounded_atom:
            templates = ["{object} is clear.",
                    "No disk is placed on top of {object}.",
                    "{object} is not obstructed by any disk."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'on' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["{upper} is on top of {lower}.",
                "{upper} is above {lower}."]
            return random.choice(templates).format(lower=items[1], upper=items[0])
        elif 'smaller' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["{smaller} is smaller than {larger}.",
                "{larger} is larger than {smaller}."]
            return random.choice(templates).format(smaller=items[0], larger=items[1])
        else:
            raise NotImplementedError
            
    def get_negated_atom_description(self, P, grounded_atom):
        # clear/1, ontable/1, handempty/0, holding/1, on/2
        if 'clear' in grounded_atom:
            templates = ["{object} is not clear.",
                    "Some disk is placed on top of {object}.",
                    "{object} is obstructed by some disk."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'on' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["{upper} is on not on {lower}.",
                "{upper} is not situated above {lower}."]
            return random.choice(templates).format(lower=items[1], upper=items[0])
        else:
            raise NotImplementedError
            
class RandomHanoiTranslator(HanoiTranslator):
    
        
    def get_domain_description(self):
        return """There are three pegs and few disks of different sizes stacked on these pegs. The disks are numbered from 1
smallest to largest. Disk moves in this puzzle should follow:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one stack and placing it on top of another stack.
3. A larger disk may not be placed on top of a smaller disk. 

The goal is to move the disks to specific stacks."""
    
    def get_objects_description(self, P):
        number_of_disks = len(P.problem.language.constants())
        return f"There are {number_of_disks-3} disks."