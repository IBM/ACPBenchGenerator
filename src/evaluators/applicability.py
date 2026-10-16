from evaluators.base import BaseEvaluator, cleanup_answer, fix_action_name, jaccard_similarity, set_equal, skewed_jaccard_similarity


class ApplicabilityEvaluator(BaseEvaluator):
    def get_score(self, ans, doc):
        real_answer = doc["answer"]
        real_answer = [a.lower() for a in real_answer]
        ans = [[fix_action_name(a) for a in x] for x in ans]
        # print(f'Real answer: {real_answer}')
        # print(f'Model answer: {ans}')

        scores = [skewed_jaccard_similarity(real_answer, cleanup_answer(x)) for x in ans]
        avg = sum(scores)/len(scores)
        if avg > 0.0:
            print(f"Skewed score: {avg}")
        # Changed to exact answer
        self.add_scores([set_equal(real_answer, cleanup_answer(x)) for x in ans])
        # self.add_scores([jaccard_similarity(real_answer, cleanup_answer(x)) for x in ans])
        return self.get_avg_score()

