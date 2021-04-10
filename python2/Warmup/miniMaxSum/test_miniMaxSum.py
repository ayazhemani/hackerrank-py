"""TDD Test Cases for miniMaxSum.py
"""

import unittest
from miniMaxSum import mini_max_sum

class TestMiniMaxSum(unittest.TestCase):
    """Validate sum of top and bottom 4 integers
    """
    def test_hackerrank_sample(self):
        """Validate sample set
        """
        result = mini_max_sum([1, 2, 3, 4, 5])
        self.assertEquals(result, (10, 14))

    def test_zero_data(self):
        """Validate sample set of zeros
        """
        result = mini_max_sum([0, 0, 0, 0, 0])
        self.assertEquals(result, (0, 0))

    def test_big_data(self):
        """Validate sample set of zeros
        """
        result = mini_max_sum([999999, 99999, 9999999, 9999, 9999999])
        self.assertEquals(result, (11109996, 21099996))

if __name__ == '__main__':
    unittest.main(exit=False)
