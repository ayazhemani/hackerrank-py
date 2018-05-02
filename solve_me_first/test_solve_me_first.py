"""TDD Test Cases for solve_me_first.py"""

import unittest
from solve_me_first import solveMeFirst

class TestSolveMeFirst(unittest.TestCase):
    """Test cases to validate SolveMeFirst"""

    def test_small_add(self):
        """Test 1 + 3 = 4"""
        result = solveMeFirst(1, 3)
        self.assertEqual(result, 4)

    def test_large_add(self):
        """Test 99999 + 11111 = 1000000"""
        result = solveMeFirst(99999, 11111)
        self.assertEqual(result, 111110)

if __name__ == '__main__':
    unittest.main(exit=False)
