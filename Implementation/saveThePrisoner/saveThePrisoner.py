"""Solution for HackerRank challenge: Save The Prisoner
"""

def save_the_prisoner(prisoners, sweets, chair):
    """Description
    """
    return

def main():
    """Receives input from stdin, provides output to stdout.
    """
    tests = int(raw_input())
    results = []
    for i in xrange(tests):
        temp = map(int, raw_input().split(' '))
        results.append(save_the_prisoner(temp[0], temp[1], temp[2]))
    for i in xrange(tests):
        print results[i]
if __name__ == '__main__':
    main()
