''' Solution for HackerRank challenge: Python Print
https://www.hackerrank.com/challenges/python-print/problem
'''

def python_print(n):
	'''Print the list of integers from  through  as a string, without spaces.

	Args:
		n (int): length of string

	Returns:
		string: consecutive values
	'''
	text = ''
	for num in range(1,n+1):
		#print(num, end='')
		text = text + str(num)
	return text


def main():
	'''Receives input from stdin, provides output to stdout.
	'''
	n = int(input())
	print(python_print(n))
	return

if __name__ == '__main__':
	main()
