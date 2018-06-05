"""Solution for HackerRank challenge: ACM ICPC Team
"""
from itertools import combinations

def acm_icpc_team(knowledge):
    """Calculate the maximum number of topics a 2-person team can know and
    calculate the number of ways to form a 2-person team that knows the
    maximum number of topics.

    Input is given as an array of n lines containing a binary string of
    length m. If the ith line's jth character is 1, then the ith person knows
    the jth topic.

    Args:
        knowledge (string[]): Array of strings indicating topics known

    Returns:
        int[2]: Array of two integers as follows:
            Maximum number of topics,
            Length of combinations resulting in max known topics
    """
    max_total = 0
    pairings = {}
    potential_teams = [[knowledge[i], knowledge[j]] \
                       for (i, j) in combinations(range(len(knowledge)), 2)]
    for team in potential_teams:
        total = get_combined_topics(team)
        if total >= max_total:
            pairings[total] = pairings.get(total, [])
            pairings[total].append(team)
    return [max(pairings.keys()), len(pairings[max(pairings.keys())])]

def get_combined_topics(team):
    """Calculates the combined known topics for 2 team members

    Args:
        team (string[2]): Knowlege of potential team members

    Returns:
        int: Number of combined known topics

    """
    know1, know2 = team
    knowledge = int(know1, base=2) | int(know2, base=2)
    return bin(knowledge).count('1')

def main():
    """Receives input from stdin, provides output to stdout.
    """
    n, m = map(int, raw_input().split(' '))
    knowledge = []
    for i in xrange(n):
        knowledge.append(raw_input())
    print '\n'.join(map(str, acm_icpc_team(knowledge)))

if __name__ == '__main__':
    main()
