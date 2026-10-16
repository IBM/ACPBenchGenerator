from PDDL2NL.utils.translation_util import ProblemTranslator, _list_to_string, _is_are

class GoldMinerTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        description = f"A robotic arm is in a grid and can only move to locations that are connected to its current location."
        return description
    
    def get_objects_description(self, P):
        rows = int(P.problem.name.split('-')[2].replace("rows",""))
        cols = int(P.problem.name.split('-')[3].replace("cols",""))
        description = f"The {rows}x{cols} grid locations may have gold, hard rocks, or soft rocks. Rocks cannot be moved. The robotic arm can pick up laser or bomb. Only one item can be picked at a time.  There is one laser is the grid that can be used to clear rocks. Robotic arm can fire laser at a location from a connected location. The locations are of the form fi-jf (e.g., f3-2f or f0-1f). The grid cells are connected to their neighbors (e.g., f1-2f is connected to the four neighbors f0-2f, f2-2f, f1-1f, and f1-3f). "
        return description
    
    def get_static_atoms_description(self, P, just_atoms=False):
        bomb_at_symbol = [i for i in P.static_symbols() if i.name == 'bomb-at'][0]
        bomb_location = [i.binding[0].name for i in P.get_grounded_atoms(bomb_at_symbol)]
        description = f"If a bomb is picked, it cannot be placed back. It can only be detonated at connected location that have soft rock. Bomb supply is available at {bomb_location[0]} location. "
        location_type = [i for i in P.problem.language.sorts if i.name=='loc'][0]
        # description += f"There are {location_type.cardinality()} locations on the grid: "
        # description += ", ".join([i.name for i in location_type.domain()]) + ". "
        
        # conn_symbol = [i for i in P.static_symbols() if i.name == 'connected'][0]
        # description += "The following locations are connected: "
        # description += ", ".join([f"{j.binding[0].name} to {j.binding[1].name}" for j in P.get_grounded_atoms(conn_symbol)]) + ". "
    
        return description
    
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        description = "Currently, "
        if just_atoms:
            description = ""
        robot_at = [f.replace("robot-at ", "") for f in state if "robot-at " in f]
        if not just_atoms:
            if len(robot_at) > 0:
                description += f"the robot is at position {robot_at[0]} and "
            if "arm-empty " in state:
                description += f"its arm is empty."
            elif "holds-bomb " in state:
                description += f"is holding a bomb."
            elif "holds-laser " in state:
                description += f"is holding a laser."
            elif "holds-gold " in state:
                description += f"is holding gold."
        else: 
            if len(robot_at) > 0:
                description += f"The robot is at position {robot_at[0]}."
            if "arm-empty " in state:
                description += f"The robot's arm is empty."
            elif "holds-bomb " in state:
                description += f"The robot is holding a bomb."
            elif "holds-laser " in state:
                description += f"The robot is holding a laser."
            elif "holds-gold " in state:
                description += f"The robot is holding gold."
        hard_rock = [f.replace("hard-rock-at ", "") for f in state if "hard-rock-at " in f]
        if len(hard_rock) > 0:
            if not just_atoms:
                description += f" The following locations have hard rock: {_list_to_string(hard_rock)}."
            else:
                description += f"Hard rock at {_list_to_string(hard_rock)}."
        
        soft_rock = [f.replace("soft-rock-at ", "") for f in state if "soft-rock-at " in f]
        if len(soft_rock) > 0:
            if not just_atoms:
                description += f" The following locations have soft rock: {_list_to_string(soft_rock)}."
            else:
                description += f"Soft rock at {_list_to_string(soft_rock)}."
            
        gold_location = [f.replace("gold-at ", "") for f in state if "gold-at " in f]
        if len(gold_location) > 0:
            description += f" The gold is at {gold_location[0]} location."
        
        laser_location = [f.replace("laser-at ", "") for f in state if "laser-at " in f]
        if len(laser_location) > 0:
            description += f" The laser is at {laser_location[0]} location."
        if just_atoms:
            clear_location = [f.replace("clear ", "") for f in state if "clear " in f]
            if len(clear_location) > 0:
                description += f"Location(s) {_list_to_string(clear_location)} {_is_are(clear_location)} clear."
        
        return description
