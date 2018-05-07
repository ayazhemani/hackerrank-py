"""TDD Test Cases for birthdayChocolate.py
"""

import unittest
from birthdayChocolate import birthday_chocolate

class TestBirthdayChocolate(unittest.TestCase):
    """Validate number of segments that can be provided
    """
    def test_hackerrank_sample1(self):
        """Test provided inputs
        """
        result = birthday_chocolate([1, 2, 1, 3, 2], 3, 2)
        self.assertEquals(result, 2)

    def test_hackerrank_sample2(self):
        """Test provided inputs
        """
        result = birthday_chocolate([1, 1, 1, 1, 1, 1], 3, 2)
        self.assertEquals(result, 0)

    def test_hackerrank_sample3(self):
        """Test provided inputs
        """
        result = birthday_chocolate([4], 4, 1)
        self.assertEquals(result, 1)

    def test_hackerrank_sample4(self):
        """Test provided inputs
        """
        result = birthday_chocolate([2, 2, 1, 3, 2], 4, 2)
        self.assertEquals(result, 2)


if __name__ == '__main__':
    unittest.main(exit=False)
