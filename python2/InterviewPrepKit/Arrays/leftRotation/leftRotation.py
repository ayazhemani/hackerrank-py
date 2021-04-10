"""Solution for HackerRank challenge: Left Rotate
"""

def rotate_array(to_rotate, rotations):
    """Description
    """
    return to_rotate[rotations:] + to_rotate[:rotations]

def main():
    """Receives input from stdin, provides output to stdout.
    """
    size, rotations = map(int,raw_input().split(' '))
    list_to_rotate = map(int, raw_input().split(' '))
    print ' '.join(map(str,rotate_array(list_to_rotate, rotations)))

if __name__ == '__main__':
    main()
