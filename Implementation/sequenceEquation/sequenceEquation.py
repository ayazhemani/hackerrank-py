"""Solution for HackerRank challenge: Sequence Equation
"""

def sequence_equation(seq):
    """Given a set of numbers, return the second index lookup
    (index of index) of the range of the sequence.

    Args:
        seq (int[]): Initial sequence of numbers

    Returns:
        int[]: Second index array of sequence
    """
    result = []
    for i in xrange(len(seq)):
        temp = seq.index(seq.index(i + 1) + 1) + 1
        result.append(temp)
    return result

def main():
    """Receives input from stdin, provides output to stdout.
    """
    raw_input()
    sequence = map(int, raw_input().split(' '))
    for result in sequence_equation(sequence):
        print result

if __name__ == '__main__':
    main()
