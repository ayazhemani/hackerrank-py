"""TDD Test Cases for utopianTree.py
"""

import unittest
from utopianTree import utopian_tree

class TestUtopianTree(unittest.TestCase):
    """Validate the caluclated height of the utopian tree
    """
    def test_sample1(self):
        """Validate provided test
        """
        result = utopian_tree(0)
        self.assertEquals(result, 1)

    def test_sample2(self):
        """Validate provided test
        """
        result = utopian_tree(1)
        self.assertEquals(result, 2)

    def test_sample3(self):
        """Validate provided test
        """
        result = utopian_tree(4)
        self.assertEquals(result, 7)

if __name__ == '__main__':
    unittest.main(exit=False)
