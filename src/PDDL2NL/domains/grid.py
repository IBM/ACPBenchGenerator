from PDDL2NL.utils.translation_util import ProblemTranslator
import math
import random 

class GridTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        description = f"A robot is in a grid and can only move to places that are connected to its current position."
        return description
        
    def get_objects_description(self, P):
        rows = int(P.problem.name.split('-')[1].replace("x",""))
        cols = int(P.problem.name.split('-')[2].replace("y",""))
        return f"The grid size is {rows}x{cols}, and the locations are of the form fi-jf (e.g., f3-2f or f0-1f). The grid cells are connected to their neighbors (e.g., f1-2f is connected to the four neighbors f0-2f, f2-2f, f1-1f, and f1-3f). Some positions on the grid are locked and can be opened with a key of a matching shape. The robot has an arm that can pick up a key when the key is in same location as the robot and the arm is empty. "
    
    def get_static_atoms_description(self, P):
        description = ""
        # place_symbol = [i for i in P.static_symbols() if i.name == 'place'][0]
        # places = ", ".join([j.binding[0].name for i, j in P.get_grounded_atoms(place_symbol).enumerate()])
        # description = f"There are {P.get_atom_counts(place_symbol)} positions on the grid: {places}. "
        # conn_symbol = [i for i in P.static_symbols() if i.name == 'conn'][0]
        # description += "The following positions are connected: "
        # description += ", ".join([f"{j.binding[0].name} to {j.binding[1].name}" for _, j in P.get_grounded_atoms(conn_symbol).enumerate()]) + ". "
        # lockshape_symbol = [i for i in P.static_symbols() if i.name == 'lock-shape'][0]

        # shape_symbol = [i for i in P.static_symbols() if i.name == 'shape'][0]
        keyshape_symbol = [i for i in P.static_symbols() if i.name == 'key-shape'][0]
        shape_symbol = [i for i in P.problem.language.sorts if i.name== "shape"][0]
        # keyshape_symbol = [i for i in P.problem.language.sorts if i.name == 'key-shape'][0]

        key_list = ", ".join([f"Key {j.binding[0].name} is of shape {j.binding[1].name}" for i, j in P.get_grounded_atoms(keyshape_symbol).enumerate()])
        description += f"There are {P.get_atom_counts(keyshape_symbol)} keys in {P.get_atom_counts(shape_symbol)} different shapes: {key_list}. "
        return description
        
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        description = "Currently, "
        if just_atoms:
            description = ""
        robot_at = [f.replace("at-robot ", "") for f in state if "at-robot " in f][0]
        if "arm-empty " in state:
            description += f"the robot is at position {robot_at} and its arm is empty. "
        else:
            holding_key = [f.replace("holding ", "") for f in state if "holding " in f][0]
            description += f"the robot is at position {robot_at} and is holding {holding_key}. "
        lockshape_symbol = [i for i in P.static_symbols() if i.name == 'lock-shape'][0]
        lockshape_dict = {j.binding[0].name: j.binding[1].name for i, j in P.get_grounded_atoms(lockshape_symbol).enumerate()}
        locked_positions = [f.replace("locked ", "") for f in state if "locked " in f]
        description += "All the positions are open except the following: "
        description += ", ".join([ f"{i} has {lockshape_dict[i]} shaped lock" for i in locked_positions]) + ". "
        keys_list = [f.replace("at ", "").split() for f in state if "at " in f]
        description += " ".join([f"Key {k[0]} is at position {k[1]}." for k in keys_list])
        return description    
    
    def get_atom_description(self, P, grounded_atom):
        # at-robot/1, holding/1, at/2, locked/1, arm-empty/0, open/1
        if 'holding' in grounded_atom:
            templates = ["Robot is holding {object}."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'locked' in grounded_atom:
            templates = ["Location {object} is locked."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'open' in grounded_atom:
            templates = ["Location {object} is open."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'at-robot' in grounded_atom:    
            items=grounded_atom.split()[1:]
            templates = ["Robot is at {loc} location."]
            return random.choice(templates).format(loc=items[0])
        elif 'at' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["Key {key} is at {loc} location."]
            return random.choice(templates).format(loc=items[1], key=items[0])
        elif 'arm-empty' in grounded_atom:
            templates = ["Robot's arm is empty.",
                "Robot is not holding anything."]
            return random.choice(templates)
        else:
            raise NotImplementedError
        
    
    def get_negated_atom_description(self, P, grounded_atom):
        # at-robot/1, holding/1, at/2, locked/1, arm-empty/0, open/1
        if 'holding' in grounded_atom:
            templates = ["Robot is not holding {object}."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'locked' in grounded_atom:
            templates = ["Location {object} is not locked."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'open' in grounded_atom:
            templates = ["Location {object} is not open."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'at-robot' in grounded_atom:    
            items=grounded_atom.split()[1:]
            templates = ["Robot is not at {loc} location."]
            return random.choice(templates).format(loc=items[0])
        elif 'at' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["Key {key} is not at {loc} location."]
            return random.choice(templates).format(loc=items[1], key=items[0])
        elif 'arm-empty' in grounded_atom:
            templates = ["Robot's arm is not empty.",
                "Robot is holding something."]
            return random.choice(templates)
        else:
            raise NotImplementedError