"""TDD Test Cases for jumpingOnTheCloudsRevisited.py
"""

import unittest
from jumpingOnTheCloudsRevisited import jumping_on_the_clouds_revisited

class TestJumpingOnTheCloudsRevisited(unittest.TestCase):
    """Validate remaining energy
    """
    def test_sample(self):
        """Validate provided test case
        """
        result = jumping_on_the_clouds_revisited([0, 0, 1, 0, 0, 1, 1, 0], 2)
        self.assertEquals(result, 92)

if __name__ == '__main__':
    unittest.main(exit=False)
