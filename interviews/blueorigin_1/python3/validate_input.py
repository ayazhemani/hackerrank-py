def validateInput(command):
    max_command_len = 4
    valid_actions = ('L', 'R', 'F')

    pos_x = 0
    pos_y = 0
    orientation = 0

    if len(command) > max_command_len:
        return False

    for action in command:
        if action not in valid_actions:
            return False

    for i in range(4):
        for action in command:
            if action == 'L':
                orientation = (orientation - 90) % 360
            elif action == 'R':
                orientation = (orientation + 90) % 360
            elif action == 'F':
                if orientation == 0:
                    pos_y += 1
                elif orientation == 90:
                    pos_x += 1
                elif orientation == 180:
                    pos_y -= 1
                elif orientation == 270:
                    pos_x -= 1

    if pos_y == 0 and pos_x == 0:
        return True

    return False

if __name__ == '__main__':
    print('Enter a command: ', end=' ')
    command = input()
    print(validateInput(command))
