"""Solution for HackerRank challenge: Equalize The Array
"""

def equalize_the_array(array):
    """Calculate the minimum number of deletions to create an array of equal
    elements.

    Args:
        array (int[]): array of integers.

    Returns:
        int: minimum number of deletions to create array of equal elements.
    """
    array = [array.count(i) for i in set(array)]
    array.sort()
    return sum(array) - array[-1]

def main():
    """Receives input from stdin, provides output to stdout.
    """
    raw_input()
    array = map(int, raw_input().split(' '))
    print equalize_the_array(array)

if __name__ == '__main__':
    main()
