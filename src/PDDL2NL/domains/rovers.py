from PDDL2NL.utils.translation_util import ProblemTranslator, _is_are, _list_to_string
from collections import defaultdict
import random

class RoversTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        return "This is a Rovers domain where rovers must navigate between waypoints gathering data and transmitting it back to a lander. Rovers cannot navigate to all waypoints and this makes particular routes impassable to some of the rovers. Data transmission is also constrained by the visibility of the lander from the waypoints."
        
    def get_objects_description(self, P):
        object_types = P.problem.language.sorts
        rover = object_types[1].cardinality()
        waypoint = object_types[2].cardinality()
        store = object_types[3].cardinality()
        camera = object_types[4].cardinality()
        mode = object_types[5].cardinality()
        lander = object_types[6].cardinality()
        objective = object_types[7].cardinality()
        
        return f"There are {rover} rovers, {waypoint} waypoints, {store} stores, {camera} cameras, {objective} objectives numbered consecutively. Further, there is 1 lander and 3 modes for the camera namely colour, high resolution, and low resolution. "
    
    def get_static_atoms_description(self, P):
        #[equipped_for_imaging/1, visible_from/2, on_board/2, calibration_target/2, at_lander/2, 
        #can_traverse/3, equipped_for_soil_analysis/1, equipped_for_rock_analysis/1, supports/2, visible/2, store_of/2]

        # [equipped_for_soil_analysis/1, visible/2, supports/2, can_traverse/3, store_of/2, calibration_target/2, on_board/2, equipped_for_imaging/1, equipped_for_rock_analysis/1, visible_from/2, at_lander/2]

        des_equipped_for_imaging = ""
        des_equipped_for_rock_analysis = ""
        des_equipped_for_soil_analysis = ""
        des_can_traverse = ""
        des_visible_from = ""
        des_on_board = ""
        des_calibration_target = ""
        des_lander = ""
        des_supports = ""
        des_store = ""
        des_visible_objective = ""


        visible_objective = [i for i in P.static_symbols() if i.name == 'visible_from'][0]
        visible_objective_list = []
        for f in P.get_grounded_atoms(visible_objective):
            f = str(f).replace("visible_from(", "").replace(")", "")
            visible_objective_list.append(f.split(","))

        visible_objective_from_dic = {}
        for objective, loc in visible_objective_list:
            if objective in  visible_objective_from_dic.keys():
                visible_objective_from_dic[objective] += [loc]
            else:
                visible_objective_from_dic[objective] = [loc]
        
        for objective, locs in visible_objective_from_dic.items():
            des_visible_objective += f"Objective {objective} is visible from {_list_to_string(locs)}. "
            # for loc in visible_objective_from_dic[objective]:
            #     des_visible_objective += f"{loc} and "
            # des_visible_objective = des_visible_objective[:-5] +". " 
        
        store = [i for i in P.static_symbols() if i.name == 'store_of'][0]
        #assumption each rover has one store
        store_list = []
        for f in P.get_grounded_atoms(store):
            f = str(f).replace("store_of(", "").replace(")", "")
            store_list.append(f.split(","))
        for store, rover in store_list:
            des_store += f"Rover {rover} has store {store}. "

        supports = [i for i in P.static_symbols() if i.name == 'supports'][0]
        supports_list = []
        for f in P.get_grounded_atoms(supports):
            f = str(f).replace("supports(", "").replace(")", "")
            supports_list.append(f.split(","))

        supports_dic = {}
        for camera, mode in supports_list:
            if camera in  supports_dic.keys():
                supports_dic[camera] += [mode]
            else:
                supports_dic[camera] = [mode]
        
        for camera in supports_dic.keys():
            des_supports += f"Camera {camera} supports "
            for mode in supports_dic[camera]:
                des_supports += f"{mode} and "
            des_supports = des_supports[:-5] +". " 
        
        lander = [i for i in P.static_symbols() if i.name == 'at_lander'][0]
        for f in P.get_grounded_atoms(lander): 
            des_lander += str(f).replace("at_lander(", "Lander ").replace(")", "").replace(",", " is at waypoint ") + ". "
        
        #assumption each camera is calibrated on one target
        calibration_target = [i for i in P.static_symbols() if i.name == 'calibration_target'][0]
        for f in P.get_grounded_atoms(calibration_target):
            des_calibration_target += str(f).replace("calibration_target(", "Camera ").replace(")", "").replace(",", " can be calibrated on ") + ". "
        
        on_board = [i for i in P.static_symbols() if i.name == 'on_board'][0]
        on_board_list = []
        for f in P.get_grounded_atoms(on_board):
            f = str(f).replace("on_board(", "").replace(")", "")
            on_board_list.append(f.split(","))

        on_board_dic = {}
        for camera, rover in on_board_list:
            if rover in  on_board_dic.keys():
                on_board_dic[rover] += [camera]
            else:
                on_board_dic[rover] = [camera]
        
        for rover in on_board_dic.keys():
            des_on_board += f"Rover {rover} has "
            for camera in on_board_dic[rover]:
                des_on_board += f"{camera} and "
            des_on_board = des_on_board[:-5] + " on board. "
        
        can_traverse = [i for i in P.static_symbols() if i.name == 'can_traverse'][0]
        can_traverse_list = []
        for f in P.get_grounded_atoms(can_traverse):
            f = str(f).replace("can_traverse(", "").replace(")", "")
            can_traverse_list.append(f.split(","))

        traverse_dic = {}
        for rover, fromLoc, toLoc in can_traverse_list:
            if rover in  traverse_dic.keys():
                traverse_dic[rover] += [(fromLoc, toLoc)]
            else:
                traverse_dic[rover] = [(fromLoc, toLoc)]
        
        for rover in traverse_dic.keys():
            des_can_traverse += f"Rover {rover} can traverse from "
            des_can_traverse += ", ".join([f"{fromTo} to {To}" for fromTo, To in traverse_dic[rover]]) +". "
        # des_can_traverse = des_can_traverse[:-2] + ". "
        
        
        equipped_for_imaging = [i for i in P.static_symbols() if i.name == 'equipped_for_imaging'][0]
        items_equipped_for_imaging = [str(f).replace("equipped_for_imaging(", "").replace(")", "")   for f in P.get_grounded_atoms(equipped_for_imaging)]
        des_equipped_for_imaging = ""
        if len(items_equipped_for_imaging) > 0:
            des_equipped_for_imaging +=  f"Rover(s) {_list_to_string(items_equipped_for_imaging)} {_is_are(items_equipped_for_imaging)} equipped for imaging. "
        else:
            des_equipped_for_imaging +=  f"No rovers are equipped for imaging. "
                    
        equipped_for_rock_analysis = [i for i in P.static_symbols() if i.name == 'equipped_for_rock_analysis'][0]
        items_equipped_for_rock_analysis = [str(f).replace("equipped_for_rock_analysis(", "").replace(")", "")   for f in P.get_grounded_atoms(equipped_for_rock_analysis)]
        des_equipped_for_rock_analysis = ""
        if len(items_equipped_for_rock_analysis) > 0:
            des_equipped_for_rock_analysis +=  f"Rover(s) {_list_to_string(items_equipped_for_rock_analysis)} {_is_are(items_equipped_for_rock_analysis)} equipped for rock analysis. "
        else:
            des_equipped_for_rock_analysis +=  f"No rovers are equipped for rock analysis. "
        

        equipped_for_soil_analysis = [i for i in P.static_symbols() if i.name == 'equipped_for_soil_analysis'][0]
        items_equipped_for_soil_analysis = [str(f).replace("equipped_for_soil_analysis(", "").replace(")", "")   for f in P.get_grounded_atoms(equipped_for_soil_analysis)]
        des_equipped_for_soil_analysis = ""
        if len(items_equipped_for_soil_analysis) > 0:
            des_equipped_for_soil_analysis +=  f"Rover(s) {_list_to_string(items_equipped_for_soil_analysis)} {_is_are(items_equipped_for_soil_analysis)} equipped for soil analysis. "
        else:
            des_equipped_for_soil_analysis +=  f"No rovers are equipped for soil analysis. "
        

        visible_from_dict = defaultdict(list)
        visible_from = [i for i in P.static_symbols() if i.name == 'visible'][0]
        for f in P.get_grounded_atoms(visible_from):
            f = str(f).replace("visible(", "").replace(")", "")
            items = f.split(",")
            visible_from_dict[items[1]].append(items[0])

        des_visible_from = ""
        for k, v in visible_from_dict.items():
            if len(v) >= 1:
                des_visible_from += f"Waypoint(s) {_is_are(v)} visible from {k}: {_list_to_string(v)}. "
        
        return des_equipped_for_soil_analysis + des_equipped_for_rock_analysis + des_equipped_for_imaging + des_store + des_on_board + des_calibration_target + des_supports + des_can_traverse +  des_visible_from + des_visible_objective + des_lander

        
    def get_fluent_atoms_description(self, P, state, just_atoms=False):

        #calibrated/2
        
        description = "Currently, "
        if just_atoms:
            description = ""

        at = [f.replace("at ", "").split(" ") for f in state if "at " in f]
        if len(at) >= 1: 
            for rover, location in at:
                description += f"Rover {rover} is at {location}. "
        
        at_rock = [f.replace("at_rock_sample ", "") for f in state if "at_rock_sample" in f]
        if len(at_rock) > 0:
            description += f"Rocks can be sampled at the following location(s): {_list_to_string(at_rock)}. "

        at_soil = [f.replace("at_soil_sample ", "") for f in state if "at_soil_sample" in f]
        if len(at_soil) > 0:
            description += f"Soil can be sampled at the following location(s): {_list_to_string(at_soil)}. "


        available = [f.replace("available ", "") for f in state if "available" in f]
        if(len(available) ==1):
            description += f"Rover {available[0]} is available. "
        elif (len(available) >1): 
            description += f"Rovers {_list_to_string(available)} are available. "


        communicated_rock_data = [f.replace("communicated_rock_data ", "") for f in state if "communicated_rock_data" in f]
        if(len(communicated_rock_data) == 1):
            description += f"Rock data was communicated from waypoint {communicated_rock_data[0]}; "
        elif (len(communicated_rock_data) > 1): 
            description += "Rock data were communicated from the following waypoints: " + ", ".join(communicated_rock_data) + ". "

        communicated_soil_data = [f.replace("communicated_soil_data ", "") for f in state if "communicated_soil_data" in f]
        if(len(communicated_soil_data) == 1):
            description += f"Soil data was communicated from waypoint {communicated_soil_data[0]}; "
        elif (len(communicated_soil_data) >1): 
            description += "Soil data were communicated from the following waypoints: " + ", ".join(communicated_soil_data) + ". "

        
        communicated_image_data = [f.replace("communicated_image_data ", "").split(" ") for f in state if "communicated_image_data" in f]
        if len(communicated_image_data) >= 1:
            for image, mode in communicated_image_data:
                description += f"Image {image} was communicated in mode {mode}. "


        
        have_soil_analysis = [f.replace("have_soil_analysis ", "").split(" ") for f in state if "have_soil_analysis" in f]
        if len(have_soil_analysis) >= 1:
            for rover, loc in have_soil_analysis :
                description += f"Rover {rover} has soil analyzed in waypoint {loc}. "


        have_rock_analysis = [f.replace("have_rock_analysis ", "").split(" ") for f in state if "have_rock_analysis" in f]
        if len(have_rock_analysis) >= 1:
            for rover, loc in have_rock_analysis :
                description += f"Rover {rover} has rock analyzed in waypoint {loc}. "


        have_image = [f.replace("have_image ", "").split(" ") for f in state if "have_image" in f]
        if len(have_image) >= 1:
            for rover, objective, mode in have_image :
                description += f"Rover {rover} has image {objective} in mode {mode}. "


        calibrated = [f.replace("calibrated ", "").split(" ") for f in state if "calibrated" in f]
        if len(calibrated) >= 1:
            for camera, rover in calibrated :
                description += f"Rover {rover} has its camera {camera} calibrated. "
                

        empty = [f.replace("empty ", "") for f in state if "empty " in f]
        if len(empty) > 0:
            description += f"Store(s) {_list_to_string(empty)} {_is_are(empty)} empty. "


        full = [f.replace("full ", "") for f in state if "full " in f]
        if len(full) > 0:
            description += f"Store(s) {_list_to_string(full)} {_is_are(full)} full. "
            
        #Note: channel free is not really used or is meanigfull - ignoring it. 
        if just_atoms:
            free_channels = [f.replace("channel_free ", "") for f in state if "channel_free " in f]
            if len(free_channels) > 0:
                description += f"Channel {_list_to_string(free_channels)} {_is_are(free_channels)} free. "
        
        return description

    def get_negated_atom_description(self, P, grounded_atom):
        # empty/1, at_soil_sample/1, at/2, at_rock_sample/1, full/1, calibrated/2, channel_free/1, available/1
        if 'have_rock_analysis' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["Rover {rover} does not have rock analyzed at waypoint {loc}."]
            return random.choice(templates).format(rover=items[0], loc=items[1])
        elif 'calibrated' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = [ "Rover {rover} does not have its camera {camera} calibrated." ]
            return random.choice(templates).format(camera=items[0], rover=items[1])
        elif 'communicated_soil_data' in grounded_atom:
            templates = ["Soil data was not communicated from waypoint {object}."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'at_soil_sample' in grounded_atom:
            templates = ["Soil should not be sampled at {object}.",
                         "Soil at {object} is sampled."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'at_rock_sample' in grounded_atom:
            templates = ["Rock should not be sampled at {object}.",
                         "Rock at {object} is sampled."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'full' in grounded_atom:
            templates = ["Store {object} is not full."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'empty' in grounded_atom:
            templates = ["Store {object} is not empty."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        elif 'at' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["Rover {rover} is not at {location}.",
                "Rover {rover} is not longer at {location}."]
            return random.choice(templates).format(rover=items[0], location=items[1])
        elif 'channel_free' in grounded_atom:
            templates = ["Channel {object} is not free."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        
        elif 'available' in grounded_atom:
            templates = ["Rover {object} is not available."]
            return random.choice(templates).format(object=grounded_atom.split()[1])
        else:
            raise NotImplementedError