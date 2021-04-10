"""TDD Test Cases for divisibleSumPairs.py
"""

import unittest
from divisibleSumPairs import divisible_sum_pairs

class TestDivisibleSumPairs(unittest.TestCase):
    """Validate permutations count where sum of any two integers is divisible
    """
    def test_hackerrank_sample(self):
        """Validate provided test case
        """
        result = divisible_sum_pairs(3, [1, 3, 2, 6, 1, 2])
        self.assertEquals(result, 5)

    def test_one_pair(self):
        """Validate test where one valid pair of candidate numbers
        """
        result = divisible_sum_pairs(4, [1, 3])
        self.assertEquals(result, 1)

    def test_no_pairs(self):
        """Validate test where no valid pairs of candidate numbers
        """
        result = divisible_sum_pairs(10, [1, 3, 2, 6, 1, 2])
        self.assertEquals(result, 0)

if __name__ == '__main__':
    unittest.main(exit=False)
