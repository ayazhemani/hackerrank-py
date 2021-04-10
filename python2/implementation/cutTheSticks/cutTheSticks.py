"""Solution for HackerRank challenge: Cut The Sticks
"""

def cut_the_sticks(sticks):
    """Iteratively cut sticks based on the minimum stick size.

    Args:
        sticks (int[]): Length of all sticks in bundle.

    Returns:
        int[]: Number of sticks cut at each iteration.
    """
    results = []
    while sticks:
        results.append(len(sticks))
        sticks = [stick - min(sticks) for stick in sticks if stick - min(sticks) > 0]

    return results

def main():
    """Receives input from stdin, provides output to stdout.
    """
    raw_input()
    sticks = map(int, raw_input().split(' '))
    for result in cut_the_sticks(sticks):
        print result

if __name__ == '__main__':
    main()
