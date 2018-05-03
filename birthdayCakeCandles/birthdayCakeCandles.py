"""Solution for HackerRank challenge: Birthday Cake Candles
"""

def birthday_cake_candles(quantity, heights):
    """Count the frequency of candles with the greatest height
    """
    max_height = max(heights)
    blown = 0
    for i in heights:
        if i == max_height:
            blown += 1
    return blown

def main():
    """Receives input from stdin, provides output to stdout.
    """
    quantity = input()
    heights = map(long, raw_input().split(' '))
    print birthday_cake_candles(quantity, heights)

if __name__ == '__main__':
    main()
