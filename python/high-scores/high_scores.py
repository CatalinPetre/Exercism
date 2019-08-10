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
        while i < 2:
            maxim = max(self.scores)
            element = self.scores.remove(maxim)
            max_scores = max_scores + element
        return max_scores


   # def __repr__(self):
        # return self.scores    
# player_1 = HighScores()
# Cat = HighScores([1, 2, 10, 3])
# Cat.highest_score()
# Cat.latest()
# print("???")
