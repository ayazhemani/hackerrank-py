"""TDD Test Cases for countingValleys.py
"""

import unittest
from countingValleys import counting_valleys

class TestCountingValleys(unittest.TestCase):
    """Validate the number of valleys in a hike
    """
    def test_hackerrank_sample(self):
        """Validate one valley in a hike
        """
        result = counting_valleys([1, -1, -1, -1, 1, -1, 1, 1])
        self.assertEquals(result, 1)

    def test_no_valleys(self):
        """Validate zero valleys in a hike
        """
        result = counting_valleys([1, 1, 1, 1, -1, -1, -1, -1])
        self.assertEquals(result, 0)

if __name__ == '__main__':
    unittest.main(exit=False)
