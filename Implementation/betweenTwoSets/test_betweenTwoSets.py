"""TDD Test Cases for betweenTwoSets.py
"""

import unittest
from betweenTwoSets import between_two_sets

class TestBetweenTwoSets(unittest.TestCase):
    """Validate the set_results that factors into set_b and can be factored by set_a
    """
    def test_hackerrank_sample(self):
        """Provided test case
        """
        result = between_two_sets([2, 4], [16, 32, 96])
        self.assertEquals(result, 3)

    def test_2elements(self):
        """Provided test case
        """
        result = between_two_sets([2, 4], [32, 128])
        self.assertEquals(result, 4)

    def test_3factors(self):
        """Provided test case
        """
        result = between_two_sets([2, 4, 8], [16, 32, 96])
        self.assertEquals(result, 2)


if __name__ == '__main__':
    unittest.main(exit=False)
