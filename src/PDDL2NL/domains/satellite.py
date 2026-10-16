from PDDL2NL.utils.translation_util import ProblemTranslator, _is_are
from collections import defaultdict 

class SatelliteTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        return  "This domain consists of satellite(s) equipped with various instruments that can be switched on when the power is available. Each instrument has a calibration target object and supports taking images of objects in particular modes. When the instrument power is switched on, it is not calibrated. To calibrate an instrument, the satellite should point to the calibration target object and the instrument should be powered on.  To take an image of an object, the satellite must point to that object and the instrument must be calibrated."
    
    def get_objects_description(self, P):
        satellite_type = [i for i in P.problem.language.sorts if i.name=='satellite'][0]
        description = f"There {_is_are(satellite_type.cardinality())} {satellite_type.cardinality()} satellite(s), numbered consecutively. "
        # description += ", ".join([i.name for i in satellite_type.domain()])+ ". "
        direction_type = [i for i in P.problem.language.sorts if i.name=='direction'][0]
        description += f"There {_is_are(direction_type.cardinality())} {direction_type.cardinality()} possible target object(s): "
        description += ", ".join([i.name for i in direction_type.domain()])+ ". "
        mode_type = [i for i in P.problem.language.sorts if i.name=='mode'][0]
        description += f"There {_is_are(mode_type.cardinality())} {mode_type.cardinality()} image mode(s): "
        description += ", ".join([i.name for i in mode_type.domain()]) + ". "
        instrument_type = [i for i in P.problem.language.sorts if i.name=='instrument'][0]
        description += f"There {_is_are(mode_type.cardinality())} {instrument_type.cardinality()} instrument(s), numbered consecutively. "
        # description += ", ".join([i.name for i in instrument_type.domain()])+ ". "
        return description
        
    def get_static_atoms_description(self, P):
        on_board_symbol = [i for i in P.static_symbols() if i.name == 'on_board'][0]
        on_board_items = defaultdict(list)
        for i in P.get_grounded_atoms(on_board_symbol):
            on_board_items[i.binding[1].name ].append(i.binding[0].name)
        description = ""
        for k, v in on_board_items.items():
            description += f"Satellite {k} has following instruments onboard: " + ", ".join(v) +". "
        calibration_target_symbol = [i for i in P.static_symbols() if i.name == 'calibration_target'][0]
        targets = {i.binding[0].name: i.binding[1].name for i in P.get_grounded_atoms(calibration_target_symbol)}
        
        supports_symbol = [i for i in P.static_symbols() if i.name == 'supports'][0]
        modes = {i.binding[0].name: i.binding[1].name for i in P.get_grounded_atoms(supports_symbol)}
        
        for key in modes.keys():
            description += f"Instrument {key} supports image of mode {modes[key]} and its calibration target is {targets[key]}. "
        return description
    
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        description = f"Currently, "
        if just_atoms:
            description = ""
        satellite_pointings = [f.replace("pointing ", "").split() for f in state if "pointing " in f]
        if len(satellite_pointings) > 0:
            description += ". ".join([f"Satellite {i[0]} is pointing to {i[1]}" for i in satellite_pointings]) +". "
        
        power_available = [f.replace("power_avail ", "") for f in state if "power_avail " in f]
        if len(power_available) > 0:
            description += "Power is available on the following satellite(s): " + f", ".join(power_available) + ". "
        
        power_inuse = [f.replace("power_on ", "") for f in state if "power_on " in f]
        if len(power_inuse) > 0:
            description += "Following instruments are powered on: " + f", ".join(power_inuse) + ". "
        
        calibrated = [f.replace("calibrated ", "") for f in state if "calibrated " in f]
        if len(calibrated) > 0:
            description += "Following instruments are calibrated: " + f", ".join(calibrated) + ". "
        
        image_mode = [f.replace("have_image ", "").split() for f in state if "have_image " in f]
        if len(image_mode) > 0:
            for i in image_mode:
                description += f"A {i[1]} mode image of target {i[0]} is available. "
                
        
        return description