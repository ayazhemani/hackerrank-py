"""Solution for HackerRank challenge: Viral Advertising
"""

def viral_advertising(days):
    """Calculate the likes for an ad campaign after a number of days.

    Growth rate is given by the following rate:
        Each day, floor(recipients/2) of the recipients like the
        advertisement and will share it with  friends on the following day.

    Args:
        days (int): number of ad campaign days elapsed

    Returns:
        int: number of advertisment likes
    """
    shared = 5
    liked = 0
    cumulative = 0
    for i in xrange(days):
        liked = (shared // 2)
        shared = liked * 3
        cumulative += liked
    return cumulative

def main():
    """Receives input from stdin, provides output to stdout.
    """
    days_count = int(raw_input())
    print viral_advertising(days_count)

if __name__ == '__main__':
    main()
