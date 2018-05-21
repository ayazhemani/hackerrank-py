"""Solution for HackerRank challenge: Repeated String
"""

def repeated_string(substr, repeat_length):
    """Given a string and a length, repeat the string enough times to
    count and return the number of 'a' characters within the length.

    Args:
        substr (string): substring to repeat and find 'a' characters.
        repeat_length (int): length of string to count 'a' characters.

    Returns:
        int: count of 'a' characters within infinite string
    """
    count = (substr.count('a') * int(repeat_length / len(substr))) + \
            (substr[:repeat_length % len(substr)].count('a'))

    return count

def main():
    """Receives input from stdin, provides output to stdout.
    """
    substr = raw_input()
    repeat_length = int(raw_input())
    print repeated_string(substr, repeat_length)

if __name__ == '__main__':
    main()
