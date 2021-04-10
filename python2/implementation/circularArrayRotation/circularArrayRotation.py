"""Solution for HackerRank challenge: Circular Array Rotation
"""

def circular_array_rotation(elements, rotation_count):
    """Given an array and a rotation offset,
    return a new right rotated array.

    Args:
        elements (int[]): listed elements to be rotated
        rotation_count (int): length of rotation offset

    Returns:
        int[]: new array of rotated elements
    """
    rotate = rotation_count % len(elements)
    elements = elements[len(elements)-rotate:] + elements[:len(elements)-rotate]
    return elements

def main():
    """Receives input from stdin, provides output to stdout.
    """
    element_count, rotation_count, query_count = map(int, raw_input().split(' '))
    elements = map(int, raw_input().split(' '))

    rotated_array = circular_array_rotation(elements, rotation_count)
    queries = []
    for i in xrange(query_count):
        queries.append(int(raw_input()))
    for query in queries:
        print rotated_array[query]

if __name__ == '__main__':
    main()
