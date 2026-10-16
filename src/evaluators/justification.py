from PDDL2NL.utils.tarski_utils import get_tarski_problem
from evaluators.base import BaseEvaluator, fix_action_name
from PDDL2NL.utils import tarskilite as tl


def is_subsequence(plan, new_plan):
    i = 0
    for a in plan:
        if a == new_plan[i]:
            i+=1
            if len(new_plan) == i:
                # Done
                return True
    return False

def is_plan(id, domain, problem, new_plan):
    P = get_tarski_problem(domain, problem)
    if P is None:
        # Unsolvable
        return False
    # Check if new_plan is a plan

    current_state = P.init
    for action in new_plan:
        applicable_actions = P.get_applicable_actions(current_state)
        app_actions_list = [f'({a.name.lower()})' for a in applicable_actions]
        if action.lower() not in app_actions_list:
            return False
        # assert action.lower() in app_actions_list, f"{action} is not in {app_actions_list}"
        a = applicable_actions[app_actions_list.index(action.lower())]
        current_state = tl.progress(current_state, a)
    return tl.entails(current_state, P.goal)


def is_subsequence_and_plan(id, domain, problem, plan, new_plan):
    if len(plan) <= len(new_plan):
        return False
    if not is_subsequence(plan, new_plan):
        return False
    return is_plan(id, domain, problem, new_plan)


class JustificationEvaluator(BaseEvaluator):
    def get_score(self, ans, doc):

        real_answer = doc["answer"]
        # print(f'Answer {ans}')
        # for a in ans:
        #     ind = int(a[-1])
        #     a = a[:-1]
        #     print(f'Answer {a}, index {ind}')

        id = doc["id"]
        seq = doc["inputs"][19:-147]
        # print(doc["inputs"])
        # print(f'#{seq}#')
        seq = seq.replace(") (", ")######(").split("######")
        # print(f'Original plan: {seq}')
        # print(f'Original plan length: {len(seq)}')
        for x in ans:
            x = [fix_action_name(a) for a in x]
            if len(x) == 0:
                # Wrong answer - never an empty sequence
                self.scores.append(0)
                continue
            # print(f'Reduced plan: {x}')
            # print(f'Reduced plan length: {len(x)}')
            # seq_x = x.replace(") (", ")######(").split("######")
            # print(f'Reduced plan: {seq_x}')
            self.scores.append(is_subsequence_and_plan(id, doc["PDDL_domain"].lower(), doc["PDDL_problem"].lower(), seq, x))




        return self.get_avg_score()
