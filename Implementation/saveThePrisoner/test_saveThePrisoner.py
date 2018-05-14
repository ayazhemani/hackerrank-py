"""TDD Test Cases for saveThePrisoner.py
"""

import unittest
from saveThePrisoner import save_the_prisoner

class TestSaveThePrisoner(unittest.TestCase):
    """Description
    """
    def test_sample(self):
        """Description
        """
        result = save_the_prisoner()
        self.assertEquals(result, None)

if __name__ == '__main__':
    unittest.main(exit=False)
