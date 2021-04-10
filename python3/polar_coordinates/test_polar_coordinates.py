''' TDD Test Cases for polar_coordinates.py
https://www.hackerrank.com/challenges/polar-coordinates/problem
'''

import unittest
from polar_coordinates import polar_coordinates

class TestPolarCoordinates(unittest.TestCase):
	'''Test conversion of Cartesian coordinates to polar coordinates
	'''

	def test_hackerrank_sample1(self):
		'''Verify provided test case.
		'''
		result = polar_coordinates('1+2j')
		self.assertEqual(result, (2.23606797749979, 1.1071487177940904))
		return

	def test_hackerrank_sample2(self):
		'''Verify provided test case.
		'''
		result = polar_coordinates('-1.0+0.0j')
		self.assertEqual(result, (1.0, 3.1415926535897931))
		return

if __name__ == '__main__':
	unittest.main(exit=False)
