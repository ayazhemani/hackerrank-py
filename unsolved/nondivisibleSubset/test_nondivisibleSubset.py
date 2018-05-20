"""TDD Test Cases for nondivisibleSubset.py
"""

import unittest
from nondivisibleSubset import nondivisible_subset

class TestNondivisibleSubset(unittest.TestCase):
    """Description
    """
    def test_sample(self):
        """Description
        """
        result = nondivisible_subset([1, 7, 2, 4], 3)
        self.assertEquals(result, 3)

if __name__ == '__main__':
    unittest.main(exit=False)
