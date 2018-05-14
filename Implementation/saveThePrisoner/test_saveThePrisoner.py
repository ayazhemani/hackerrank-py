"""TDD Test Cases for saveThePrisoner.py
"""

import unittest
from saveThePrisoner import save_the_prisoner

class TestSaveThePrisoner(unittest.TestCase):
    """Validate prisoner number with bad candy
    """
    def test_hackerrank_sample1(self):
        """Validate sample test case
        """
        result = save_the_prisoner(4, 6, 2)
        self.assertEquals(result, 3)

    def test_hackerrank_sample2(self):
        """Validate sample test case
        """
        result = save_the_prisoner(5, 2, 1)
        self.assertEquals(result, 2)

    def test_zero_index(self):
        """Validate last prisoner receiving candy
        """
        result = save_the_prisoner(5, 2, 4)
        self.assertEquals(result, 5)

if __name__ == '__main__':
    unittest.main(exit=False)
