"""Solution for HackerRank challenge: Migratory Birds
"""

def migratory_birds(birds):
    """Given a list of birds (by bird type), determine the type of bird with
    the highest frequency

    Args:
        birds (int[]): list of birds by bird type

    Returns:
        int: type of bird with the greatest frequency
    """
    set_birds = list(set(birds))
    frequency = [birds.count(bird_type) for bird_type in set_birds]
    return set_birds[frequency.index(max(frequency))]

def main():
    """Receives input from stdin, provides output to stdout.
    """
    raw_input() # number of birds - not needed
    birds = map(int, raw_input().split(' '))
    print migratory_birds(birds)

if __name__ == '__main__':
    main()
