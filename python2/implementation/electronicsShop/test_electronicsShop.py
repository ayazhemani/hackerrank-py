"""TDD Test Cases for electronicsShop.py
"""

import unittest
from electronicsShop import electronics_shop

class TestElectronicsShop(unittest.TestCase):
    """Validate spend given highest-cost affordable electronics
    """
    def test_hackerrank_sample1(self):
        """Validate case where keyboard and usb can be purchased
        """
        result = electronics_shop(10, [3, 1], [5, 2, 8])
        self.assertEquals(result, 9)

    def test_no_purchase(self):
        """Validate case where no purchase is possible
        """
        result = electronics_shop(5, [4], [5])
        self.assertEquals(result, -1)

if __name__ == '__main__':
    unittest.main(exit=False)
