"""Solution for HackerRank challenge: Diagonal Difference
"""

def diagonal_difference(matrix_len, matrix_array):
    """Given a square matrix, calculate the absolute difference
    between the sum of the diagonals.

    Args:
        matrix_len (TYPE): size of the matrix square - length and height.
        matrix_array (TYPE): 2 dimensional integer array for matrix

    Returns:
        int: absolute value of difference in diagonals
    """

    difference = 0
    for i in xrange(matrix_len):
        difference += matrix_array[i][i] - matrix_array[i][-i-1]

    return abs(difference)

def main():
    """Gets input from stdin, provides output to stdout.
    """
    matrix_len = input()
    matrix_array = []
    for i in xrange(0, matrix_len):
        temp = map(int, raw_input().split(' '))
        matrix_array.append(temp)
    print diagonal_difference(matrix_len, matrix_array)

if __name__ == '__main__':
    main()
