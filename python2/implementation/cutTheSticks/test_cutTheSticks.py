"""TDD Test Cases for cutTheSticks.py
"""

import unittest
from cutTheSticks import cut_the_sticks

class TestCutTheSticks(unittest.TestCase):
    """Validate number of sticks cut at each iteration.
    """
    def test_hackerrank_sample1(self):
        """Validate provided test case.
        """
        result = cut_the_sticks([5, 4, 4, 2, 2, 8])
        self.assertEquals(result, [6, 4, 2, 1])

    def test_hackerrank_sample2(self):
        """Validate provided test case.
        """
        result = cut_the_sticks([1, 2, 3, 4, 3, 3, 2, 1])
        self.assertEquals(result, [8, 6, 4, 1])

if __name__ == '__main__':
    unittest.main(exit=False)
