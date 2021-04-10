"""Solution for HackerRank challenge: Bon Appetit
"""

def bon_appetit(bill, not_eaten, charged):
    """Given 2 patrons splitting a bill, determine amount that Patron_1 is
    overcharged. Patron_1 orders one less item than Patron_2 (denoted as
    not_eaten).

    Args:
        bill (int[]): Array of prices of items ordered.
        not_eaten (int): Array index of item not eaten by Patron_1.
        charged (int): Amount Patron_2 charges Patron_1, after meal split.

    Returns:
        string: refunded amount to Patron_1 if overcharged, else "Bon Appetit"
    """
    actual = (sum(bill) - bill[not_eaten]) / 2
    refund = charged - actual
    if refund == 0:
        refund = 'Bon Appetit'

    return refund

def main():
    """Receives input from stdin, provides output to stdout.
    """
    items_count, not_eaten = map(int, raw_input().split(' '))
    bill = map(int, raw_input().split(' '))
    charged = int(raw_input())
    print bon_appetit(bill, not_eaten, charged)

if __name__ == '__main__':
    main()
