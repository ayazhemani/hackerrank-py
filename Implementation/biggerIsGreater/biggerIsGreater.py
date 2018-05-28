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


    base_val = get_lexicographical_value(str)
    results = {}
    for permutation in permutations(str):
        val = get_lexicographical_value(permutation)
        if val > base_val:
            results[val] = permutation

    keylist = results.keys()
    keylist.sort()

    if not keylist:
        return 'no answer'

    return ''.join(results[keylist[0]])

    # START DANS CODE
    # str_len = len(str)

    # for i in xrange(1, str_len):
    #     if i == str_len - 1:
    #         temp = ord(str[0])
    #         templist = [ord(letter) for letter in str]
    #         new_templist = [ord(letter) for letter in str if ord(letter) > temp]
    #         templist.sort()
    #         new_templist.sort()
    #         if len(new_templist) == 0:
    #             return 'no answer'
    #         templist.remove(new_templist[0])
    #         return chr(new_templist[0]) + ''.join([chr(ltr) for ltr in templist])

    #     elif ord(str[str_len - i]) > ord(str[str_len - i - 1]):
    #         # print str[str_len - i], str[str_len - i - 1], ord(str[str_len - i]), ord(str[str_len - i - 1])
    #         tempy = [letter for letter in str]
    #         tempy[str_len - i] = str[str_len - i - 1]
    #         tempy[str_len - i - 1] = str[str_len - i]
    #         return ''.join(tempy)
    # # END DANS CODE

    return str

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

def get_lexicographical_value(lex_str):
    """Summary

    Args:
        lex_str (TYPE): Description

    Returns:
        TYPE: Description
    """
    val = 0
    for i in xrange(len(lex_str)):
        val += (ord(lex_str[i]) - ord('`')) * (10 ** (len(lex_str) - i - 1))
    return val

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
