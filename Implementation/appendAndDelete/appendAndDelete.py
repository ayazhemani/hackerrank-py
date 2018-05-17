"""Solution for HackerRank challenge: Append And Delete
"""

def append_and_delete(s1, s2, ops):
    """Description
    """
    same_count = 0
    for i in xrange(len(s1)):
        if s1[:i] != s2[:i]:
            same_count = i -1
            break
    delete_count = len(s1) - same_count
    append_count = len(s2) - same_count
    # Exact number of operations performed
    if delete_count + append_count == ops:
        return 'Yes'
    # More operations performed than required, but no full delete
    elif (ops - delete_count - append_count) > 0 and \
        (ops - delete_count - append_count) % 2 == 0 and \
        (ops - delete_count - append_count) / 2 <= same_count:
        return 'Yes'
    # Operations include fully deleting string and appending text
    elif ops >= len(s1) + len(s2):
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
