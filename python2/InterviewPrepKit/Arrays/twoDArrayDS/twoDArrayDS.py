"""Solution for HackerRank challenge: 2D Array - DS
"""

def twoDArrayDS(hourglass_input):
    """Description
    """
    hourglass_sums = []
    for i in xrange(0, len(hourglass_input) - 2):
        for j in xrange(0, len(hourglass_input[0]) - 2):
            temp_hourglass = []
            temp_hourglass.append(hourglass_input[i + 0][j + 0:j + 3])
            temp_hourglass.append(hourglass_input[i + 1][j + 0:j + 3])
            temp_hourglass.append(hourglass_input[i + 2][j + 0:j + 3])
            hourglass_sums.append(sum_hourglass(temp_hourglass))
    return max(hourglass_sums)

def sum_hourglass(small_array):
    """ Evaluate sum of hourglass input

    Args:
        small_array (int[3][3]): subset of large array
    """

    return sum(map(sum,small_array)) - small_array[1][0] - small_array[1][2]

def main():
    """Receives input from stdin, provides output to stdout.
    """
    hourglass_input = []
    for i in xrange(6):
        hourglass_input.append(map(int, raw_input().split(' ')))
    print twoDArrayDS(hourglass_input)

if __name__ == '__main__':
    main()
