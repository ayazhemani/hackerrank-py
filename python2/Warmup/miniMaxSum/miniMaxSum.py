"""Solution for HackerRank challenge: Mini-Max Sum
"""

def mini_max_sum(int_array):
    """Produce a sum of the top and bottom 4 integers

    Args:
        int_array (array[5]): array of five positive integers.

    Returns:
        long tuple: minimum and maximum values that can be summed from array
    """
    min_track = float('inf')
    max_track = float('-inf')
    min_track = sum(int_array) - max(int_array)
    max_track = sum(int_array) - min(int_array)
    return (min_track, max_track)

def main():
    """Receives input from stdin, provides output to stdout.
    """
    int_input = map(int, raw_input().split(' '))
    result = mini_max_sum(int_input)
    print result[0], result[1]

if __name__ == '__main__':
    main()
