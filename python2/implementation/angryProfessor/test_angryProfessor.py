"""TDD Test Cases for angryProfessor.py
"""

import unittest
from angryProfessor import angry_professor

class TestAngryProfessor(unittest.TestCase):
    """Validate if class is cancelled due to lack of quorum
    """
    def test_sample1(self):
        """Validate provided tests
        """
        result = angry_professor(3, [-1, -3, 4, 2])
        self.assertEquals(result, 'YES')

    def test_sample2(self):
        """Validate provided tests
        """
        result = angry_professor(2, [0, -1, 2, 1])
        self.assertEquals(result, 'NO')

if __name__ == '__main__':
    unittest.main(exit=False)
