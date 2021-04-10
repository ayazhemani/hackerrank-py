"""TDD Test Cases for gradingStudents.py
"""

import unittest
from gradingStudents import grading_students

class TestGradingStudents(unittest.TestCase):
    """Test rounding up functionality for grading students
    """
    def test_hackerrank_sample(self):
        """Provided test case
        """
        result = grading_students([73, 67, 38, 33])
        self.assertEquals(result, [75, 67, 40, 33])

    def test_failing_grade(self):
        """Summary
        """
        result = grading_students([29])
        self.assertEquals(result, [29])

    def test_nonfailing_norounding(self):
        """Summary
        """
        result = grading_students([80])
        self.assertEquals(result, [80])

    def test_nonfailing_rounding(self):
        """Summary
        """
        result = grading_students([84])
        self.assertEquals(result, [85])

if __name__ == '__main__':
    unittest.main(exit=False)
