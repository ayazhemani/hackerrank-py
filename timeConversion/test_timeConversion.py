"""TDD Test Cases for timeConversion.py
"""

import unittest
from timeConversion import time_conversion

class TestTimeConversion(unittest.TestCase):
    """Test time conversion from AM/PM to 24hr format
    """
    def test_hackerrank_sample(self):
        """Provided test case
        """
        result = time_conversion('07', '05', '45', 'PM')
        self.assertEquals(result, '19:05:45')

    def test_noon(self):
        """Test edge case of 12PM
        """
        result = time_conversion('12', '00', '00', 'PM')
        self.assertEquals(result, '12:00:00')

    def test_midnight(self):
        """Test edge case of 12PM
        """
        result = time_conversion('12', '00', '00', 'AM')
        self.assertEquals(result, '00:00:00')

    def test_AM(self):
        """Test AM conversion
        """
        result = time_conversion('07', '05', '45', 'AM')
        self.assertEquals(result, '07:05:45')

if __name__ == '__main__':
    unittest.main(exit=False)
