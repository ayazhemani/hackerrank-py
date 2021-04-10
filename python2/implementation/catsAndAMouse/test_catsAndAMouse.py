"""TDD Test Cases for catsAndAMouse.py
"""

import unittest
from catsAndAMouse import cats_and_a_mouse

class TestCatsAndAMouse(unittest.TestCase):
    """Validate the winner of the cat/mouse fight
    """
    def test_hackerrank_sample1(self):
        """Validate provided test case
        """
        result = cats_and_a_mouse([1, 2, 3])
        self.assertEquals(result, 'Cat B')

    def test_hackerrank_sample2(self):
        """Validate provided test case
        """
        result = cats_and_a_mouse([1, 3, 2])
        self.assertEquals(result, 'Mouse C')

if __name__ == '__main__':
    unittest.main(exit=False)
