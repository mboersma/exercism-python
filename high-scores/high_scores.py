"""MAnage a game player's High Score list."""


class HighScores(object):
    """Reports the latest, best, and top three scores of those given."""

    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        """Return the latest entry in the scores."""
        return self.scores[-1]

    def personal_best(self):
        """Return the largest entry in the scores."""
        return max(self.scores)

    def personal_top_three(self):
        """Return the top three entries in the scores, highest to lowest."""
        return sorted(self.scores, reverse=True)[:3]
