from evaluators.base import BaseEvaluator

# from pddl.logic import Predicate, constants, variables
# from pddl.core import Domain, Problem
# from pddl.parser.domain import DomainParser
# from pddl.parser.problem import ProblemParser

# from pddl.action import Action
# from pddl.requirements import Requirements


class LandmarksEvaluator(BaseEvaluator):
    def get_score(self, ans, doc):
        # Updated version: the questions are generated only for cases where all atoms are either 
        # in state, goal, landmarks, or non-landmarks sets
        real_answer = doc["answer"]
        real_answer_yes = [a.lower() for a in real_answer["yes"]]
        real_answer_no = [a.lower() for a in real_answer["no"]]

        # print(real_answer_yes)
        if "(dummy val1)" in real_answer_yes:
            return 0
        # real_answer_maybe = [a.lower() for a in real_answer["maybe"]]
        # print(f'Real answer: yes: {real_answer_yes},   no: {real_answer_no}')
        # print(f'Model answer: {ans}')
        for x in ans:
            if x.strip().lower() in real_answer_yes:
                self.scores.append(True)
            elif x.strip().lower() == "none":
                self.scores.append(len(real_answer_yes) == 0)
            else:
                self.scores.append(False)
                
        return self.get_avg_score()
