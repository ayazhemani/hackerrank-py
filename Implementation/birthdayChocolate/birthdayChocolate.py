"""Solution for HackerRank challenge: Birthday Chocolate
"""

def birthday_chocolate(squares, day_sum, month_length):
    """Description

    Args:
        squares (TYPE): Description
        day_sum (TYPE): Description
        month_length (TYPE): Description

    Returns:
        TYPE: Description
    """
    portions = None

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
