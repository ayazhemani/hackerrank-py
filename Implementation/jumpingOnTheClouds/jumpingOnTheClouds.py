"""Solution for HackerRank challenge: Jumping On The Clouds
"""

def jumping_on_the_clouds(clouds):
    """Determine the length of the shortest path from start cloud to end
    cloud while avoiding clouds with value 1. Jumps can be of length 1 or 2,
    although jumps must be made through the consequtive clouds.

    Args:
        clouds (int[]): Array of cloud values.

    Returns:
        int: Length of shortest path from start to end cloud.
    """
    index_clouds = [index for index, v in enumerate(clouds) if v == 0]
    for cloud in index_clouds:
        if index_clouds.index(cloud) == len(index_clouds) - 1:
            break
        if index_clouds[index_clouds.index(cloud) - 1] == cloud - 1 and \
        index_clouds[index_clouds.index(cloud) + 1] == cloud + 1:
            index_clouds.remove(cloud)

    return len(index_clouds) - 1

def main():
    """Receives input from stdin, provides output to stdout.
    """
    raw_input()
    clouds = map(int, raw_input().split(' '))
    print jumping_on_the_clouds(clouds)

if __name__ == '__main__':
    main()
