''' TDD Test Cases for find_angle.py
https://www.hackerrank.com/challenges/find-angle/problem
'''

import unittest
from find_angle import find_angle

class TestFindAngle(unittest.TestCase):
	'''Test angle MBC
	'''

	def test_hackerrank_sample1(self):
		'''Verify provided test case.
		'''
		result = find_angle(10, 10)
		self.assertEqual(result, '45°')
		return

	def test_hackerrank_sample2(self):
		'''Verify provided test case.
		'''
		result = find_angle(5,5)
		self.assertEqual(result, '45°')
		return

if __name__ == '__main__':
	unittest.main(exit=False)
