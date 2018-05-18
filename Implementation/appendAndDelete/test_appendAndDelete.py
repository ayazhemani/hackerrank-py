"""TDD Test Cases for appendAndDelete.py
"""

import unittest
from appendAndDelete import append_and_delete

class TestAppendAndDelete(unittest.TestCase):
    """Validate if sufficient number of opertions exist.
    """
    def test_hackerrank_sample1(self):
        """Validate provided test cases.
        """
        result = append_and_delete('hackerhappy', 'hackerrank', 9)
        self.assertEquals(result, 'Yes')

    def test_hackerrank_sample2(self):
        """Validate provided test cases.
        """
        result = append_and_delete('asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv', 'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv', 20)
        self.assertEquals(result, 'Yes')

if __name__ == '__main__':
    unittest.main(exit=False)
