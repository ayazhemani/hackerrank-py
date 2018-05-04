"""HackerRank Challenge: Simple Array Sum.
"""

def simple_array_sum(len, arr):
    """Given an array of integers, find the sum of its elements.

    Args:
        len (int): size of the array (arr).
        arr (int[]): array of integers.
    """
    return sum(arr)

def main():
    """Get stdin, format inputs, & print to stdout.
    """
    length = input()
    int_string = map(int, raw_input().split(" "))
    print simple_array_sum(length, int_string)

if __name__ == '__main__':
    main()
