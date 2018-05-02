"""TDD Test Cases for aVeryBigSum.py
"""

import unittest
from aVeryBigSum import a_very_big_sum

class TestAVeryBigSum(unittest.TestCase):
    """Test cases to validate aVeryBigSum.py
    """
    def test_hackerrank_input(self):
        """Test addition of 5 numbers
        1000000001 1000000002 1000000003 1000000004 1000000005
        Result: 5000000015
        """
        result = a_very_big_sum(5, [1000000001, 1000000002, 1000000003,
                                    1000000004, 1000000005])
        self.assertEqual(result, 5000000015)

    def test_sum_two_large_nums(self):
        """Test addition of 2 large numbers
        976987698768758 + 46546436436543 = 1023534135205301
        """
        result = a_very_big_sum(2, [976987698768758, 46546436436543])
        self.assertEqual(result, 1023534135205301)

    def test_sum_two_negative_nums(self):
        """Validate sum of two negative numbers
        (-77598566859887585) + (-435253245325432543) = (-512851812185320128)
        """
        result = a_very_big_sum(2, [-77598566859887585, -435253245325432543])
        self.assertEquals(result, -512851812185320128)

    def test_sum_nothing(self):
        """Validate sum of nothing
        """
        result = a_very_big_sum(0, [])
        self.assertEquals(result, 0)

if __name__ == '__main__':
    unittest.main(exit=False)
