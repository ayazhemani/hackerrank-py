"""Solution for HackerRank challenge: Forming a Magic Square

Need to learn: itertools.permutations

The Lo Shu Square, as the magic square on the turtle shell is called,
is the unique normal magic square of order three in which 1 is at the
bottom and 2 is in the upper right corner. Every normal magic square of
order three is obtained from the Lo Shu by rotation or reflection.

2   7   6
9   5   1
4   3   8
"""
def rotate_square_90(square):
    """Rotate square 90 degrees clockwise

    Args:
        square (int[][]): square integer matrix

    Returns:
        int[len(square)][len(square)]: rotated square
    """
    new_square = [list(x) for x in zip(*square[::-1])]
    return new_square

def reflect_square(square):
    """Reflect square on primary axis (where i == j)

    Args:
        square (int[][]): square integer matrix

    Returns:
        int[len(square)][len(square)]: reflected square
    """
    new_square = [[0]*len(square) for _ in range(len(square))]
    for i in xrange(len(square)):
        for j in xrange(len(square)):
            new_square[i][j] = square[j][i]
    return new_square

def forming_a_magic_square(square):
    """Given a list of magic squares, determine the minimum difference
    to transform the input into a magic square.

    Args:
        square (int[][]): Provided square input

    Returns:
        int: minimum difference in values between square and any magic_sqaure
    """
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        ]
    difference = [0 for _ in range(len(magic_squares))]
    for i in xrange(1, 4):
        magic_squares[i] = (rotate_square_90(magic_squares[i-1]))
    for i in xrange(4, 8):
        magic_squares[i] = (reflect_square(magic_squares[i-4]))

    for k in xrange(len(magic_squares)):
        for i in xrange(len(square)):
            for j in xrange(len(square[i])):
                difference[k] += abs(square[i][j] - magic_squares[k][i][j])
    return min(difference)

def main():
    """Receives input from stdin, provides output to stdout.
    """
    square = [[0] * 3] * 3
    square[0] = map(int, raw_input().split(' '))
    square[1] = map(int, raw_input().split(' '))
    square[2] = map(int, raw_input().split(' '))
    print forming_a_magic_square(square)

if __name__ == '__main__':
    main()
