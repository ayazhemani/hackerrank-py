"""Solution for HackerRank challenge: Drawing Book
"""

def drawing_book(book_len, page):
    """Determine the minimum number of pages to turn (from the front or
    back of the book) to get to the desired page.

    Args:
        book_len (int): number of pages in the book.
        page (int): desired page to turn to.

    Returns:
        int: minimum number of pages to turn to get to the correct page.
    """
    if book_len % 2 == 0:
        book_len += 1
    return min([abs(book_len-page), abs(page-0)])/2

def main():
    """Receives input from stdin, provides output to stdout.
    """
    book_len = int(raw_input())
    page = int(raw_input())
    print drawing_book(book_len, page)

if __name__ == '__main__':
    main()
