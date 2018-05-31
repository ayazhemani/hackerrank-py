"""Solution for HackerRank challenge: Bigger Is Greater
"""

from itertools import permutations

def bigger_is_greater(str):
    """Description

    Args:
        str (TYPE): Description

    Returns:
        TYPE: Description
    """
    initial_sequence = [ord(ltr) for ltr in str]
    final_sequence = next_permutation(initial_sequence)
    if not final_sequence:
        return 'no answer'
    return ''.join(map(chr, final_sequence))

def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return arr

def main():
    """Receives input from stdin, provides output to stdout.
    """
    test_len = int(raw_input())
    results = []
    for i in xrange(test_len):
        results.append(bigger_is_greater(raw_input().strip()))

    for result in results:
        print result

if __name__ == '__main__':
    main()
