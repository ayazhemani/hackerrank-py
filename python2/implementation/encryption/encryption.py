"""Solution for HackerRank challenge: Encryption
"""
import math

def encrypt(str):
    """Given a string rewrite the string as a block of text and return the columns of the block.

    Where:
        The block width is the ceiling of the sqrt of the string length.
        The block length is the floor of the sqrt of the string length.

    Args:
        str (string): Sentence to encrypt with spaces removed.

    Returns:
        string[]: Columns of block of text.
    """
    length = int(math.floor(len(str) ** 0.5))
    width = int(math.ceil(len(str) ** 0.5))
    while len(str) > length*width:
        length += 1
    str = str.ljust(length*width)

    result = []
    for i in range(width):
        result.append(str[i::width].replace(' ', ''))

    return result

def main():
    """Receives input from stdin, provides output to stdout.
    """
    input_string = raw_input().replace(' ', '')
    for word in encrypt(input_string):
        print word,

if __name__ == '__main__':
    main()
