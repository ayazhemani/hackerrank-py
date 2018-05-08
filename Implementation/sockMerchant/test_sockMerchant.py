"""TDD Test Cases for sockMerchant.py
"""

import unittest
from sockMerchant import sock_merchant

class TestSockMerchant(unittest.TestCase):
    """Validate number of sock pairs present
    """
    def test_hackerrank_sample(self):
        """Validate provided test case
        """
        result = sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20])
        self.assertEquals(result, 3)

    def test_one_pair(self):
        """Validate case of one matching pair
        """
        result = sock_merchant([10, 10])
        self.assertEquals(result, 1)

    def test_no_matching_pairs(self):
        """Validate case of no matching pairs
        """
        result = sock_merchant([10, 20])
        self.assertEquals(result, 0)

if __name__ == '__main__':
    unittest.main(exit=False)
