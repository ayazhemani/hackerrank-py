"""TDD Test Cases for encryption.py
"""

import unittest
from encryption import encrypt

class TestEncryption(unittest.TestCase):
    """Validate columns of blocks for given string.
    """
    def test_hackerrank_sample1(self):
        """Validate provided test.
        """
        result = encrypt('haveaniceday')
        self.assertEquals(result, ['hae', 'and', 'via', 'ecy'])

    def test_hackerrank_sample2(self):
        """Validate provided test.
        """
        result = encrypt('feedthedog')
        self.assertEquals(result, ['fto', 'ehg', 'ee', 'dd'])

    def test_hackerrank_sample3(self):
        """Validate provided test.
        """
        result = encrypt('chillout')
        self.assertEquals(result, ['clu', 'hlt', 'io'])

    def test_hackerrank_sample4(self):
        """Validate provided test.
        """
        result = encrypt('iffactsdontfittotheorychangethefacts')
        self.assertEquals(result, ['isieae', 'fdtonf', 'fotrga', 'anoyec', 'cttctt', 'tfhhhs'])

if __name__ == '__main__':
    unittest.main(exit=False)
