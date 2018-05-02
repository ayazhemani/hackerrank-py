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
            Difference = 15
        """
        result = diagonal_difference(3, [[11, 2, 4], [4, 5, 6],
                                         [10, 8, -12]])
        self.assertEquals(result, 15)

if __name__ == '__main__':
    unittest.main(exit=False)
