"""Compute the sum of two integers.
"""

def solve_me_first(x_1, y_1):
    """Function to compute sum of two numbers.

    Args:
        x_1 (int): The first integer.
        y_1 (int): The second integer.

    Returns:
        int: Sum of x_1 and y_1.
    """
    return x_1 + y_1

def main():
    """Get inputs from stdin and print to stdout
    """
    x_1 = input()
    y_1 = input()
    print solve_me_first(x_1, y_1)

if __name__ == '__main__':
    main()
