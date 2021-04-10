"""Solution for HackerRank challenge: Sock Merchant
"""

def sock_merchant(colors):
    """Given a list of colors of socks present,
    determine the number of matching pairs of socks available

    Args:
        colors (int[]): Array of colors of socks available

    Returns:
        int: Number of matching pairs available
    """
    colors.sort()
    colors_set = list(set(colors))
    frequency = [colors.count(color)/2 for color in colors_set]
    return sum(frequency)

def main():
    """Receives input from stdin, provides output to stdout.
    """
    raw_input() # number of socks not used
    colors = map(int, raw_input().split(' '))
    print sock_merchant(colors)

if __name__ == '__main__':
    main()
