"""TDD Test case for sherlockAndSquares.py
"""

import unittest
from sherlockAndSquares import sherlock_and_squares

class TestSherlockAndSquares(unittest.TestCase):
    """Validate the count of squares in the provided range.
    """
    def test_hackerrank_sample1(self):
        """Validate provided test case.
        """
        result = sherlock_and_squares([3, 9])
        self.assertEquals(result, 2)

    def test_hackerrank_sample2(self):
        """Validate provided test case.
        """
        result = sherlock_and_squares([17, 24])
        self.assertEquals(result, 0)

if __name__ == '__main__':
    unittest.main(exit=False)
