"""TDD Test Cases for beautifulDaysAtTheMovies.py
"""

import unittest
from beautifulDaysAtTheMovies import beautiful_days_at_the_movies

class TestBeautifulDaysAtTheMovies(unittest.TestCase):
    """Validate count of days from range that are beautiful
    """
    def test_sample(self):
        """Validate provided tests
        """
        result = beautiful_days_at_the_movies(20, 23, 6)
        self.assertEquals(result, 2)

    def test_one_date(self):
        """Validate one date that is not beautiful
        """
        result = beautiful_days_at_the_movies(10, 10, 6)
        self.assertEquals(result, 0)

if __name__ == '__main__':
    unittest.main(exit=False)
