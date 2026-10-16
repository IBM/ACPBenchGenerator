from PDDL2NL.utils.pddl_utils import is_unsolvable_new_goal
from PDDL2NL.utils.tarski_utils import get_tarski_problem
from PDDL2NL.utils.tarskilite import get_atoms_pddl, get_positive_preds
from evaluators.base import BaseEvaluator
from pddl import parse_domain, parse_problem
from pddl.logic import Predicate, constants, variables
from pddl.core import Domain, Problem
# from pddl.parser.domain import DomainParser
# from pddl.parser.problem import ProblemParser

from pddl.action import Action
from pddl.requirements import Requirements


def create_all_atoms_reachable_check_task(domain, problem):
    # TODO: Fix this transformation - need to be able to restart
    # Adding an extra predicate for each predicate. 
    # If the predicate is added by the action, we add it to the effect.
    # We replace the goal by conjunction over the new predicates.

    Prob = get_tarski_problem(domain, problem)
    if Prob is None:
        return None, None

    d = parse_domain(domain)
    p = parse_problem(problem)

    extra_predicates = {}
    for p in d.predicates:
        ep = Predicate(f"X__achieved__{p.name}", *p.terms)
        extra_predicates[p.name] = ep

    reachable = Prob.compute_reachable_facts()
    goal = get_atoms_pddl(d, p, reachable)
    extended_goal = []
    for g in goal:
        eg = extra_predicates[g.name]
        extended_goal.append(eg(*g.terms))

    actions = []
    for a in d.actions:
        pos_effs = get_positive_preds(a.effect)
        if len(pos_effs) > 0:
            extra_pos_effs = [extra_predicates[x.name] for x in pos_effs]
            b =  Action(a.name, parameters=a.parameters,
                                precondition=a.precondition,
                                effect=a.effect & extra_pos_effs)
            actions.append(b)
        else:
            actions.append(a)

    # define the domain object.
    requirements = [Requirements.TYPING, Requirements.ADL]
    new_d = Domain(d.name,
                requirements=requirements,
                types=d.types,
                constants=d.constants,
                predicates=list(d.predicates) + list(extra_predicates.values()),
                actions=actions)
    new_p = Problem(p.name, domain=new_d,
                    requirements=requirements,
                    objects=p.objects,
                    init=p.init,
                    goal=extended_goal)

    return new_d, new_p


def check_all_atoms_reachable(domain, problem):
    # TODO: create transformation, check if solvable
    return None




class ReachabilityEvaluator(BaseEvaluator):
    def get_score(self, ans, doc):
        real_answer = doc["answer"]
        real_answer = [f'({x.strip().lower()})' for x in real_answer]

        # if len(real_answer) == 0 and any(["none" == x.strip().lower() for x in ans]):
        #     # At least one answer is none and we don't have any evidence
        #     # Checking if all propositions are reachable by translation and planning
        #     # If not, getting unreachable
        #     unreachable_atoms = check_all_atoms_reachable(doc["PDDL_domain"], doc["PDDL_problem"])
        #     if unreachable_atoms is not None:
        #         real_answer = unreachable_atoms

        if len(real_answer) == 0:
            # None
            self.add_scores(["none" == x.strip().lower() for x in ans])
            # print(f"EMPTY ANSWER {self.scores}")
            # if scores == [False]:
            #     print(f'===============> Model answer: {ans}')    
        else:
            for x in ans:
                if x.strip().lower() in real_answer:
                    # print("No need to run the planner")
                    self.scores.append(True)
                    # print(f'===============> Model answer: {ans}')
                    # print(f'===============> Real answer: {real_answer}')
                else:
                    # Need to run a planner
                    # print("Need to run the planner")
                    atom = x.strip().lower()
                    self.scores.append(is_unsolvable_new_goal(doc["PDDL_domain"].lower(), doc["PDDL_problem"].lower(), atom))

            # print(f"NONEMPTY ANSWER {self.scores}")

        return self.get_avg_score()
