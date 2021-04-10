"""TDD Test Cases for breakingTheRecords.py
"""

import unittest
from breakingTheRecords import breaking_the_records

class TestBreakingTheRecords(unittest.TestCase):
    """Validate the frequency of (high and low) record breaks
    """
    def test_hackerrank_sample(self):
        """Validate provided inputs
        """
        result = breaking_the_records([10, 5, 20, 20, 4, 5, 2, 25, 1])
        self.assertEquals(result, [2, 4])

    def test_hackerrank_sample2(self):
        """Validate provided inputs
        """
        result = breaking_the_records([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
        self.assertEquals(result, [4, 0])

    def test_one_score(self):
        """Validate provided inputs
        """
        result = breaking_the_records([100000000])
        self.assertEquals(result, [0, 0])

    def test_same_scores(self):
        """Validate provided inputs
        """
        result = breaking_the_records([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEquals(result, [0, 0])

if __name__ == '__main__':
    unittest.main(exit=False)
