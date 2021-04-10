"""TDD Test Cases for equalizeTheArray.py
"""

import unittest
from equalizeTheArray import equalize_the_array

class TestEqualizeTheArray(unittest.TestCase):
    """Validate minimum number of deletions to create array of equal elements.
    """
    def test_sample(self):
        """Validate provided test case.
        """
        result = equalize_the_array([3, 3, 2, 1, 3])
        self.assertEquals(result, 2)

if __name__ == '__main__':
    unittest.main(exit=False)
