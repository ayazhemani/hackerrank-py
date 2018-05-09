"""Solution for HackerRank challenge: Electronics Shop
"""

def electronics_shop(budget, keyboard, usb):
    """Given a budget and available electronics, determine the highest amount
     that can be spent on one of each electronic device.

    Args:
        budget (int): Total amount available to spend.
        keyboard (int[]): Prices of available keyboards for purchase.
        usb (int[]): Prices of available usb drives for purchase.

    Returns:
        int: Amount spent by patron. If none, return -1.
    """
    spend = float('-inf')
    master = [[0]*len(usb)]*len(keyboard)
    for i in xrange(0, len(keyboard)):
        for j in xrange(0, len(usb)):
            master[i][j] = keyboard[i] + usb[j]
            if master[i][j] > spend and master[i][j] <= budget:
                spend = master[i][j]
    if spend == float('-inf'):
        spend = -1
    return spend

def main():
    """Receives input from stdin, provides output to stdout.
    """
    budget, keyboard_models, usb_models = map(int, raw_input().split(' '))
    keyboard = map(int, raw_input().split(' '))
    usb = map(int, raw_input().split(' '))
    keyboard.sort()
    usb.sort()
    print electronics_shop(budget, keyboard, usb)

if __name__ == '__main__':
    main()
