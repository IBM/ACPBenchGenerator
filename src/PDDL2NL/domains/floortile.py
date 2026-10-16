from PDDL2NL.utils.translation_util import ProblemTranslator, _list_to_string
import random 

class FloorTileTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        return "A set of robots use different colors to paint patterns in floor tiles. The robots can move around the floor tiles in four directions (up, down, left and right). Robots paint with one color at a time, but can change their spray guns to any available color. However, robots can only paint the tile that is in front (up) and behind (down) them, and once a tile has been painted no robot can stand on it. Robots need to paint a grid with black and white, where the cell color is alternated always."
    
    def get_objects_description(self, P):
        types = set([o.sort for o in P.problem.language.constants() if "color" not in o.sort.name ])
        ot = [f"{t.cardinality()} {t.name}s" for t in types ]
        # Removing colors from objects description, appears in the initial text.
        # return f"There are two colors: black and white, {ot[0]}, and {ot[1]}."
        return f"There are {ot[0]} and {ot[1]}."
    
    def get_static_atoms_description(self, P, just_atoms=False):
        static_symbols = P.static_symbols()
        _map = {}
        for s in static_symbols:
            if s.name in ["left", "right", "up", "down"]:
                for l in P.get_grounded_atoms(s):
                    if s.name not in _map:
                        _map[s.name] = []
                    _map[s.name].append((l.binding[0].name, l.binding[1].name))
        # Describe by right and down:
        right = [f"{r} is to the right of {l}" for r, l in _map["right"]]
        down = [f"{d} is down from {u}" for d, u in _map["down"]]
        return f"The tiles locations are: " + _list_to_string(right) + ". Further, " + _list_to_string(down)
    
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        description = "Currently, "
        if just_atoms:
            description = ""
        robots = {}
        for f in state:
            if f.startswith("robot-at "):            
                r = f.split(" ")[1]
                if r not in robots:
                    robots[r] = {}
                robots[r]["pos"] = f.split(" ")[2]
            if f.startswith("robot-has "):            
                r = f.split(" ")[1]
                if r not in robots:
                    robots[r] = {}
                robots[r]["col"] = f.split(" ")[2]

        _robot_at = [f'robot {f} is at {data["pos"]} and holding color {data["col"]}' for f, data in robots.items()]
        if len(_robot_at) > 0:
            description += _list_to_string(_robot_at) +"; "

        _clear = [f.split(" ")[1] for f in state if f.startswith("clear ")]
        if len(_clear) > 0:
            description += _list_to_string(_clear) + " are clear; " if len(_clear) > 1 else " is clear; "

        _painted = [f'{f.split(" ")[1]} is painted {f.split(" ")[2]}' for f in state if f.startswith("painted ")]
        if len(_painted) > 0:
            description += _list_to_string(_painted) +"; "

        return description[:-2] + "."
    
        
    def get_atom_description(self, P, grounded_atom):
        # robot-has/2, painted/2, clear/1, robot-at/2
        if 'clear' in grounded_atom:
            templates = ["{object} is clear."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'painted' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["Tile {tile} is painted in {color} color."]
            return random.choice(templates).format(color=items[1], tile=items[0])
        elif 'robot-has' in grounded_atom:    
            items=grounded_atom.split()[1:]
            templates = ["Robot {robot} is holding {color} paint."]
            return random.choice(templates).format(color=items[1], robot=items[0])
        elif 'robot-at' in grounded_atom:    
            items=grounded_atom.split()[1:]
            templates = ["Robot {robot} is at {color} location."]
            return random.choice(templates).format(color=items[1], robot=items[0])
        else:
            raise NotImplementedError
    
        
    def get_negated_atom_description(self, P, grounded_atom):
        # robot-has/2, painted/2, clear/1, robot-at/2
        if 'clear' in grounded_atom:
            templates = ["{object} is not clear."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'painted' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["Tile {tile} is not painted in {color} color."]
            return random.choice(templates).format(color=items[1], tile=items[0])
        elif 'robot-has' in grounded_atom:    
            items=grounded_atom.split()[1:]
            templates = ["Robot {robot} is not holding {color} paint."]
            return random.choice(templates).format(color=items[1], robot=items[0])
        elif 'robot-at' in grounded_atom:    
            items=grounded_atom.split()[1:]
            templates = ["Robot {robot} is not at {color} location."]
            return random.choice(templates).format(color=items[1], robot=items[0])
        else:
            raise NotImplementedError
            