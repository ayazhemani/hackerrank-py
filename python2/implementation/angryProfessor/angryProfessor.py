"""Solution for HackerRank challenge: Angry Professor
"""

def angry_professor(cancellation, arrivals):
    """Determine if class is cancelled based on the number of students who
    arrive on time. If less than the cancellation number arrive on time,
    class_cancelled = YES otherwise NO.

    Args:
        cancellation (int): number of students required to mantain quorum
        arrivals (int[]): student arrival times, minutes after class begins

    Returns:
        string: 'YES' | 'NO' to indicate if class is cancelled
    """
    arrivals.sort()
    if arrivals[cancellation - 1] > 0:
        return 'YES'
    return 'NO'

def main():
    """Receives input from stdin, provides output to stdout.
    """
    tests = int(raw_input())
    line1, line2 = [], []
    for i in xrange(tests):
        line1.append(map(int, raw_input().strip().split(' ')))
        line2.append(map(int, raw_input().strip().split(' ')))
    for i in xrange(tests):
        print angry_professor(line1[i][1], line2[i])

if __name__ == '__main__':
    main()
