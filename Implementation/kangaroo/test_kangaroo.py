"""TDD Test Cases for kangaroo.py
"""

import unittest
from kangaroo import kangaroo

class TestKangaroo(unittest.TestCase):
    """Test if kangaroos will meet in the same x-plane location
    """
    def test_kangaroos_divorce(self):
        """Test case if kangaroos never converge on the same x location
        """
        result = kangaroo([0, 5], [2, 3])
        self.assertEquals(result, False)

    def test_kangaroos_meet(self):
        """Test case if kangaroos meet at a x-plane location
        """
        result = kangaroo([0, 4], [3, 2])
        self.assertEquals(result, True)

    def test_parallel_kangaroos(self):
        """Test case if kangaroos travel at the same rate
        """
        result = kangaroo([0, 4], [3, 3])
        self.assertEquals(result, False)

if __name__ == '__main__':
    unittest.main(exit=False)
