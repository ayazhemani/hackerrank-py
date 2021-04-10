"""TDD Test Cases for theHurdleRace.py
"""

import unittest
from theHurdleRace import the_hurdle_race

class TestTheHurdleRace(unittest.TestCase):
    """Validate the number of potions required to jump the max height
    """
    def test_hackerrank_sample1(self):
        """Test provided use case
        """
        result = the_hurdle_race([1, 6, 3, 5, 2], 4)
        self.assertEquals(result, 2)

    def test_hackerrank_sample2(self):
        """Test provided use case
        """
        result = the_hurdle_race([2, 5, 4, 5, 2], 7)
        self.assertEquals(result, 0)

if __name__ == '__main__':
    unittest.main(exit=False)
