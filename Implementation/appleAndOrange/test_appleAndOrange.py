"""TDD Test Cases for appleAndOrange.py
"""

import unittest
from appleAndOrange import apple_and_orange

class TestAppleAndOrange(unittest.TestCase):
    """Test apple_and_orange to see if fruit lands on house
    """
    def test_hackerrank_sample(self):
        """Test given sample input
        """
        result = apple_and_orange([7, 11], [5, 15], [-2, 2, 1], [5, -6])
        self.assertEquals(result, [1, 1])

    def test_slim_house(self):
        """Test opportunity of slim house
           Failing Test case. However, situation doesn't happen
        """
        result = apple_and_orange([10, 10], [5, 15], [-2, 2, 1], [5, -6])
        self.assertEquals(result, [0, 1])

if __name__ == '__main__':
    unittest.main(exit=False)
