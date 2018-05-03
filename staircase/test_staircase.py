"""TDD Test Cases for staircase.py
"""

import unittest
from staircase import staircase

class TestStaircase(unittest.TestCase):
    """Validate staircase tests
    """
    def test_hackerrank_sample(self):
        """Validate staircase of 6 steps
        """
        result = staircase(6)
        self.assertEquals(result, ['     #',
                                   '    ##',
                                   '   ###',
                                   '  ####',
                                   ' #####',
                                   '######'])

    def test_no_input(self):
        """Validate staircase of 0 steps
        """
        result = staircase(0)
        self.assertEquals(result, [])

    def test_neg_steps(self):
        """Validate staircase of -1 steps
        """
        result = staircase(-1)
        self.assertEquals(result, [])

if __name__ == '__main__':
    unittest.main(exit=False)
