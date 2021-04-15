''' Solution for HackerRank challenge: Find Angle
https://www.hackerrank.com/challenges/find-angle/problem
'''

from math import sqrt, sin, asin, degrees

def find_angle(ab, bc):
	'''Find angle MBC in degrees

	Args:
		ab (int): The length of side ab
		bc (int): The length of side bc

	Returns:
		string: angle MBC in degrees.
	'''
	ac = sqrt(ab**2 + bc**2)
	mc = ac/2
	mbc = degrees(asin(mc/bc))
	return str(round(mbc))+u"\N{DEGREE SIGN}"


def main():
	'''Receives input from stdin, provides output to stdout.
	'''
	ab = int(input())
	bc = int(input())
	print(find_angle(ab,bc))
	return

if __name__ == '__main__':
	main()
