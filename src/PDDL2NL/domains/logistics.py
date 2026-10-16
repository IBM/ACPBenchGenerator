from PDDL2NL.utils.translation_util import ProblemTranslator, _num_obj_str, _list_to_string, _is_are
import random

class LogisticsTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        return "There are several cities, each containing several locations, some of which are airports. There are also trucks, which can drive within a single city, and airplanes, which can fly between airports. The goal is to get some packages from various locations to various new locations."
    
    def get_objects_description(self, P):
        # static_symbols = P.static_symbols()
        objects = {}
        # for s in static_symbols:
        #     if s.name in ["location", "city", "truck", "airplane", "airport", "obj"]:
        #         for l in P.get_grounded_atoms(s):
        #             if s.name not in objects:
        #                 objects[s.name] = []
        #             objects[s.name].append(l.binding[0].name)
        # Rename
        # objects["package"] = objects.pop("obj")
        for t in ["location", "city", "truck", "airplane", "airport", "package"]:
            ttype = [i for i in P.problem.language.sorts if i.name==t][0]
            objects[t] = [x.name for x in ttype.domain()]

        return f'There are {_num_obj_str("truck", objects)} and {_num_obj_str("airplane", objects)}, as well as {_num_obj_str("package", objects)}. There are {_num_obj_str("location", objects)} across {_num_obj_str("city", objects)}.'
        
    def get_static_atoms_description(self, P):
        static_symbols = P.static_symbols()
        cities = {}
        for s in static_symbols:
            if s.name == "in-city":
                for l in P.get_grounded_atoms(s):
                    city = l.binding[1].name
                    loc = l.binding[0].name
                    if city not in cities:
                        cities[city] = []
                    cities[city].append(loc)
        description = "The locations are in cities as follows: "
        for city, locations in cities.items():
            description += f'{_list_to_string(locations)} {_is_are(locations)} in {city}; ' 
        return description[:-2] + "."
    
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        
        description = "Currently, "
        if just_atoms:
            description = ""
        _at = {}
        _in = {}
            
        for f in state:
            if f.startswith("at "):
                l = f.split(" ")[2]
                if l not in _at:
                    _at[l] = []
                _at[l].append(f.split(" ")[1])
            if f.startswith("in "):
                v = f.split(" ")[2]
                if v not in _in:
                    _in[v] = []
                _in[v].append(f.split(" ")[1])

        for l, f in _at.items():
            description += f'{_list_to_string(f)} {_is_are(f)} at {l}, '

        for v, f in _in.items():
            description += f'{_list_to_string(f)} {_is_are(f)} in {v}, '

        return description[:-2] + "."
    
    def get_negated_atom_description(self, P, grounded_atom):
        if 'at' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["{object} is not at {location}.",
                "{object} is not at location {location}."]
            return random.choice(templates).format(object=items[1], location=items[0])
        elif 'in' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["{object} is not in {location}.",]
            return random.choice(templates).format(object=items[1], location=items[0])
        else:
            raise NotImplementedError
            