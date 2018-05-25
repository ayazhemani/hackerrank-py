"""TDD Test Cases for encryption.py
"""

import unittest
from encryption import encrypt

class TestEncryption(unittest.TestCase):
    """Description
    """
    def test_sample(self):
        """Description
        """
        result = encrypt()
        self.assertEquals(result, None)

if __name__ == '__main__':
    unittest.main(exit=False)
