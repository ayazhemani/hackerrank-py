"""Solution for HackerRank challenge: Modified Kaprekar Numbers
"""

def modified_kaprekar_numbers(num_range):
    """Produce modified kaprekar numbers for the provided range.

    Modified kaprekar numbers are defined as:
        Consider a positive whole number n with d digits. We square n to
        arrive at a number that is either [2 * d] digits long or [2 * d - 1]
        digits long. Split the string representation of the square into two
        parts, l and r. The right hand part, r must be d digits long. The
        left is the remaining substring. Convert those two substrings back to
        integers, add them and see if you get n.

    Args:
        num_range (int[2]): Inclusive range to check for Kaprekar Numbers

    Returns:
        string[]: Array of Kaprekar Numbers
    """
    kep_nums = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728, 4950, 5050, 7272,
                7777, 9999, 17344, 22222, 77778, 82656, 95121, 99999]

    if not kep_nums or num_range > 99999:
        kep_nums = []
        for i in xrange(min(num_range), max(num_range) + 1):
            digits = len(str(i))
            i_squared = i ** 2
            digits_squared = len(str(i_squared))
            right = str(i_squared)[::-1][:digits][::-1]
            left = str(i_squared)[:digits_squared - len(right)]
            if int('0'+left) + int(right) == i and i != 0:
                kep_nums.append(i)

    result = []
    for num in kep_nums:
        if num >= num_range[0] and num <= num_range[1]:
            result.append(str(num))
    if not result:
        result.append('INVALID RANGE')
    return result

def main():
    """Receives input from stdin, provides output to stdout.
    """
    num_range = []
    num_range.append(int(raw_input()))
    num_range.append(int(raw_input()))
    print ' '.join(map(str, modified_kaprekar_numbers(num_range)))

if __name__ == '__main__':
    main()
