"""Solution for HackerRank challenge: Kangaroo
"""

def kangaroo(location, rate):
    """Find if kangaroos will ever meet in the same x-plane location

    Args:
        location (int[2]): starting location of kangaroos
            (index indicates kangaroo number)
        rate (int[2]): rate of kangaroo jumps
            (index indicates kangaroo number)
            1 <= rate[n] <= 10000

    Returns:
        BOOL: if the kangaroos will ever meet at the same location

    Example:
        Kangaroo_1 starts at location b_1 at rate m_1
        Kangaroo_2 starts at location b_2  at rate m_2

        Position k_1 = m_1 * j_1 + b_1 where j_1 is any number of jumps
        Position k_2 = m_2 * j_2 + b_2 where j_2 is any number of jumps
        When the positions & jumps are the same: k_1 = k_2 AND j_1 = j_2
            m_1 * j + b_1 = m_2 * j + b_2
            0 = (m_1 - m_2) * j + (b_1 - b_2)
            (b_2 - b_1) / (m_1 - m_2) = j
    """
    if location[0] - location[1] != 0 and rate[0] - rate[1] == 0:
        return False
    jumps = (location[1] - location[0]) / (rate[0] - rate[1])
    remainer = (location[1] - location[0]) % (rate[0] - rate[1])
    return jumps > 0 and remainer == 0

def main():
    """Receives input from stdin, provides output to stdout.
    """
    location_k1, rate_k1, location_k2, rate_k2 = map(int, raw_input().split(' '))
    locations = [location_k1, location_k2]
    rates = [rate_k1, rate_k2]
    if kangaroo(locations, rates):
        print 'YES'
    else:
        print 'NO'

if __name__ == '__main__':
    main()
