"""TDD Test Cases for acmIcpcTeam.py
"""

import unittest
from acmIcpcTeam import acm_icpc_team
from acmIcpcTeam import get_combined_topics

class TestAcmIcpcTeam(unittest.TestCase):
    """Validate max topics known by teams, and number of those teams
    """
    def test_sample(self):
        """Validate provided test case
        """
        result = acm_icpc_team(['10101', '11100', '11010', '00101'])
        self.assertEquals(result, [5, 2])

class TestGetCombinedTopics(unittest.TestCase):
    """Validate correct number of topics known by two individuals
    """

    def test_mutually_exclusive(self):
        """Validate topics known when knowledge is mutually exclusive
        """
        result = get_combined_topics(('101010', '010101'))
        self.assertEquals(result, 6)

    def test_union(self):
        """Validate topics known when knowledge shared
        """
        result = get_combined_topics(('101010', '101010'))
        self.assertEquals(result, 3)

if __name__ == '__main__':
    unittest.main(exit=False)
