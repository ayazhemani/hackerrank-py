"""Solution for HackerRank challenge: Plus Minus
"""

def plus_minus(arr_size, int_array):
    """Calculate the fractions of array elements that are positive, negative, and are zeros.

    Return the decimal value of each fraction on a new line.

    Args:
        arr_size (int): size of the integer array.
        int_array (int[]): integer array.

    Returns:
        string[3]: array fractions that are positive, negative, and zero.
            Array is string formatted with a precision of 6 decimal places.
                Positive: A decimal representing of the fraction of positive
            numbers in the array.
                Negative: A decimal representing of the fraction of negative numbers in the array.
                Zero: A decimal representing of the fraction of zeros in
                the array.
    """
    solution = [0.0, 0.0, 0.0] # positive, negative, zero

    for i in xrange(arr_size):
        if int_array[i] > 0:
            solution[0] += 1
        elif int_array[i] < 0:
            solution[1] += 1
        else:
            solution[2] += 1

    if arr_size == 0: # account for divide by zero
        arr_size += 1

    for i in xrange(len(solution)):
        solution[i] /= arr_size
        solution[i] = "{:.6f}".format(solution[i])

    return solution

def main():
    """Receives input from stdin, provides output to stdout.
    """
    arr_size = input()
    int_array = map(int, raw_input().split(' '))
    for dec in plus_minus(arr_size, int_array):
        print dec

if __name__ == '__main__':
    main()
