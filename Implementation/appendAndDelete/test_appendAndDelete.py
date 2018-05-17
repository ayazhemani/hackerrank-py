"""TDD Test Cases for appendAndDelete.py
"""

import unittest
from appendAndDelete import append_and_delete

class TestAppendAndDelete(unittest.TestCase):
    """Description
    """
    def test_hackerrank_sample1(self):
        """Description
        """
        result = append_and_delete('hackerhappy', 'hackerrank', 9)
        self.assertEquals(result, 'Yes')

if __name__ == '__main__':
    unittest.main(exit=False)
