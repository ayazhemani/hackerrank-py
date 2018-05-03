"""TDD Test Cases for diagonalDifference.py
"""

import unittest
from diagonalDifference import diagonal_difference

class TestDiagonalDifference(unittest.TestCase):
    """Test Cases to validate calulation of absolute diagonal differences
    """
    def test_hackerrank_sample(self):
        """Validate absolute difference of given matrix.
        [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
        Absolute Difference = 15
        """
        result = diagonal_difference(3, [[11, 2, 4], [4, 5, 6],
                                         [10, 8, -12]])
        self.assertEquals(result, 15)

    def test_no_matrix(self):
        """Validate matrix of length zero
        [[]]
        Absolute Difference = 0
        """
        result = diagonal_difference(0, [[]])
        self.assertEquals(result, 0)

    def test_neg_matrix(self):
        """Validate matrix of negative integers
        [[-11, -2, -4], [-4, -5, -6], [-10, -8, -12]]
        Absolute Difference = 9
        """
        result = diagonal_difference(3, [[-11, -2, -4],
                                         [-4, -5, -6],
                                         [-10, -8, -12]])
        self.assertEquals(result, 9)

    def test_5x5_matrix(self):
        """Validate matrix of length 5
        [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]
         Absolute Difference = 0
        """
        result = diagonal_difference(5, [[1, 2, 3, 4, 5],
                                         [6, 7, 8, 9, 10],
                                         [11, 12, 13, 14, 15],
                                         [16, 17, 18, 19, 20],
                                         [21, 22, 23, 24, 25]])
        self.assertEquals(result, 0)

if __name__ == '__main__':
    unittest.main(exit=False)
