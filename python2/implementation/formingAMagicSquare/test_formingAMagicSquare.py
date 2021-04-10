"""TDD Test Cases for formingAMagicSquare.py
"""

import unittest
from formingAMagicSquare import forming_a_magic_square
from formingAMagicSquare import rotate_square_90, reflect_square

class TestFormingAMagicSquare(unittest.TestCase):
    """Validate the minimum difference required to transform input
    into a magic square
    """
    def test_hackerrank_sample1(self):
        """Validate provided sample
        """
        result = forming_a_magic_square([[5, 3, 4], [1, 5, 8], [6, 4, 2]])
        self.assertEquals(result, 7)

    def test_hackerrank_sample2(self):
        """Validate provided sample
        """
        result = forming_a_magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 5]])
        self.assertEquals(result, 1)

    def test_hackerrank_sample3(self):
        """Validate provided sample
        """
        result = forming_a_magic_square([[4, 8, 2], [4, 5, 7], [6, 1, 6]])
        self.assertEquals(result, 4)

    def test_rotate(self):
        """Test rotation of a square matrix
        """
        result = rotate_square_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEquals(result, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_reflect(self):
        """Test reflection of a square matrix
        """
        result = reflect_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEquals(result, [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

if __name__ == '__main__':
    unittest.main(exit=False)
