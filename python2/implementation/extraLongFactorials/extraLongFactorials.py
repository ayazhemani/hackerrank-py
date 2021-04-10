"""Solution for HackerRank challenge: Extra Long Factorials
"""

def extra_long_factorials(num_to_factorial):
    """Calculate the factorial of an integer.

    Args:
        num_to_factorial (int): Number to create factorial for.

    Returns:
        long: factorial of input.
    """
    n_factorial = 1
    for i in xrange(1, num_to_factorial + 1):
        n_factorial *= i
    return n_factorial

def main():
    """Receives input from stdin, provides output to stdout.
    """
    num_to_factorial = int(raw_input())
    print extra_long_factorials(num_to_factorial)

if __name__ == '__main__':
    main()
