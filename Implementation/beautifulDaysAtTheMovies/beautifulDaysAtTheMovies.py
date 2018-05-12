"""Solution for HackerRank challenge: Beautiful Days At The Movies
"""

def beautiful_days_at_the_movies(start, end, divisor):
    """Determine if a day is a beautiful day from a range of days.
    A day is beautiful if it's date and reversed date difference is
    divisible by another number.

    Args:
        start (int): Start day to consider.
        end (int): End date to consider.
        divisor (int): Divisor to determine if date is beautiful

    Returns:
        int: count of number of dates in range are beautiful
    """
    count = 0
    for i in xrange(start, end + 1):
        if (i - int(str(i)[::-1])) % divisor == 0:
            count += 1
    return count

def main():
    """Receives input from stdin, provides output to stdout.
    """
    start, end, divisor = map(int, raw_input().strip().split(' '))
    print beautiful_days_at_the_movies(start, end, divisor)

if __name__ == '__main__':
    main()
