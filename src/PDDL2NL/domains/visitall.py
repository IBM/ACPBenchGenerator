from PDDL2NL.utils.translation_util import ProblemTranslator, _list_to_string
import random

class VisitallTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        return "This is a visitall domain where a robot in a grid must visit all the cells or places in the grid. There are some unavailable places in the grid."   
    
    def get_objects_description(self, P):
        rows = int(P.problem.name.split('-')[1])
        cols = int(P.problem.name.split('-')[2])
        return f"The grid size is {rows}x{cols}, and the location cell names are of the form loc-xi-yj (e.g., loc-x0-y2 or loc-x1-y1)."


    def get_static_atoms_description(self, P):
        rows = int(P.problem.name.split('-')[1])
        cols = int(P.problem.name.split('-')[2])

        places = P.problem.language.constants()
        cells = set()
        for p in places:
            cells.add(p.name)

        if len(cells) == rows*cols:
            return f"The grid cells are connected to their available neighbors. There are no unavailable cells."

        assert ( len(cells) < rows*cols )
        all_cells = set([f"loc-x{i}-y{j}" for i in range(rows) for j in range(cols)])
        u = list(all_cells - cells)

        if len(u) == 1:
            return f'The grid cells are connected to their available neighbors. The only unavailable cell is {u[0]}.'

        return f'The grid cells are connected to their available neighbors. The unavailable cells are {_list_to_string(u)}.'

        
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        description = "Currently, "
        if just_atoms:
            description = ""
        at_robot = [f.replace("at-robot ", "") for f in state if "at-robot " in f]
        if len(at_robot) > 0:
            description += "the robot is in place " + at_robot[0] + "."
        visited = [f.replace("visited ", "") for f in state if "visited" in f]
        if len(visited) == 1:
            description += "Place " + str(visited[0]) + " has been visited."
        elif len(visited) > 1:
            description += f"The following places have been visited: {_list_to_string(visited)}."
        return description 
    
    def get_atom_description(self, P, grounded_atom):
        if 'at-robot' in grounded_atom:
            templates = ["The robot is in place {loc}.",
                    "The robot is at {loc}.",]
            return random.choice(templates).format(loc=grounded_atom.split()[1])
        elif 'visited' in grounded_atom:
            templates = ["Place {loc} is visited."]
            return random.choice(templates).format(loc=grounded_atom.split()[1])
        else:
            raise NotImplementedError
        
    def get_negated_atom_description(self, P, grounded_atom):
        if 'at-robot' in grounded_atom:
            templates = ["The robot is not in place {loc}.",
                    "The robot is not at {loc}.",]
            return random.choice(templates).format(loc=grounded_atom.split()[1])
        elif 'visited' in grounded_atom:
            templates = ["Place {loc} is not visited."]
            return random.choice(templates).format(loc=grounded_atom.split()[1])
        else:
            raise NotImplementedError
            
        