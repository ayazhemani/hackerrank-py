"""Solution for HackerRank challenge: Staircase
"""

def staircase(steps):
    """Description

    Args:
        steps (int): number of rows in staircase

    Returns:
        string[steps]: array of strings to compose the staircase
    """
    if steps < 1:
        return []

    stairs = [''] * steps
    for i in xrange(steps):
        for j in xrange(steps):
            if j < steps - i - 1:
                stairs[i] = stairs[i] + ' '
            else:
                stairs[i] = stairs[i] + '#'
    return stairs

def main():
    """Receives input from stdin, provides output to stdout.
    """
    steps = input()
    for i in staircase(steps):
        print i

if __name__ == '__main__':
    main()
