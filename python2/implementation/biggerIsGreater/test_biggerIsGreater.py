"""TDD Test Cases for biggerIsGreater.py
"""

import unittest
from biggerIsGreater import bigger_is_greater

class TestBiggerIsGreater(unittest.TestCase):
    """Description
    """
    def test_hackerrank_sample1(self):
        """Description
        """
        result = bigger_is_greater('ab')
        self.assertEquals(result, 'ba')

    def test_hackerrank_sample2(self):
        """Description
        """
        result = bigger_is_greater('zz')
        self.assertEquals(result, 'no answer')

    def test_hackerrank_sample3(self):
        """Description
        """
        result = bigger_is_greater('hefg')
        self.assertEquals(result, 'hegf')

    def test_hackerrank_sample4(self):
        """Description
        """
        result = bigger_is_greater('dhck')
        self.assertEquals(result, 'dhkc')

    def test_hackerrank_sample5(self):
        """Description
        """
        result = bigger_is_greater('dkhc')
        self.assertEquals(result, 'hcdk')

if __name__ == '__main__':
    unittest.main(exit=False)
