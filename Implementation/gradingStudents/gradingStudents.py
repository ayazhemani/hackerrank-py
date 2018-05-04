"""Solution for HackerRank challenge: Grading Students
"""

def grading_students(scores):
    """Description
    """
    new_scores = scores
    for i in xrange(len(scores)):
        if scores[i] > 35 and scores[i] % 5 > 2:
            new_scores[i] = scores[i] - scores[i] % 5 + 5
    return new_scores

def main():
    """Receives input from stdin, provides output to stdout.
    """
    given_scores = []
    num_grades = int(raw_input())
    for i in xrange(num_grades):
        given_scores.append(int(raw_input()))
    for score in grading_students(given_scores):
        print score

if __name__ == '__main__':
    main()
