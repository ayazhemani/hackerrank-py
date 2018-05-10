"""TDD Test Cases for climbingTheLeaderboard.py
"""

import unittest
from climbingTheLeaderboard import climbing_the_leaderboard

class TestClimbingTheLeaderboard(unittest.TestCase):
    """Description
    """
    def test_sample(self):
        """Description
        """
        result = climbing_the_leaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
        self.assertEquals(result, [6, 4, 2, 1])

    def test_tie_leaderboard(self):
        """Description
        """
        result = climbing_the_leaderboard([100, 100, 100], [100, 100, 100])
        self.assertEquals(result, [1, 1, 1])

    def test_sample1(self):
        """Description
        """
        result = climbing_the_leaderboard([100], [120])
        self.assertEquals(result, [1])

if __name__ == '__main__':
    unittest.main(exit=False)
