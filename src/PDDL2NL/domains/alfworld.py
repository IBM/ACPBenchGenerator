import re

from PDDL2NL.utils.translation_util import ProblemTranslator, _num_obj_str, _list_to_string, _is_are

class AlfworldTranslator(ProblemTranslator):

    # get the prefix (before the _bar)
    def _get_object_prefix(self, object):
        if "sinkbasin" in object:
            return "sinkbasin"
        pattern = r'[0-9]'
        return  re.sub(pattern, '', object)

    def _has_num(self, object):
        pattern = r'[0-9]'
        return  bool(re.search(pattern, object)) 

    def _get_on_in(self, receptacle):
        onlist = ['stoveburner', 'ottoman', 'sidetable', 'diningtable', 'coffeetable', 'dresser', 'desk', 'towelholder', 'toiletpaperhanger', 'sofa', 'armchair', 'handtowelholder', 'tvstand', 'laundryhamper', 'shelf', 'paintinghanger', 'countertop']
        inlist = ['garbagecan', 'cabinet', 'bed', 'cart', 'drawer', 'toilet', 'bathtubbasin', 'coffeemachine', 'toaster', 'sink', 'sinkbasin', 'microwave', 'fridge', 'safe']
        
        receptacle = self._get_object_prefix(receptacle)

        if receptacle in onlist:
            return "on"
        elif receptacle in inlist:
            return "in"
        return "on"


    def get_domain_description(self):
        return "This is an alfworld domain where an agent is asked to carry different tasks such as: picking up objects, opening or closing receptacles, warming up an object in a microwave, cleaning an object in a sink, or toggling an object. "
    
    def get_objects_description(self, P):

        objects = {}
        static_symbols = P.problem.language.constants()

        for s in static_symbols:
            if s.sort.name in ["location"]:
                if s.sort.name not in objects: 
                    objects[s.sort.name] = []
                objects[s.sort.name].append(s.name)

            if s.sort.name in ["receptacle", "objectorreceptacle"]:
                if "receptacle" not in objects:
                    objects["receptacle"] = {}

                receptacleType = self._get_object_prefix(s.name)
                receptacleDic = objects["receptacle"]
        
                if (receptacleType not in receptacleDic): 
                    receptacleDic[receptacleType] = [s.name] 
                else:
                    receptacleDic[receptacleType].append(s.name)

                objects["receptacle"] = receptacleDic

            if s.sort.name in ["object", "objectorreceptacle"]:
                if "object" not in objects:
                    objects["object"] = {}

                objectType = self._get_object_prefix(s.name)
                objectDic = objects["object"]
                if self._has_num(s.name):
                    if (objectType not in objectDic): 
                        objectDic[objectType] = [s.name] 
                    else:
                        objectDic[objectType].append(s.name)
                objects["object"] = objectDic

        receptaclestxt = "" 
        itemstxt = ""
        locationstxt = ""

        for item in objects['object']:
            itemstxt += _num_obj_str(item, objects['object']) + ", "

        for receptacle in objects['receptacle']:
            receptaclestxt += _num_obj_str(receptacle, objects['receptacle']) + ", "

        locationstxt  = _num_obj_str("location", objects)
        return("There are "+ str(len(objects['object'])) + " object types: " + itemstxt  + str(len(objects['receptacle'])) + " receptacle types: " + receptaclestxt + "and " + locationstxt + " all numbered consecutively. ")
  



    def get_static_atoms_description(self, P):

        #receptacleAtLocation
        receptacleatlocation = [i for i in P.static_symbols() if i.name == 'receptacleatlocation'][0]

        receptacleatlocation_list = []
        receptacleatLocationdic = {}

        for f in P.get_grounded_atoms(receptacleatlocation):
            f = str(f).replace("receptacleatlocation(", "").replace(")", "")
            receptacleatlocation_list.append(f.split(","))
        for receptacle, location in receptacleatlocation_list:
            if location not in receptacleatLocationdic: #first time for location
                receptacleatLocationdic[location] = [receptacle]
            else:
                receptacleatLocationdic[location].append(receptacle)

        if len(receptacleatLocationdic) > 1:
            description = "The receptacles are at locations as follows. "

        for location in receptacleatLocationdic:
            if len(receptacleatLocationdic[location]) == 1:
                description += f"{receptacleatLocationdic[location][0]} is at {location}. "
            elif len(receptacleatLocationdic[location]) > 1:
                description += f"{_list_to_string(receptacleatLocationdic[location])} are at {location}. "

        description += "Receptacles that are neither open nor closed are not openable. Receptacles are not pickupable. Desklamps are not pickupable. "

        return description

    def get_fluent_atoms_description(self, P, state, just_atoms=False):

        description = "Currently, "
        if just_atoms:
            description = ""

        objectdic = {}
        objectatlocation = [f.replace("objectatlocation ", "").split(" ") for f in state if f.startswith("objectatlocation")]

        if len(objectatlocation) >= 1: 
            for object, location in objectatlocation:
                if location not in objectdic: #first time for this location 
                    objectdic[location] = [object]
                else: 
                    objectdic[location].append(object)

        if len(objectdic) > 1:
            description += "the objects are at locations as follows. "

        for location in objectdic:
            if len(objectdic[location]) == 1:
                description += f"{objectdic[location][0]} is at {location}. "
            elif len(objectdic[location]) > 1:
                description += f"{_list_to_string(objectdic[location])} are at {location}. "

        

        atlocation = [f.replace("atlocation ", "").split(" ") for f in state if f.startswith("atlocation")]
        if len(atlocation) >= 1: 
            for agent, location in atlocation:
                description += f"agent {agent} is at location {location}. "
 

        inreceptacledic = {}
        inreceptacle = [f.replace("inreceptacle ", "").split(" ") for f in state if f.startswith("inreceptacle")]

        if len(inreceptacle) >= 1: 
            for object, receptacle in inreceptacle:
                if receptacle not in inreceptacledic: #first time for this receptacle
                    inreceptacledic[receptacle] = [object]
                else: 
                    inreceptacledic[receptacle].append(object)

        if len(inreceptacledic) > 1:
            description += "The objects are in/on receptacle as follows. "

        for receptacle in inreceptacledic:
            p = self._get_on_in(receptacle)
            if len(inreceptacledic[receptacle]) == 1:
                description += f"{inreceptacledic[receptacle][0]} is {p} {receptacle}. "
            elif len(inreceptacledic[receptacle]) > 1:
                description += f"{_list_to_string(inreceptacledic[receptacle])} are {p} {receptacle}. "


        atomDic = {'closed': 'closed', 'isclean': 'clean', 'iscool': 'cool', 'checked': "checked", 'ishot': "hot", 'opened': 'open',  'istoggled':"toggled", 'issliced': "sliced", 'ison': "on", 'isoff': "off"}

        for predicate in atomDic:

            newlist = [f.replace(predicate + " ", "") for f in state if f.startswith(predicate)]
            
            if len(newlist) == 1:
                description += f"{_list_to_string(newlist)} is {atomDic[predicate]}. "
            if len(newlist) > 2:
                description += f"{_list_to_string(newlist)} are {atomDic[predicate]}. "


        atomValidate = {'pickandplace': "is in a receptacle of", 'examineinlight': "is examined under an object of", 
                        'cleanandplace':"is clean and is in a receptacle of", 
                        'heatandplace': "is hot and is in a receptacle of", 'coolandplace': 'is cool and is in a receptacle of'}
        

        validate = [f.replace("validate", "").split(" ") for f in state if f.startswith("validate")]
        if len(validate) > 1: 
            print("ERROR: more than one validate")
        elif len(validate) == 1:
            validateobjects = validate[0]
            if "examineinlight" in validateobjects[0]:
                description += f"It has been validated that an object of type {validateobjects[2]} {atomValidate[validateobjects[0]]} type {validateobjects[1]}. "
            elif "picktwoandplace" in validateobjects[0]:
                description += f"It has been validated that two objects of type {validateobjects[1]} are in a receptacle of type {validateobjects[2]}. "
            else:
                description += f"It has been validated that an object of type {validateobjects[1]} {atomValidate[validateobjects[0]]} type {validateobjects[2]}. "

        notvalidated = [f.replace("notvalidated", "").split(" ") for f in state if f.startswith("notvalidated")]
        if len(notvalidated) == 1: 
                            description += f"Nothing has been validated. "

        handempty = [f.replace("handempty ", "").split(" ") for f in state if f.startswith("handempty ")]
        if len(handempty) == 1:
            description += f"agent1's hands are empty. "
        elif len(handempty) > 1:
            description += f"ERROR: hands empty repeated. "
        elif len(handempty) == 0:           ##must be holding something
            holds = [f.replace("holds ", "").split(" ") for f in state if f.startswith("holds ")]
            if len(holds) > 1:
                print("ERROR: holding more than one object")
            elif len(holds) == 1:
                description += f"{holds[0][0]} is holding object {holds[0][1]}. "


 

        return description 
