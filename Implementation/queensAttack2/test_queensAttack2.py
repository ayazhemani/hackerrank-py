"""TDD Test Cases for queensAttack2.py
"""

import unittest
from queensAttack2 import queens_attack_2

class TestqueensAttack2(unittest.TestCase):
    """Description
    """
    def test_hackerrank_sample1(self):
        """Description
        """
        result = queens_attack_2(4, [4, 4], [])
        self.assertEquals(result, 9)

    def test_hackerrank_sample2(self):
        """Description
        """
        result = queens_attack_2(5, [4, 3], [[5, 5], [4, 2], [2, 3]])
        self.assertEquals(result, 10)

if __name__ == '__main__':
    unittest.main(exit=False)
