"""TDD Test Cases for jumpingOnTheClouds.py
"""

import unittest
from jumpingOnTheClouds import jumping_on_the_clouds

class TestJumpingOnTheClouds(unittest.TestCase):
    """Validate number of jumps required to traverse clouds.
    """
    def test_hackerrank_sample1(self):
        """Validate provided test case.
        """
        result = jumping_on_the_clouds([0, 0, 1, 0, 0, 1, 0])
        self.assertEquals(result, 4)

    def test_hackerrank_sample2(self):
        """Validate provided test case.
        """
        result = jumping_on_the_clouds([0, 0, 0, 0, 1, 0])
        self.assertEquals(result, 3)

    def test_hackerrank_sample3(self):
        """Validate provided test case.
        """
        result = jumping_on_the_clouds([0, 0, 1, 0, 0, 1, 0])
        self.assertEquals(result, 4)

if __name__ == '__main__':
    unittest.main(exit=False)
