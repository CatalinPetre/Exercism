class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top_three(self):
        max_scores = []
        i = 0
        length = len(self.scores)
        while i < length and i < 3:
            maxim = max(self.scores)
            self.scores.remove(maxim)
            max_scores.append(maxim)
            i = i + 1
        return max_scores
