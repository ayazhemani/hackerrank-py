"""TDD Test Cases for test_dayOfTheProgrammer.py
"""

import unittest
from dayOfTheProgrammer import day_of_the_programmer

class TestDayOfTheProgrammer(unittest.TestCase):
    """Validate the 256th day of the Russian calendar, given the year
    """
    def test_hackerrank_sample1(self):
        """Validate provided test case
        """
        result = day_of_the_programmer(2017)
        self.assertEquals(result, '13.09.2017')

    def test_hackerrank_sample2(self):
        """Validate provided test case
        """
        result = day_of_the_programmer(2016)
        self.assertEquals(result, '12.09.2016')

    def test_hackerrank_sample3(self):
        """Validate provided test case
        """
        result = day_of_the_programmer(1800)
        self.assertEquals(result, '12.09.1800')

if __name__ == '__main__':
    unittest.main(exit=False)
