"""Solution for HackerRank challenge: Between Two Sets
"""

def between_two_sets(factors, elements):
    """Given two sets of integers (set_a and set_b)
    determine the length of a set of integers (set_results)
    such that:
    1) set_a divides cleanly into set_results AND
    2) set_results divides cleanly into set_b

    Args:
        factors (int[]): set_a as described above
        elements (int[]): set_b as described above

    Returns:
        int: length of results set
    """
    results = []
    for i in xrange(max(factors), min(elements) + 1):
        tally = True
        for factor in factors:
            tally = tally and (i % factor == 0)
        for element in elements:
            tally = tally and (element % i == 0)
        if tally:
            results.append(i)
    return len(results)

def main():
    """Receives input from stdin, provides output to stdout.
    """
    raw_input()
    factors = map(int, raw_input().split(' '))
    elements = map(int, raw_input().split(' '))
    print between_two_sets(factors, elements)

if __name__ == '__main__':
    main()
