"""TDD Test Cases for drawingBook.py
"""

import unittest
from drawingBook import drawing_book

class TestDrawingBook(unittest.TestCase):
    """Validate the minimum number of pages turn to get to the correct page
    """
    def test_one_page_turn(self):
        """Validate turning one page
        """
        result = drawing_book(6, 2)
        self.assertEquals(result, 1)

    def test_no_pages_turned(self):
        """Validate turning no pages
        """
        result = drawing_book(5, 4)
        self.assertEquals(result, 0)

if __name__ == '__main__':
    unittest.main(exit=False)
