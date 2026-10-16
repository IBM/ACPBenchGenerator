import tempfile
from PDDL2NL.utils.tarski_utils import generate_optimal_plans_for_problem_state
from PDDL2NL.utils.translation_util import get_pddl_domain
from evaluators.base import BaseEvaluator
from PDDL2NL.utils import tarskilite as tl



def is_on_optimal_plan(domain, problem, action, opt):
    with tempfile.NamedTemporaryFile() as domain_temp, \
         tempfile.NamedTemporaryFile() as problem_temp:
        if "logistics" in str(domain):
            domain = get_pddl_domain("logistics")
        if "depot" in str(domain):
            domain = get_pddl_domain("depot")

        with open(str(domain_temp.name), 'w', encoding='utf8') as file:
            file.write(domain.lower())
        with open(str(problem_temp.name), 'w', encoding='utf8') as file:
            file.write(problem.lower())

        # Here, we need to keep the temp files live until the end of the function
        try:
            P = tl.STRIPS(str(domain_temp.name), str(problem_temp.name))
        except Exception as e:
            # Unsolvable
            return False

        a = P.get_action_or_none(action[1:-1])
        if a is None:
            return False
        state = P.init
        next_state = tl.progress(state, a)
        if opt is None:
            # Get an optimal plan cost
            # print("Getting an optimal plan cost")
            plans = generate_optimal_plans_for_problem_state(P, state, num_plans=1, timeout=5)
            # print(plans)
            opt = len(plans[0]["actions"])
            # print(f"Optimal plan cost found: {opt}")
        else:
            # print(f"Optimal plan cost is known: {opt}")
            opt = int(opt)    

        # print("Getting an optimal plan for the next state")
        next_plans = generate_optimal_plans_for_problem_state(P, next_state, num_plans=1, timeout=5)
        # print(next_plans)
        if next_plans is None:
            return False
        next_opt = len(next_plans[0]["actions"])
        # if next_opt + 1 == opt:
        #     print(f"Current state value is {opt}, next state value is {next_opt}")
        return next_opt + 1 == opt
    


class NextActionEvaluator(BaseEvaluator):
    def get_score(self, ans, doc):

        real_answer = doc["answer"]
        real_answer_yes = [a.lower() for a in real_answer["yes"]]
        real_answer_no = [a.lower() for a in real_answer["no"]]
        real_answer_maybe = [a.lower() for a in real_answer["maybe"]]
        opt = real_answer.get("opt", None)
        # print(f'Real answer: yes: {real_answer_yes},   no: {real_answer_no},    maybe: {real_answer_maybe}')
        # print(f'Model answer: {ans}')
        for x in ans:
            # print(f'Model answer {x.strip().lower()}')
            if x.strip().lower() in real_answer_yes:
                # print(f"Next action is in the set: {x}")
                self.scores.append(True)
            elif x.strip().lower() in real_answer_no:
                # applicable, not towards goal
                self.scores.append(False)
            elif x.strip().lower() not in real_answer_maybe:
                # Not applicable
                self.scores.append(False)
            else:                
                # Need to run a planner
                action = x.strip().lower()
                # print("Running a planner")
                self.scores.append(is_on_optimal_plan(doc["PDDL_domain"].lower(), doc["PDDL_problem"].lower(), action, opt))

            # print(f"NONEMPTY ANSWER {scores}")



        return self.get_avg_score()
