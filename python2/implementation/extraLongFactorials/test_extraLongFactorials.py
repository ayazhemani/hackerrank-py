"""TDD Test Cases for extraLongFactorials.py
"""

import unittest
from extraLongFactorials import extra_long_factorials

class TestExtraLongFactorials(unittest.TestCase):
    """Validate factorial of input.
    """
    def test_hackerrank_sample(self):
        """Validate provided test case.
        """
        result = extra_long_factorials(25)
        self.assertEquals(result, 15511210043330985984000000)

if __name__ == '__main__':
    unittest.main(exit=False)
