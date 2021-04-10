"""Solution for HackerRank challenge: Append And Delete
"""

def append_and_delete(s1, s2, ops):
    """Determine if enough operations exist to transform string1 into string2.

    Args:
        s1 (string): Initial string to transform
        s2 (string): Target string for transformation
        ops (int): Number of operations provided

    Returns:
        string: 'Yes' | 'No' to indicate sufficient number of operations
    """
    same_count = 0
    for i in xrange(len(s1)):
        if s1[:i] != s2[:i]:
            break
        same_count = i
    delete_count = len(s1) - same_count
    append_count = len(s2) - same_count
    min_ops = delete_count + append_count
    # Exact number of operations performed (or more)
    if ops >= min_ops:
        # Exact number of operations performed
        if min_ops == ops:
            return 'Yes'
        # Operations include fully deleting string and appending text
        elif ops >= (len(s1) + len(s2)):
            return 'Yes'
        # More operations performed than required, but no full delete
        elif (ops - min_ops) % 2 == 0:
            return 'Yes'
    return 'No'

def main():
    """Receives input from stdin, provides output to stdout.
    """
    initial_string = raw_input().strip()
    final_string = raw_input().strip()
    operations_count = int(raw_input())
    print append_and_delete(initial_string, final_string, operations_count)

if __name__ == '__main__':
    main()
