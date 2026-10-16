from PDDL2NL.utils.translation_util import ProblemTranslator, _num_obj_str, _list_to_string, _is_are
import random 

class GrippersTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        return "This is a grippers domain, where there is a robot with two grippers. The robot can carry a ball in each. The goal is to take the balls from one room to another."
    
    def get_objects_description(self, P):
        static_symbols = P.problem.language.constants()
        objects = {}
        for s in static_symbols:
            if s.sort.name in ["robot", "room", "ball"]:
                if s.sort.name not in objects:
                    objects[s.sort.name] = []
                objects[s.sort.name].append(s.name)
        # # Rename
        # objects["ball"] = objects.pop("object")

        return f'There are {_num_obj_str("robot", objects)}, {_num_obj_str("room", objects)}, and {_num_obj_str("ball", objects)}, numbered consecutively.'

        
    def get_static_atoms_description(self, P):
        return ""
        
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        _at = {}
        _at_robby = {}
        _free = {}
        _carry = {}
            
        for f in state:
            if f.startswith("at "):
                l = f.split(" ")[2]
                if l not in _at:
                    _at[l] = []
                _at[l].append(f.split(" ")[1])
            if f.startswith("at-robby "):
                r, l = f.split(" ")[1: 3]
                _at_robby[r] = l
            if f.startswith("free "):
                r, g = f.split(" ")[1: 3]
                if r not in _free:
                    _free[r] = set()
                if g.startswith("left"):
                    _free[r].add("l")
                elif g.startswith("right"):
                    _free[r].add("r")
                else:
                    _free[r].add(g)
            if f.startswith("carry "):
                r, b, g = f.split(" ")[1:4]
                if r not in _carry:
                    _carry[r] = { }
                if g.startswith("left"):
                    g = "l"
                elif g.startswith("right"):
                    g = "r"
                _carry[r][g] = b

        description = "Currently, "

        for r, l in _at_robby.items():
            lfree = r in _free and "l" in _free[r]
            rfree = r in _free and "r" in _free[r]
            if lfree and rfree:
                gdesc = " and both grippers are free"
            elif rfree:
                # left gripper is not free
                gdesc = f', right gripper is free, and left gripper is carrying the ball {_carry[r]["l"]}'  
            elif lfree:
                # right gripper is not free
                gdesc = f', left gripper is free, and right gripper is carrying the ball {_carry[r]["r"]}'  
            else:
                # both grippers is not free
                gdesc = f', left gripper is carrying the ball {_carry[r]["l"]}, and right gripper is carrying the ball {_carry[r]["r"]}'  

            description += f'the robot {r} is at {l}' + gdesc + ', '
        description = description[:-2] + "."
        if len(_at.keys()) > 0:
            description += " Additionally, "
            for l, f in _at.items():
                description += f'{_list_to_string(f)} {_is_are(f)} at {l}, '
            
            description = description[:-2] + "." 
        return description
    
    
    def get_atom_description(self, P, grounded_atom):
        # at-robby/2, carry/3, free/2, at/2]
        if 'at-robby' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["Robot {robo} is at {loc} location.", "Robot {robo} is in room {loc}.", ]
            return random.choice(templates).format(loc=items[1], robo=items[0])
        elif 'free' in grounded_atom:
            items=grounded_atom.split()[1:]
            if 'l' in items[1]:
                return f"The left gripper of robot {items[0]} is free."
            elif 'r' in items[1]:
                return f"The right gripper of robot {items[0]} is free."
            else:
                return f"The gripper {items[1]} of robot {items[0]} is free."
        elif 'at' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["Ball {ball} is at {loc} location.", "Ball {ball} is in room {loc}.", ]
            return random.choice(templates).format(loc=items[1], ball=items[0])
        elif 'carry' in grounded_atom:
            items=grounded_atom.split()[1:]
            if 'l' in items[2]:
                return f"Robot {items[0]} is carrying the ball {items[1]} in the left gripper."
            elif 'r' in items[2]:
                return f"Robot {items[0]} is carrying the ball {items[1]} in the right gripper."
            else:
                return f"Robot {items[0]} is carrying the ball {items[1]} in gripper {items[2]}."
        else:
            raise NotImplementedError
        
    def get_negated_atom_description(self, P, grounded_atom):
        # at-robby/2, carry/3, free/2, at/2]
        if 'at-robby' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["Robot {robo} is not at {loc} location.", "Robot {robo} is not in the room {loc}.", ]
            return random.choice(templates).format(loc=items[1], robo=items[0])
        elif 'free' in grounded_atom:
            items=grounded_atom.split()[1:]
            if 'l' in items[1]:
                return f"The left gripper of robot {items[0]} is not free."
            if 'r' in items[1]:
                return f"The right gripper of robot {items[0]} is not free."
        elif 'at' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["Ball {ball} is not at {loc} location.", "Ball {ball} is not in the room {loc}.", ]
            return random.choice(templates).format(loc=items[1], ball=items[0])
        elif 'carry' in grounded_atom:
            items=grounded_atom.split()[1:]
            if 'l' in items[2]:
                return f"Robot {items[0]} is not carrying the ball {items[1]} in the left gripper."
            if 'r' in items[2]:
                return f"Robot {items[0]} is not carrying the ball {items[1]} in the right gripper."
        else:
            raise NotImplementedError