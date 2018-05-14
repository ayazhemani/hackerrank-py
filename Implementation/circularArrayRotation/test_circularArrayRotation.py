"""TDD Test Cases for circularArryaRotation.py
"""

import unittest
from circularArrayRotation import circular_array_rotation

class TestCircularArrayRotation(unittest.TestCase):
    """Validate the correct right rotated array
    """
    def test_hackerrank_sample1(self):
        """Validate provided test case
        """
        result = circular_array_rotation([1, 2, 3], 2)
        self.assertEquals(result, [2, 3, 1])

    def test_no_rotation(self):
        """Validate correct zero rotation
        """
        result = circular_array_rotation([1, 2, 3], 0)
        self.assertEquals(result, [1, 2, 3])

    def test_rotate_one(self):
        """Validate correct one unit rotation
        """
        result = circular_array_rotation([1, 2, 3], 1)
        self.assertEquals(result, [3, 1, 2])

if __name__ == '__main__':
    unittest.main(exit=False)
