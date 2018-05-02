"""Calulate the sum of up to 10 very large integers (i.e. 10^10).
"""

def a_very_big_sum(length, long_list):
    """Calculate the sum of very large integers.

    Returns:
        long: Sum of all numbers in the list.

    Args:
        length (int): length of list of numbers
        long_list (long): list of long numbers to add
    """
    return sum(long_list)

def main():
    """Obtains inputs from stdin and outputs to stdout.
    """
    list_len = input()
    list_numbers = map(long, raw_input().split(' '))
    print a_very_big_sum(list_len, list_numbers)

if __name__ == '__main__':
    main()
