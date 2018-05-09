"""TDD Test Cases for pickingNumbers.py
"""

import unittest
from pickingNumbers import picking_numbers

class TestPickingNumbers(unittest.TestCase):
    """Validate max number of digits with a difference of less than 2
    """
    def test_hackerrank_sample1(self):
        """Validate provided test case
        """
        result = picking_numbers([4, 6, 5, 3, 3, 1])
        self.assertEquals(result, 3)

    def test_hackerrank_sample2(self):
        """Validate provided test case
        """
        result = picking_numbers([1, 2, 2, 3, 1, 2])
        self.assertEquals(result, 5)

    def test_set_same_numbers(self):
        """Validate provided test case
        """
        result = picking_numbers([1, 1, 1, 1, 1])
        self.assertEquals(result, 5)

if __name__ == '__main__':
    unittest.main(exit=False)
