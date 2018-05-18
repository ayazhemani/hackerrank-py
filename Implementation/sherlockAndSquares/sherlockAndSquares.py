"""Solution for HackerRank challenge: Sherlock And Squares
"""

def sherlock_and_squares(square_range):
    """Determine the number of squares present in a range of numbers.

    Args:
        square_range (int[2]): Min and Max of range of numbers (inclusive).

    Returns:
        int: Count of squares within inclusive range
    """
    max_sqrt = int(square_range[1] ** 0.5)
    min_sqrt = float(square_range[0] ** 0.5)
    if int(min_sqrt) != min_sqrt:
        min_sqrt += 1
    min_sqrt = int(min_sqrt)
    count = max_sqrt - min_sqrt + 1
    return count

def main():
    """Receives input from stdin, provides output to stdout.
    """
    results = []
    for i in xrange(int(raw_input())):
        results.append(sherlock_and_squares(map(int, raw_input().split(' '))))

    for result in results:
        print result
if __name__ == '__main__':
    main()
