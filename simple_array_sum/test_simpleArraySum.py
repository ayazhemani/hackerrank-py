"""TDD Test Cases for simple_array_sum.py
"""

import unittest
from simpleArraySum import simple_array_sum

class TestSimpleArraySum(unittest.TestCase):
    """Test cases to validate simple_array_sum.
    """
    def test_hackerrank_inputs(self):
        """Verify correct sum of HackerRank Test
            1 + 2 + 3 + 4 + 10 + 11 = 31
        """
        result = simple_array_sum(6, [1, 2, 3, 4, 10, 11])
        self.assertEquals(result, 31)

    def test_add_nothing(self):
        """Test to accept no inputs.
        """
        result = simple_array_sum(0, [])
        self.assertEqual(result, 0)

    def test_add_two_ints(self):
        """Verify output for sum of 2 ints.
            8080 + 80808 = 88888
        """
        result = simple_array_sum(2, [8080, 80808])
        self.assertEquals(result, 88888)

    def test_add_five_ints(self):
        """Verify output for sum of 5 ints.
            1 + 2 + 3 + 5 + 8 = 19
        """
        result = simple_array_sum(5, [1, 2, 3, 5, 8])
        self.assertEquals(result, 19)

    def test_add_negative_ints(self):
        """Verify output for sum of 2 neg ints.
            (-22) + (-33) = (-55)
        """
        result = simple_array_sum(2, [-22, -33])
        self.assertEquals(result, -55)


if __name__ == '__main__':
    unittest.main(exit=False)
