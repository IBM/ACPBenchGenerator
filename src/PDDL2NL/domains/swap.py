from PDDL2NL.utils.translation_util import ProblemTranslator, _is_are, _list_to_string
import random 

class SwapTranslator(ProblemTranslator):
    
    def get_domain_description(self):
        return "This is a swap domain where agents are swapping items or roles. Each agent is always assigned a single item/role."
    # The goal is to obtain desired items/roles assigned."   
    
    def get_objects_description(self, P):
        agent_type = [i for i in P.problem.language.sorts if i.name=='agent'][0]
        role_type = [i for i in P.problem.language.sorts if i.name=='role'][0]
        agents = [x.name for x in agent_type.domain()]
        roles = [x.name for x in role_type.domain()]
        
        description = f"There {_is_are(agent_type.cardinality())} {agent_type.cardinality()} agents: {_list_to_string(agents)}. There {_is_are(role_type.cardinality())} {role_type.cardinality()} items/roles: {_list_to_string(roles)}."
        return description


    def get_static_atoms_description(self, P):
        return ""
        
    def get_fluent_atoms_description(self, P, state, just_atoms=False):
        description = "Currently, "
        if just_atoms:
            description = ""
  
        assigned = [f.replace("assigned ", "").split(" ") for f in state if f.startswith("assigned")]
        if len(assigned) > 0:
            assigned_desc = [f"{a[0]} is assigned {a[1]}" for a in assigned ]
            description += _list_to_string(assigned_desc) + "."
        return description 
   
    def get_negated_atom_description(self, P, grounded_atom):
        if 'assigned' in grounded_atom:
            items=grounded_atom.split()[1:]
            templates = ["{agent} is not assigned {role}",]
            return random.choice(templates).format(role=items[1], agent=items[0])
        else:
            raise NotImplementedError
   