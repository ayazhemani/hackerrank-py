"""TDD Test Cases for sequenceEquation.py
"""

import unittest
from sequenceEquation import sequence_equation

class TestSequenceEquation(unittest.TestCase):
    """Validate the second index lookup sequence
    """
    def test_hackerrank_sample1(self):
        """Validate provided test case
        """
        result = sequence_equation([5, 2, 1, 3, 4])
        self.assertEquals(result, [4, 2, 5, 1, 3])

if __name__ == '__main__':
    unittest.main(exit=False)
