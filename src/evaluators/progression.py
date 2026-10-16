from evaluators.base import BaseEvaluator, cleanup_answer, set_equal


class ProgressionEvaluator(BaseEvaluator):
    def get_score(self, ans, doc):
        real_answer = doc["answer"]
        real_answer_pos = [a.lower() for a in real_answer["pos"]]
        real_answer_neg = [a.lower() for a in real_answer["neg"]]
        # print(f'Real answer: {real_answer_pos}, {real_answer_neg}')
        # print(f'Model answer: {ans}')

        # self.scores = [jaccard_similarity(real_answer, cleanup_answer(x)) for x in ans]
        for x in ans:
            if len(x) > 2 or len(x) < 1:
                self.scores.append(False)
                # print(f'Real answer: {real_answer_pos}, {real_answer_neg}')
                # print(f'Wrong number of elements in the list: {x}')
            else:
                p = cleanup_answer(x[0])
                if len(x) == 2:
                    n = cleanup_answer(x[1])
                else:
                    # Assuming the last is dropped because it is empty
                    n = []
                ans = [set_equal(real_answer_pos, p), set_equal(real_answer_neg, n)]
                # print(f'positive: real {real_answer_pos}, answer {p}, score {int(all(ans))}')
                # print(f'negative: real {real_answer_neg}, answer {n}, score {int(all(ans))}')
                self.scores.append(all(ans))

        return self.get_avg_score()
