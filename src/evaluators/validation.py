from evaluators.base import BaseEvaluator


class ValidationEvaluator(BaseEvaluator):
    def get_score(self, ans, doc):

        seq_index = int(doc["answer"])
        # seq = doc["inputs"][72:][:-2]
        # print(doc["inputs"])
        # print(f'#{seq}#')
        # seq = seq.replace(") (", ")######(").split("######")
        assert(seq_index>= -1)
        # assert(seq_index < len(seq))
        if seq_index == -1:
            real_answer = "None"
        else:
            real_answer = str(seq_index)
            # real_answer = seq[seq_index].strip()

        if real_answer.isnumeric():
            
            scores = [abs(int(real_answer) - int(x.strip().lower())) for x in ans]
            avg = sum(scores)/len(scores)
            if avg > 0.0:
                print(f"Distance from the right index: {avg}")

        self.add_scores([real_answer.lower() == x.strip().lower() for x in ans])

        return self.get_avg_score()
