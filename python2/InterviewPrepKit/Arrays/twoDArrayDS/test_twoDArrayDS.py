"""TDD Test Cases for twoDArrayDS.py
"""

import unittest
from twoDArrayDS import twoDArrayDS, sum_hourglass

class TestTwoDArrayDS(unittest.TestCase):
    """Description
    """
    def test_small_hourglass(self):
        """Description
        """
        result = sum_hourglass([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEquals(result, 35)

    def test_twoDArray(self):
        result = twoDArrayDS([[0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1],
                              [2, 2, 2, 2, 2, 2],
                              [3, 3, 3, 3, 3, 3],
                              [4, 4, 4, 4, 4, 4],
                              [5, 5, 5, 5, 5, 5]])
        self.assertEquals(result, 28)

    def hackerrank_sample(self):
        result = twoDArrayDS([[1, 1, 1, 0, 0, 0],
                              [0, 1, 0, 0, 0, 0],
                              [1, 1, 1, 0, 0, 0],
                              [0, 0, 2, 4, 4, 0],
                              [0, 0, 0, 2, 0, 0],
                              [0, 0, 1, 2, 4, 0]])
        self.assertEquals(result, 19)

if __name__ == '__main__':
    unittest.main(exit=False)
