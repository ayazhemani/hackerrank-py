"""TDD Test Cases for bonAppetit.py
"""

import unittest
from bonAppetit import bon_appetit

class TestBonAppetit(unittest.TestCase):
    """Validate overcharged amounts for Patron_1
    """
    def test_overcharged(self):
        """Validate case when Patron_2 overcharges Patron_1
        """
        result = bon_appetit([3, 10, 2, 9], 1, 12)
        self.assertEquals(result, 5)

    def test_not_overcharged(self):
        """Validate case if charges are correct
        """
        result = bon_appetit([3, 10, 2, 9], 1, 7)
        self.assertEquals(result, 'Bon Appetit')

if __name__ == '__main__':
    unittest.main(exit=False)
