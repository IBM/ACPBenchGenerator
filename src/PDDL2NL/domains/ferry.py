from PDDL2NL.utils.translation_util import ProblemTranslator, _list_to_string, _is_are, _num_obj_str
import random

class FerryTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        return "This is a ferry domain, where the task is to transport cars from their start to their goal locations, using a ferry. Each location is accessible by ferry from each other location. The cars can be debarked or boarded, and the ferry can carry only one car at a time."
    
    def get_objects_description(self, P):
        # static_symbols = P.static_symbols()
        # locations = []
        # cars = []
        # for s in static_symbols:
        #     if s.name == "location":
        #         for l in P.get_grounded_atoms(s):
        #             locations.append(l.binding[0].name)
        #     if s.name == "car":
        #         for l in P.get_grounded_atoms(s):
        #             cars.append(l.binding[0].name)
        objects = {}
        for t in ["location", "car"]:
            ttype = [i for i in P.problem.language.sorts if i.name==t][0]
            objects[t] = [x.name for x in ttype.domain()]

        # return f"There are {len(locations)} locations and {len(cars)} cars, numbered consecutively."
        return f'There are {_num_obj_str("location", objects)} and {_num_obj_str("car", objects)}, numbered consecutively.'


    def get_static_atoms_description(self, P, just_atoms=False):
        return ""
    
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        description = "Currently, "
        if just_atoms:
            description = ""
        emptyferry = 'empty-ferry ' in state
        ferryat = [f.split(" ")[1] for f in state if f.startswith("at-ferry ")]
        assert (len(ferryat) == 1)
        ferryat = ferryat[0]

        # Adding the ferry
        if emptyferry:
            description += f"the ferry is at {ferryat} location and it is empty. "
        else:
            car_at_ferry = [f.split(" ")[1] for f in state if f.startswith("on ")]
            assert(len(car_at_ferry) == 1)
            car_at_ferry = car_at_ferry[0]
            description += f"the ferry is at {ferryat}, with the car {car_at_ferry} on board. "

        # Adding cars by location
        cars = {}
        for car, location in [(f.split(" ")[1], f.split(" ")[2]) for f in state if f.startswith("at ")]:
            if location not in cars:
                cars[location] = []
            cars[location].append(car)

        description += "The cars are at locations as follows: " 
        for loc, c in cars.items():
            description += _list_to_string(c) + f" {_is_are(c)} at {loc}; "

        return description[:-2] + "."
    
    def get_atom_description(self, P, grounded_atom):
        # at-ferry/1, at/2, empty-ferry/0, on/1
        if 'at-ferry' in grounded_atom:
            templates = ["The ferry is at {ferryat} location."]
            return random.choice(templates).format(ferryat=grounded_atom.split()[1])
        elif 'on' in grounded_atom:
            templates = ["Car {object} is on board the ferry.",
                    "Car {object} is on the ferry.",
                    "Ferry has car {object} on board."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'empty-ferry' in grounded_atom:
            templates = ["The ferry is empty.",
                         "There are no cars on the ferry."]
            return random.choice(templates)
        elif 'at' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["Car {car} is at location {loc}."]
            return random.choice(templates).format(loc=items[1], car=items[0])
        else:
            raise NotImplementedError
            
            
                
    def get_negated_atom_description(self, P, grounded_atom):
        # at-ferry/1, at/2, empty-ferry/0, on/1
        if 'at-ferry' in grounded_atom:
            templates = ["The ferry is not at {ferryat} location."]
            return random.choice(templates).format(ferryat=grounded_atom.split()[1])
        elif 'on' in grounded_atom:
            templates = ["Car {object} is not on board the ferry.",
                    "Car {object} is not on the ferry.",
                    "Ferry does not have car {object} on board."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'empty-ferry' in grounded_atom:
            templates = ["The ferry is not empty."]
            return random.choice(templates)
        elif 'at' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["Car {car} is not at location {loc}."]
            return random.choice(templates).format(loc=items[1], car=items[0])
        else:
            raise NotImplementedError
            