"""TDD Test Cases for findDigits.py
"""

import unittest
from findDigits import find_digits

class TestFindDigits(unittest.TestCase):
    """Validate count of digits in number that are divisible.
    """
    def test_hackerrank_sample1(self):
        """Validate provided test case
        """
        result = find_digits(12)
        self.assertEquals(result, 2)

    def test_hackerrank_sample2(self):
        """Validate provided test case
        """
        result = find_digits(1012)
        self.assertEquals(result, 3)

if __name__ == '__main__':
    unittest.main(exit=False)
