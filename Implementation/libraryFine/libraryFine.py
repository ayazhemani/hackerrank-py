"""Solution for HackerRank challenge: Library Fine
"""

def library_fine(rtn, due):
    """Calculate the book fine based on the calendar day, month, or year
    differences.

    Args:
        rtn (int[3]): Day, Month, Year that the book was returned.
        due (int[3]): Day, Month, Year that the book was due.

    Returns:
        int: Fine for overdue book, if any.
    """
    fine = 0
    if rtn[2] - due[2] > 0:
        # Book Year overdue
        fine = 10000
    else:
        if rtn[2] - due[2] == 0 and rtn[1] - due[1] > 0:
            # Book Month overdue
            fine = 500 * (rtn[1] - due[1])
        else:
            if rtn[2] - due[2] == 0 and \
                    rtn[1] - due[1] == 0 and \
                    rtn[0] - due[0] > 0:
                # Book Day overdue
                fine = 15 * (rtn[0] - due[0])
    return fine

def main():
    """Receives input from stdin, provides output to stdout.
    """
    book_returned = map(int, raw_input().split(' '))
    book_due = map(int, raw_input().split(' '))

    print library_fine(book_returned, book_due)

if __name__ == '__main__':
    main()
