from PDDL2NL.utils.translation_util import ProblemTranslator, _list_to_string, _is_are
import random

class BlocksWorldTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        return "This is a blocksworld domain where blocks can be placed on top of each other or on the table. There is one robotic arm that can move the block."
    
    def get_objects_description(self, P):
        number_of_blocks = len(P.problem.language.constants())
        return f"There are {number_of_blocks} blocks."
    
    def get_static_atoms_description(self, P, just_atoms=False):
        return ""
    
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        description = "Currently, "
        if just_atoms:
            description = "" 
        handempty = "handempty " in state
        # Adding status of the robotic arm
        if handempty:
            description += f"the robotic arm is empty. "
        else:
            holding = [f for f in state if "holding " in f]
            # ['holding block_24']
            if len(holding) > 0:
                block_number = holding[0].replace("holding ", "")
                description += f"the robotic arm is holding {block_number}. "
        # Adding description for blocks that are on the table
        ontable_list = [f.replace("ontable ", "") for f in state if "ontable " in f]
        
        if len(ontable_list) > 0:
            description += f"The following block(s) {_is_are(ontable_list)} on the table: {_list_to_string(ontable_list)}." 
        # Adding description for blocks on each other.
        on_list =  [f.replace("on ", "").split() for f in state if "on " in f]
        if len(on_list) > 0:
            description += f' The following block(s) {_is_are(on_list)} stacked on top of another block: {_list_to_string([f"{on_atom[0]} is on {on_atom[1]}" for on_atom in on_list])}.'
        
        #Handle clear
        if just_atoms:
            clear_list =  [f.replace("clear ", "").split() for f in state if "clear " in f]
            if len(clear_list) > 0:
                description += f' No block {_is_are(clear_list)} placed on top of the following block(s): {_list_to_string([f"{clear_atom[0]}" for clear_atom in clear_list])}.'
        
        return description
    
    def get_atom_description(self, P, grounded_atom):
        # clear/1, ontable/1, handempty/0, holding/1, on/2
        if 'clear' in grounded_atom:
            templates = ["Block {object} is clear.",
                    "No blocks are placed on top of {object}.",
                    "{object} is not obstructed by any other blocks."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'ontable' in grounded_atom:
            templates = ["Block {object} is on the table.",
                    "Block {object} is placed on the table.",
                    "Block {object} is located on the table."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'handempty' in grounded_atom:
            templates = ["The robotic arm is empty.",
                "The robotic arm is not holding anything."]
            return random.choice(templates)
        elif 'holding' in grounded_atom:
            templates = ["The robotic arm is holding {object}.",
                "The block {object} is currently being held by the robotic arm."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'on' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["The block {upper} is on top of block {lower}.",
                "The block {lower} is currently situated under the block {upper}." ,
                "The block {upper} is currently situated above the block {lower}."]
            return random.choice(templates).format(lower=items[1], upper=items[0])
        else:
            raise NotImplementedError
            
    def get_negated_atom_description(self, P, grounded_atom):
        # clear/1, ontable/1, handempty/0, holding/1, on/2
        if 'clear' in grounded_atom:
            templates = ["Block {object} is not clear.",
                    "Some block is placed on top of {object}.",
                    "{object} is obstructed by other block."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'ontable' in grounded_atom:
            templates = ["Block {object} is not on the table.",
                    "Block {object} is not placed on the table.",
                    "Block {object} is not located on the table."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'handempty' in grounded_atom:
            templates = ["The robotic arm is not empty.",
                "The robotic arm is holding a block."]
            return random.choice(templates)
        elif 'holding' in grounded_atom:
            templates = ["The robotic arm is not holding {object}.",
                         "The robotic arm is empty.",
                "The block {object} is not holded."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'on' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["The block {upper} is on not on top of block {lower}.",
                "The block {lower} is not situated under the block {upper}." ,
                "The block {upper} is not situated above the block {lower}."]
            return random.choice(templates).format(lower=items[1], upper=items[0])
        else:
            raise NotImplementedError
            