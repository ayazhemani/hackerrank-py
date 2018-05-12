"""TDD Test Cases for viralAdvertising.py
"""

import unittest
from viralAdvertising import viral_advertising

class TestViralAdvertising(unittest.TestCase):
    """Validate the number of likes for an ad campaign after a number of days.
    """
    def test_hackerrank_sample1(self):
        """Validate provided test
        """
        result = viral_advertising(1)
        self.assertEquals(result, 2)

    def test_hackerrank_sample2(self):
        """Validate provided test
        """
        result = viral_advertising(2)
        self.assertEquals(result, 5)

    def test_hackerrank_sample3(self):
        """Validate provided test
        """
        result = viral_advertising(3)
        self.assertEquals(result, 9)

    def test_hackerrank_sample4(self):
        """Validate provided test
        """
        result = viral_advertising(4)
        self.assertEquals(result, 15)

    def test_hackerrank_sample5(self):
        """Validate provided test
        """
        result = viral_advertising(5)
        self.assertEquals(result, 24)

if __name__ == '__main__':
    unittest.main(exit=False)
