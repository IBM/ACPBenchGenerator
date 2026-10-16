from PDDL2NL.utils.translation_util import ProblemTranslator, _list_to_string, _is_are
import random

class FrogsJumpingTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        return """Jumping frogs puzzle where two groups of frogs face each other on a line of lily pads. Frogs on the left can only move right; frogs on the right can only move left. A frog may slide onto the immediately adjacent empty pad or jump over exactly one frog onto an empty pad two spaces away. The pads are numbered from 1
left to right. The puzzle is solved when the two groups of frogs swap positions."""
    
    def get_objects_description(self, P):
        right_frogs = P.problem.language.get_sort('rightfrog')
        return f"There are {right_frogs.cardinality()} frogs on each side."
    
    def get_static_atoms_description(self, P, just_atoms=False):
        # TODO
        return ""
    
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        # TODO
        description = "Currently, "
        if just_atoms:
            description = "" 
        # Adding description for each frog.
        at_list =  [f.replace("at ", "").split() for f in state if "at " in f]
        if len(at_list) > 0:
            description += f'The frogs are located as follows: {_list_to_string([f"{at_atom[0]} is at {at_atom[1]}" for at_atom in at_list])}. \n'
        
        #Handle empty
        empty_list =  [f.replace("empty ", "").split() for f in state if "empty " in f]
        if len(empty_list) > 0:
            assert len(empty_list) == 1
            description += f'The lily pad {empty_list[0][0]} is empty.'
        
        return description
    
    def get_atom_description(self, P, grounded_atom):
        # clear/1, ontable/1, handempty/0, holding/1, on/2
        if 'empty' in grounded_atom:
            templates = ["{object} is empty.",
                    "No frog is at lily pad {object}.",
                    "{object} is not occupied by any frog."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'at' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["{upper} is on top of {lower}.",
                "{upper} is above {lower}."]
            return random.choice(templates).format(lower=items[1], upper=items[0])
        else:
            raise NotImplementedError
            
    def get_negated_atom_description(self, P, grounded_atom):
        # clear/1, ontable/1, handempty/0, holding/1, on/2
        if 'empty' in grounded_atom:
            templates = ["{object} is not empty.",
                    "Some frog is at pad {object}.",
                    "{object} is obstructed by some frog."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'on' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["{upper} is on not on {lower}.",
                "{upper} is not situated above {lower}."]
            return random.choice(templates).format(lower=items[1], upper=items[0])
        else:
            raise NotImplementedError

    
        
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