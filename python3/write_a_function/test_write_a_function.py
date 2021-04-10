''' TDD Test Cases for is_leap.py
https://www.hackerrank.com/challenges/write-a-function/problem
'''

import unittest
from write_a_function import is_leap

class TestWriteAFunction(unittest.TestCase):
	'''Description
	'''

	def test_hackerrank_sample1(self):
		'''Verify provided test case.
		'''
		result = is_leap(1990)
		self.assertEquals(result, False)
		return

	def test_hackerrank_sample2(self):
		'''Verify provided test case.
		'''
		result = is_leap(2000)
		self.assertEquals(result, True)
		return

	def test_hackerrank_sample3(self):
		'''Verify provided test case.
		'''
		result = is_leap(2400)
		self.assertEquals(result, True)
		return

if __name__ == '__main__':
	unittest.main(exit=False)
