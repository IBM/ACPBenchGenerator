
from IPython.display import Markdown, display
from ipywidgets import Label, Checkbox, Button, HBox, VBox, Layout
from tarski.io import PDDLReader
import json 
import ipywidgets as wid
from utils.logging_util import create_exp_name
import os 

class ActionTemplateAnnotation:
    def __init__(self, domain, action_variations_folder,  user ):
        self.user=user
        unique_id = create_exp_name(f"{domain}_{user}", os.getpid())
        self.results_file = f"{action_variations_folder}/results/{unique_id}.jsonl"
        action_templates_file=f"{action_variations_folder}/action_templates.json"
        self.domain = domain 
        self.action_templates=json.load(open(action_templates_file))[self.domain]
        reader = PDDLReader(raise_on_error=True)
        reader.parse_domain(f"/data/planning_datasets/autoplanbench/data/{self.domain}/domain.pddl")
        self.pddl_problem = reader.parse_instance(f"/data/planning_datasets/autoplanbench/data/{self.domain}/adapted_instances/instance-1.pddl")
        self.action_idx = 0
        self.i = 0
        self.actions = list(self.pddl_problem.actions.keys())
    
    def log_annotation(self, action, annotations):
        output_dict = {"domain": self.domain, "user":self.user,"action":action,"annotation":[]}
        for i, model in enumerate(self.action_templates[action].keys()):
            template =  self.action_templates[action][model]
            assert annotations[i].description == f"{template} ({model})"
            output_dict['annotation'].append((model, template, annotations[i].value))
        with open(self.results_file, 'a') as outfile:
            json.dump(output_dict, outfile)
            outfile.write('\n')
        # display(Markdown(f"Your annotations are logged in following file: {self.results_file}"))
            
            
        
    def next_action(self):
        if self.i >= len(self.actions):
            display(Markdown(f"### All actions were for {self.domain} domain were annotated. You may select another domain and start again."))
            return
        self.print_action_info(self.actions[self.i])
        action = self.actions[self.i].lower()
        a_box = [Checkbox(description=f"{template} ({model})", layout=Layout(width='1500px'),style={"description_width":"0px"},) for model, template in self.action_templates[action].items()]
        ui  = VBox(a_box)
        display(ui)
        def on_click(button):
            # selected_options = [widget.description for widget in ui.children if widget.value]
            self.log_annotation(action, ui.children)
            # text.description = selected_options
            button.description = f'Thanks'
            button.disabled = True
            self.i += 1
            # display(Markdown(f"### Rerun `ata.next_action()` to annotate next action."))
            
        button = Button(description="Save")
        button.on_click(on_click)
        display(wid.HBox([button]))
        return action

    def suggest_template(self, action, template):
        output_dict = {"domain": self.domain, "user":self.user,"action":action,"annotation":[("manual", template, True)]}
        with open(self.results_file, 'a') as outfile:
            json.dump(output_dict, outfile)
            outfile.write('\n')
        display(Markdown(f"Your suggested template for {action} was logged in following file: {self.results_file}"))
        
                
        
        
        
    def print_action_info(self, action):
        header=f"#### Domain: {self.domain}\n"
        header+=f"#### Action: {action}\n"
        header+=f"\nparameters: `{str(self.pddl_problem.get_action(action))}`\n"
        header+=f"\nprecondition: `{str(self.pddl_problem.get_action(action).precondition)}` \n"
        header+=f"\neffect: `{str(self.pddl_problem.get_action(action).effects)}` \n\n\n"
        header+="Now select the descriptions that best match the action"
        display(Markdown(header))