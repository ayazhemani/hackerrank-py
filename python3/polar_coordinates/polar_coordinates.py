''' Solution for HackerRank challenge: Polar Coordinates
https://www.hackerrank.com/challenges/polar-coordinates/problem
'''
from cmath import polar

def polar_coordinates(z=None):
	'''You are given a complex z.
	Your task is to convert it to polar coordinates.

	Args:
		z (string): A single line containing the complex number

	Returns:
		float: r
		float: phi
	'''
	if z is None: return
	return polar(complex(z))


def main():
	'''Receives input from stdin, provides output to stdout.
	'''
	cartesisan = input()
	polar = polar_coordinates(cartesisan)
	print(polar[0])
	print(polar[1])
	return

if __name__ == '__main__':
	main()
