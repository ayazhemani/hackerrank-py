"""TDD Test Cases for designerPDFViewer.py
"""

import unittest
from designerPDFViewer import designer_pdf_viewer

class TestDesignerPDFViewer(unittest.TestCase):
    """Validate calculated highlighted area of text
    """
    def test_hackerrank_sample1(self):
        """Validate provieded test case
        """
        result = designer_pdf_viewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5,
                                      5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                                     'abc')
        self.assertEquals(result, 9)

    def test_hackerrank_sample2(self):
        """Validate provieded test case
        """
        result = designer_pdf_viewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5,
                                      5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7],
                                     'zaba')
        self.assertEquals(result, 28)

if __name__ == '__main__':
    unittest.main(exit=False)
