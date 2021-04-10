"""Solution for HackerRank challenge: Apple And Orange
"""

def apple_and_orange(house, trees, apples, oranges):
    """Description
    """
    house_fruit = [[], []]
    # Find if apples hit house
    for apple in apples:
        if apple + trees[0] >= house[0] and apple + trees[0] <= house[1]:
            house_fruit[0].append(apple)

    for orange in oranges:
        if orange + trees[1] >= house[0] and orange + trees[1] <= house[1]:
            house_fruit[1].append(orange)
    # Find if oranges hit house

    return [len(house_fruit[0]), len(house_fruit[1])]

def main():
    """Receives input from stdin, provides output to stdout.
    """
    house = map(int, raw_input().split(' '))
    trees = map(int, raw_input().split(' '))
    raw_input() # fruit_count not used
    apples = map(int, raw_input().split(' '))
    oranges = map(int, raw_input().split(' '))
    for fruit in apple_and_orange(house, trees, apples, oranges):
        print fruit

if __name__ == '__main__':
    main()
