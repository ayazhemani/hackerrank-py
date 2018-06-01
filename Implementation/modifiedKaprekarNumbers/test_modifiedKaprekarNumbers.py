"""TDD Test Cases for modifiedKaprekarNumbers.py
"""

import unittest
from modifiedKaprekarNumbers import modified_kaprekar_numbers

class TestmodifiedKaprekarNumbers(unittest.TestCase):
    """Validate kaprekar numbers for the provided input range.
    """
    def test_hackerrank_sample(self):
        """Validate provided test case.
        """
        result = modified_kaprekar_numbers([1, 100])
        self.assertEquals(result, ['1', '9', '45', '55', '99'])

    def test_invalid_range(self):
        """Validate output given invalid input ranges.
        """
        result = modified_kaprekar_numbers([0, 0])
        self.assertEquals(result, ['INVALID RANGE'])

if __name__ == '__main__':
    unittest.main(exit=False)
