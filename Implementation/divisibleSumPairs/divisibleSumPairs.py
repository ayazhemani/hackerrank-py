"""Solution for HackerRank challenge: Divisible Sum Pairs
"""

def divisible_sum_pairs(divisor, candidates):
    """Given number candidates and the divisor, determine the number of
    permutations of candidates where the sum of any 2 candidates is divisible
    by the divisor.

    Args:
        divisor (int): number to check for clean divisibility
        candidates (int[]): numbers that are candidates for sum pairs

    Returns:
        int: number of permutations where the sum is divisible
    """
    pair_count = 0
    for i in xrange(0, len(candidates)):
        for j in xrange(i + 1, len(candidates)):
            if (candidates[i] + candidates[j]) % divisor == 0:
                pair_count += 1
    return pair_count

def main():
    """Receives input from stdin, provides output to stdout.
    """
    max_index, divisor = map(int, raw_input().split(' '))
    candidates = map(int, raw_input().split(' '))
    print divisible_sum_pairs(divisor, candidates)

if __name__ == '__main__':
    main()
