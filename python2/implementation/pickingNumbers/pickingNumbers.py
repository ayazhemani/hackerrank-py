"""Solution for HackerRank challenge: Picking Numbers
"""

def picking_numbers(numbers):
    """Given a set of numbers, determine the longest length subset that can
    be derived where all combinations of 2 numbers will have a difference of
    less than 2.

    Args:
        numbers (int[]): Sorted list of numbers

    Returns:
        int: Length of longest subset with combination difference of <2
    """
    numbers_set = list(set(numbers))
    numbers_count = [numbers.count(i) for i in numbers_set]
    tally = max(numbers_count)
    combos = [abs(numbers_set[i-1] - numbers_set[i]) for i in xrange(1, len(numbers_set))]
    for i in xrange(len(combos)):
        if combos[i] <= 1 and tally < numbers_count[i] + numbers_count[i+1]:
            tally = numbers_count[i] + numbers_count[i+1]
    return tally

def main():
    """Receives input from stdin, provides output to stdout.
    """
    raw_input() # size of the array not needed
    numbers = map(int, raw_input().split(' '))
    numbers.sort()

    print picking_numbers(numbers)

if __name__ == '__main__':
    main()
