"""Solution for HackerRank challenge: Utopian Tree
"""

def utopian_tree(cycles):
    """Calculate the height of the utopian tree given the starting height 1.
    The tree doubles height each spring, and grows 1 meter each summer.
    Cycles begin at the onset of spring.

    Args:
        cycles (int): number of cycles the tree has lived

    Returns:
        int: calculated height of the tree

    """
    height = 1
    for i in xrange(cycles):
        if i % 2 == 0: #Spring - doubles in height
            height *= 2
        else: #Summer - grows 1 meter
            height += 1
    return height

def main():
    """Receives input from stdin, provides output to stdout.
    """
    tests = [0] * int(raw_input())
    for i in xrange(len(tests)):
        tests[i] = int(raw_input())
    for i in tests:
        print utopian_tree(i)
if __name__ == '__main__':
    main()
