"""Solution for HackerRank challenge: Climbing The Leaderboard
"""

def climbing_the_leaderboard(scoreboard, game_scores):
    """Given a list of new game scores and a leaderboard ranking,
    determine the new ranking of the player

    Args:
        scoreboard (int[]): Sorted list of unique scores on leaderboard
        game_scores (TYPE): Scores of player

    Returns:
        int[]: List of rankings by player with game_scores
    """
    #board = scoreboard
    scoreboard = list(set(scoreboard))
    scoreboard.append(float('inf'))
    scoreboard.sort(reverse=True)
    rank = []
    for i in xrange(len(scoreboard)-1, -1, -1):
        for j in xrange(len(rank), len(game_scores)):
            if scoreboard[i] > game_scores[j]:
                rank.append(i+1)
            if scoreboard[i] == game_scores[j]:
                rank.append(i)
            if i == 0:
                break

    return rank

def main():
    """Receives input from stdin, provides output to stdout.
    """
    raw_input() #number of scores on scoreboard not needed
    scoreboard = map(int, raw_input().strip().split(' '))
    raw_input() #number of games played not needed
    game_scores = map(int, raw_input().strip().split(' '))
    for rank in climbing_the_leaderboard(scoreboard, game_scores):
        print rank


if __name__ == '__main__':
    main()
