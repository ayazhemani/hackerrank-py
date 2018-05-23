"""Solution for HackerRank challenge: Queen's Attack II
"""

def queens_attack_2(board_len, queen_position, obstacles):
    """Description
    """
    queen_position = [queen_position[0] - 1, queen_position[1] - 1]
    board = [[0] * board_len for _ in xrange(board_len)]
    for obstacle in obstacles:
        board[obstacle[0] - 1][obstacle[1] - 1] = -1
    q_pos = queen_position
    board[q_pos[0]][q_pos[1]] = 1

    #move East (x + 1)
    while q_pos[0] < board_len:
        board[q_pos[0]][q_pos[1]] = 1
        q_pos[0] += 1
    q_pos = queen_position

    #move West (x - 1)
    while q_pos[0] > 0:
        board[q_pos[0]][q_pos[1]] = 1
        q_pos[0] -= 1
    q_pos = queen_position

    #move North (y + 1)
    while q_pos[1] < board_len:
        board[q_pos[0]][q_pos[1]] = 1
        q_pos[1] += 1
    q_pos = queen_position

    #move South (y - 1)
    while q_pos[1] > 0:
        board[q_pos[0]][q_pos[1]] = 1
        q_pos[1] -= 1
    q_pos = queen_position

    #move NorthEast (x + 1, y + 1)
    while q_pos[0] < board_len and q_pos[1] < board_len:
        board[q_pos[0]][q_pos[1]] = 1
        q_pos[0] += 1
        q_pos[1] += 1
    q_pos = queen_position

    #move NorthWest (x - 1, y + 1)
    while q_pos[0] > 0 and q_pos[1] < board_len:
        board[q_pos[0]][q_pos[1]] = 1
        q_pos[0] -= 1
        q_pos[1] += 1
    q_pos = queen_position

    #move SouthEast (x + 1, y - 1)
    while q_pos[0] < board_len and q_pos[1] > 0:
        board[q_pos[0]][q_pos[1]] = 1
        q_pos[0] += 1
        q_pos[1] -= 1
    q_pos = queen_position

    #move SouthWest (x - 1, y - 1)
    while q_pos[0] > 0 and q_pos[1] > 0:
        board[q_pos[0]][q_pos[1]] = 1
        q_pos[0] -= 1
        q_pos[1] -= 1
    q_pos = queen_position

    for line in board:
        print line, sum(line)
    print sum([sum(line) for line in board])
    result = sum([sum(line) for line in board]) + len(obstacles) - 1

    return result

def main():
    """Receives input from stdin, provides output to stdout.
    """
    obstacles = []
    board_len, obstacle_count = map(int, raw_input().split(' '))
    queen_position = map(int, raw_input().split(' '))
    for i in range(len(obstacle_count)):
        obstacles.append(map(int, raw_input().split(' ')))

    print queens_attack_2(board_len, queen_position, obstacles)

if __name__ == '__main__':
    main()
