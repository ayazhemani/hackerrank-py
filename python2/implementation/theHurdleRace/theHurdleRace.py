"""Solution for HackerRank challenge: The Hurdle Race
"""

def the_hurdle_race(jumps, jump_height):
    """Calculate the number of potions required to jump the max height
    """
    potions = max(jumps)-jump_height
    if potions < 0:
        return 0
    return potions

def main():
    """Receives input from stdin, provides output to stdout.
    """
    hurdle_count, jump_height = map(int, raw_input().strip().split(' '))
    jumps = map(int, raw_input().strip().split(' '))
    print the_hurdle_race(jumps, jump_height)

if __name__ == '__main__':
    main()
