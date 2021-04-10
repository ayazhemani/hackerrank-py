"""Solution for HackerRank challenge: Jumping on the Clouds: Revisited
"""

def jumping_on_the_clouds_revisited(clouds, distance):
    """Return the energy left in the cloud after it traverses hops and
    returns to index 0. Each hop consumes 1 unit of energy. When a value
    of 1 is encountered, an additional 2 units of energy are expended.

    The next index is calulated as follows:
        next_index = (current_index + distance) % cloud_count

    Args:
        clouds (int[]): Array of cloud values.
        distance (int): Hop distance cloud can traverse.

    Returns:
        int: Energy remaining after returning to index 0
    """
    i = 0
    energy = 100
    while True:
        if clouds[i] == 1:
            energy -= 2
        i = (i + distance) % len(clouds)
        energy -= 1
        if i == 0:
            break
    return energy

def main():
    """Receives input from stdin, provides output to stdout.
    """
    cloud_count, distance = map(int, raw_input().split(' '))
    clouds = map(int, raw_input().split(' '))
    print jumping_on_the_clouds_revisited(clouds, distance)

if __name__ == '__main__':
    main()
