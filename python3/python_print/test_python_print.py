''' TDD Test Cases for python_print.py
https://www.hackerrank.com/challenges/python-print/problem
'''

import unittest
from python_print import python_print

class TestPythonPrint(unittest.TestCase):
	'''Description
	'''

	def test_hackerrank_sample1(self):
		'''Verify provided test case.
		'''
		result = python_print(3)
		self.assertEquals(result, '123')
		return

	def test_hackerrank_sample2(self):
		'''Verify provided test case.
		'''
		result = python_print(5)
		self.assertEquals(result, '12345')
		return

if __name__ == '__main__':
	unittest.main(exit=False)
