from PDDL2NL.utils.translation_util import ProblemTranslator, _list_to_string, _is_are


class DepotTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        return "This is a depot domain, a combination of blocks and logistics. In this domain, trucks can transport crates, the crates can be stacked onto pallets using hoists."
    
    def get_objects_description(self, P):
        types = set([o.sort for o in P.problem.language.constants() ])
        ot = [f"{t.cardinality()} {t.name}s" for t in types ]
        return "There are " + ", ".join(ot)  + ", numbered consecutively."
    
    def get_static_atoms_description(self, P, just_atoms = False):
        return ""
    
    def get_fluent_atoms_description(self, P, state, just_atoms = False):
        description = "Currently, "
        if just_atoms:
            description = ""
        _clear = [f.split(" ")[1] for f in state if f.startswith("clear ")]
        if len(_clear) > 0:
            description += _list_to_string(_clear) + f" {_is_are(_clear)} clear; "

        _available = [f.split(" ")[1] for f in state if f.startswith("available ")]
        if len(_available) > 0:
            description += _list_to_string(_available) + f" {_is_are(_available)} available; "

        _at = [f'{f.split(" ")[1]} is at {f.split(" ")[2]}' for f in state if f.startswith("at ")]
        if len(_at) > 0:
            description += _list_to_string(_at) +"; "

        _on = [f'{f.split(" ")[1]} is on {f.split(" ")[2]}' for f in state if f.startswith("on ")]
        if len(_on) > 0:
            description += _list_to_string(_on) +"; "

        _in = [f'{f.split(" ")[1]} is in {f.split(" ")[2]}' for f in state if f.startswith("in ")]
        if len(_in) > 0:
            description += _list_to_string(_in) +"; "

        _lifting = [f'{f.split(" ")[1]} is lifting {f.split(" ")[2]}' for f in state if f.startswith("lifting ")]
        if len(_lifting) > 0:
            description += _list_to_string(_lifting) +"; "

        return description[:-2] + "."