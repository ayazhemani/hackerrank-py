"""Solution for HackerRank challenge: Cats and a Mouse
"""

def cats_and_a_mouse(position):
    """Given the positions of 2 cats and a mouse on a line,
    determine the winner.
    A cat wins if they are closest to the mouse.
    THe mouse wins if the cats are equidistant.

    Args:
        position (int[]): Positions of Cat A, Cat B, and Mouse C respectively.

    Returns:
        string: Winner of the fight.
    """
    candidates = ['Cat A', 'Cat B', 'Mouse C']
    winner = 0

    if abs(position[0]-position[2]) == abs(position[1]-position[2]):
        winner = 2
    elif abs(position[0]-position[2]) > abs(position[1]-position[2]):
        winner = 1
    return candidates[winner]

def main():
    """Receives input from stdin, provides output to stdout.
    """
    query_len = int(raw_input())
    positions = [[0] * 3] * query_len
    for position in positions:
        position = map(int, raw_input().split(' '))
        print cats_and_a_mouse(position)

if __name__ == '__main__':
    main()
