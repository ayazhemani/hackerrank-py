"""TDD Test Cases for plusMinus.py
"""

import unittest
from plusMinus import plus_minus

class TestPlusMinus(unittest.TestCase):
    """Test cases to validate positive, negative, and zero integers in an array.
    """
    def test_hackerrank_sample(self):
        """Validate provided test case
        """
        result = plus_minus(6, [-4, 3, -9, 0, 4, 1])
        self.assertEquals(result, ['0.500000', '0.333333', '0.166667'])

    def test_all_negative_numbers(self):
        """Validate all negative numbers
        """
        result = plus_minus(6, [-4, -3, -9, -10, -4, -1])
        self.assertEquals(result, ['0.000000', '1.000000', '0.000000'])

    def test_all_zero_numbers(self):
        """Validate all zero numbers
        """
        result = plus_minus(7, [0, 0, 0, 0, 0, 0, 0])
        self.assertEquals(result, ['0.000000', '0.000000', '1.000000'])

    def test_all_positive_numbers(self):
        """Validate all positive numbers
        """
        result = plus_minus(5, [4, 3, 9, 4, 1])
        self.assertEquals(result, ['1.000000', '0.000000', '0.000000'])

    def test_no_numbers(self):
        """Validate all positive numbers
        """
        result = plus_minus(0, [])
        self.assertEquals(result, ['0.000000', '0.000000', '0.000000'])

if __name__ == '__main__':
    unittest.main(exit=False)
