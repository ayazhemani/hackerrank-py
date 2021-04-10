''' Solution for HackerRank challenge: Write A Function
https://www.hackerrank.com/challenges/write-a-function/problem
'''

def is_leap(year):
	''' Given a year, determine whether it is a leap year.
	If it is a leap year, return the Boolean True, otherwise return False.

	Args:
		year (int): description

	Returns:
		bool: is year a leap year
	'''
	leap = False

	if year%4 == 0:
		leap = True
		if year%100 == 0:
			leap = False
			if year%400 == 0:
				leap = True

	return leap


def main():
	'''Receives input from stdin, provides output to stdout.
	'''
	year = int(input())
	print(is_leap(year))
	return

if __name__ == '__main__':
	main()
