"""TDD Test Cases for migratoryBirds.py
"""

import unittest
from migratoryBirds import migratory_birds

class TestMigratoryBirds(unittest.TestCase):
    """Validate the birds found with the greatest frequency
    """
    def test_hackerrank_sample(self):
        """Validate provided test
        """
        result = migratory_birds([1, 4, 4, 4, 5, 3])
        self.assertEquals(result, 4)

    def test_tied_frequency(self):
        """validate tie is broken by type of least value
        """
        result = migratory_birds([4, 4, 4, 1, 1, 1])
        self.assertEquals(result, 1)

if __name__ == '__main__':
    unittest.main(exit=False)
