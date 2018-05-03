"""TDD Test Cases for birthdayCakeCandles.py
"""

import unittest
from birthdayCakeCandles import birthday_cake_candles

class TestBirthdayCakeCandles(unittest.TestCase):
    """Validate occurances of max candle height
    """
    def test_hackerrank_sample(self):
        """Test given sample
        """
        result = birthday_cake_candles(4, [3, 2, 1, 3])
        self.assertEquals(result, 2)

if __name__ == '__main__':
    unittest.main(exit=False)
