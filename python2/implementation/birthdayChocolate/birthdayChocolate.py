"""Solution for HackerRank challenge: Birthday Chocolate
"""

def birthday_chocolate(squares, total, length):
    """Determine the number of ways the chocolate can be portioned
    given the chocolate sequence squares, the target total, and target length

    Args:
        squares (int[]): Numeric sequence on chocolate squares
        total (int): Target sum of sequence (or day in birthday)
        length (int): Target length of sequence (or month in birthday)

    Returns:
        int: number of ways chocolate can be portioned to conform to target length and sum

    """
    portions = 0
    for i in xrange(len(squares)):
        if i + length <= len(squares) and (sum(squares[i:i + length]) == total):
            portions += 1
    return portions

def main():
    """Receives input from stdin, provides output to stdout.
    """
    raw_input() #number of squares not needed
    squares = map(int, raw_input().split(' '))
    day, month = map(int, raw_input().split(' '))
    print birthday_chocolate(squares, day, month)

if __name__ == '__main__':
    main()
