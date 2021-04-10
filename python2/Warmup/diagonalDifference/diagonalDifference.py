"""Solution for HackerRank challenge: Diagonal Difference
"""

def diagonal_difference(matrix_len, matrix_array):
    """Given a square matrix, calculate the absolute difference
    between the sum of the diagonals.

    Args:
        matrix_len (int): size of the matrix square - length and height.
        matrix_array (int[][]): 2 dimensional integer array for matrix

    Returns:
        int: absolute value of difference in diagonals

    Example:
        Given a matrix_array of matrix_len = n, (n = i = j):

            a_0_0   a_0_1   a_0_2   ...     a_0_j
            a_1_0   a_1_1   a_1_2   ...     a_1_j
            a_2_0   a_2_1   a_2_2   ...     a_2_j
            ...     ...     ...     ...     ...
            a_i_0   a_i_1   a_i_2   ...     a_i_j

        The absolute difference equals the primary diagonal subtracted by the secondary diagonal:
            abs_difference = abs(diagonal_1 - diagonal_2)

        Where:
            diagonal_1 can be computed by adding all instances in the array where i == j

            diagonal_2 can be computed by adding all instances in the array where i + j == n - 1
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
