"""TDD Test Cases for lovelyTriplets.py
"""

import unittest
from lovelyTriplets import lovely_triplets

class TestLoveleyTriplets(unittest.TestCase):
    """Validate the correct graph for lovely triplets
    """
    def test_hackerrank_sample(self):
        """Test given inputs
        """
        result = lovely_triplets(3, 2)
        self.assertEquals(result, [[7, 7], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [1, 7]])

    def test_one_triplet(self):
        """Test given inputs
        """
        result = lovely_triplets(1, 2)
        self.assertEquals(result, [[4, 4], [1, 2], [2, 3], [3, 1], [1, 4]])

if __name__ == '__main__':
    unittest.main(exit=False)
