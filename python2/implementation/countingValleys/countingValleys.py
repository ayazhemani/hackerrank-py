"""Solution for HackerRank challenge: Counting Valleys
"""

def counting_valleys(steps):
    """Provided an array of vertical directions, count the number of valleys.
    Valleys are defined as a change in elevation from negative to zero.

    Args:
        steps (int[]): Array of vertical steps {-1, 1}

    Returns:
        int: Number of valleys present in hike
    """
    valleys = 0
    altitude = 0
    for i in xrange(len(steps)):
        altitude += steps[i]
        if altitude - steps[i] < 0 and altitude == 0:
            valleys += 1
    return valleys

def main():
    """Receives input from stdin, provides output to stdout.
    """
    raw_input() #number of steps not needed
    steps = [-1 if step == 'D' else 1 for step in list(raw_input())]
    print counting_valleys(steps)

if __name__ == '__main__':
    main()
