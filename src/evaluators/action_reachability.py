from PDDL2NL.utils.tarski_utils import get_tarski_problem
from PDDL2NL.utils.pddl_utils import is_unsolvable_new_goal
from evaluators.base import BaseEvaluator

def get_preconditions(domain, problem, action):
    P = get_tarski_problem(domain, problem)
    # print(domain)
    # print(problem)
    assert P is not None
    a = P.get_action_or_none(action[1:-1])
    if a is None:
        return a
        
    pres = [f'({f})' for f in a.pres]

    return f'(and {" ".join(pres)})'

class ActionReachabilityEvaluator(BaseEvaluator):
    def get_score(self, ans, doc):

        real_answer = doc["answer"]
        # real_answer = [f'({x.strip().lower()})' for x in real_answer]
        # print(f'Real answer: {real_answer}')
        # print(f'Model answer: {ans}')
        if not real_answer or len(real_answer) == 0:
            # None
            self.add_scores(["none" == x.strip().lower() for x in ans])
            # print(f"EMPTY ANSWER {self.scores}")
            # if self.scores == [False]:
            #     print(f'===============> Model answer: {ans}')    
        else:
            for x in ans:
                # Need to run a planner
                action = x.strip().lower()
                if action in real_answer:
                    self.scores.append(True)
                    continue
                prec = get_preconditions(doc["PDDL_domain"].lower(), doc["PDDL_problem"].lower(), action)
                if prec is None:
                    self.scores.append(False)
                else:
                    # print(f'===============> PREC: {prec} of action {action}')
                    self.scores.append(is_unsolvable_new_goal(doc["PDDL_domain"].lower(), doc["PDDL_problem"].lower(), prec))

            # print(f"NONEMPTY ANSWER {self.scores}")



        return self.get_avg_score()
