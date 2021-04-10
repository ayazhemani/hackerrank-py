"""Solution for HackerRank challenge: Save The Prisoner
"""

def save_the_prisoner(prisoners, sweets, first_chair):
    """Candies are distributed to prisoners in a round robin fashion around a
    circular table starting with the first chair. The last candy is bad and
    the recipient must be warned.

    Calculate the chair number of the recipient of the bad candy.

    Args:
        prisoners (int): number of prisoners (zero indexed).
        sweets (int): number of candies distributed.
        first_chair (int): first chair to begin candy distribution.

    Returns:
        int: chair of prisoner to be warned about bad candy.
    """
    warned = (sweets + first_chair - 1) % prisoners
    if warned == 0:
        warned += prisoners
    return warned

def main():
    """Receives input from stdin, provides output to stdout.
    """
    tests = int(raw_input())
    results = []
    for i in xrange(tests):
        temp = map(int, raw_input().split(' '))
        results.append(save_the_prisoner(temp[0], temp[1], temp[2]))
    for i in xrange(tests):
        print results[i]
if __name__ == '__main__':
    main()
