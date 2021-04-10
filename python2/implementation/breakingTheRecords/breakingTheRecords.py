"""Solution for HackerRank challenge: Breaking The Records
"""

def breaking_the_records(scores):
    """Given a list of game scores, determine the number of times a high or low record is broken

    Args:
        scores (int[]): list of consequtive game scores

    Returns:
        int[2]: Frequency of breaking (highest, lowest) scores
    """
    min_score, max_score = [], []
    min_score.append(scores[0])
    max_score.append(scores[0])
    for score in scores:
        if score < min(min_score):
            min_score.append(score)
        if score > max(max_score):
            max_score.append(score)
    return [len(max_score)-1, len(min_score)-1]

def main():
    """Receives input from stdin, provides output to stdout.
    """
    raw_input() # ignore first input line
    scores = map(int, raw_input().split(' '))
    print " ".join(map(str, breaking_the_records(scores)))

if __name__ == '__main__':
    main()
