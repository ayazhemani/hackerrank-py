"""TDD Test Cases for leftRotation.py
"""

import unittest
from leftRotation import rotate_array

class TestLeftRotation(unittest.TestCase):
    """Description
    """
    def test_sample(self):
        """Description
        """
        result = rotate_array([1, 2, 3, 4, 5], 4)
        self.assertEquals(result, [5, 1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main(exit=False)
