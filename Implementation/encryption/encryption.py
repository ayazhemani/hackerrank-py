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
    y_len = int(math.floor(len(str) ** 0.5))
    x_len = int(math.ceil(len(str) ** 0.5))
    while len(str) > y_len*x_len:
        y_len += 1
    str = str.ljust(y_len*x_len)

    result = []
    for i in range(x_len):
        result.append(str[i::x_len].replace(' ', ''))

    return result

def main():
    """Receives input from stdin, provides output to stdout.
    """
    input_string = raw_input().replace(' ', '')
    for word in encrypt(input_string):
        print word,

if __name__ == '__main__':
    main()
