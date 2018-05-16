"""Solution for HackerRank challenge: Find Digits
"""

def find_digits(number):
    """Count the digits in a number that divide into that number cleanly.

    Args:
        number (int): Number whose digits will be counted

    Returns:
        int: Count of digits in number that are divisible.
    """
    count = 0
    for digit in str(number):
        if int(digit) == 0:
            continue
        elif number % int(digit) == 0:
            count += 1
    return count

def main():
    """Receives input from stdin, provides output to stdout.
    """
    tests_count = int(raw_input())
    results = []
    for i in xrange(tests_count):
        results.append(find_digits(int(raw_input())))
    for result in results:
        print result

if __name__ == '__main__':
    main()
