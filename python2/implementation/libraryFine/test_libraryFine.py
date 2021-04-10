"""TDD Test Cases for libraryFine.py
"""

import unittest
from libraryFine import library_fine

class TestLibraryFine(unittest.TestCase):
    """Validate correct fine for overdue books.
    """
    def test_hackerrank_sample1(self):
        """Validate provided test case.
        """
        result = library_fine([9, 6, 2015], [6, 6, 2015])
        self.assertEquals(result, 45)

    def test_hackerrank_sample2(self):
        """Validate provided test case.
        """
        result = library_fine([15, 7, 2014], [1, 7, 2015])
        self.assertEquals(result, 0)


if __name__ == '__main__':
    unittest.main(exit=False)
