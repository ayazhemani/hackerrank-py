"""TDD Test Cases for repeatedString.py
"""

import unittest
from repeatedString import repeated_string

class TestRepeatedString(unittest.TestCase):
    """Verify the correct count of 'a' characters within infinite string.
    """
    def test_hackerrank_sample1(self):
        """Verify provided test case.
        """
        result = repeated_string('aba', 10)
        self.assertEquals(result, 7)

    def test_hackerrank_sample2(self):
        """Verify provided test case.
        """
        result = repeated_string('a', 1000000000000)
        self.assertEquals(result, 1000000000000)

if __name__ == '__main__':
    unittest.main(exit=False)
