NUMBER_LINES = 10


def find_height_and_width(lines):
    lines = [line.split(" ") for line in lines]
    actual_width, min_width, max_width = 0, 0, 0
    actual_height, min_height, max_height = 0, 0, 0
    for line in lines:
        line[1] = int(line[1])
        if line[0] == 'R':
            actual_width += line[1]
        elif line[0] == 'L':
            actual_width -= line[1]
        elif line[0] == 'D':
            actual_height -= line[1]
        else:
            actual_height += line[1]

        if max_height < actual_height:
            max_height = actual_height
        if min_height > actual_height:
            min_height = actual_height
        if max_width < actual_width:
            max_width = actual_width
        if min_width > actual_width:
            min_width = actual_width

    return [min_width, max_width, min_height, max_height]


def do_move(first_position, second_position):
    if abs(first_position[0] - second_position[0]) <= 1 and abs(first_position[1] - second_position[1]) <= 1:
        return False
    return True


def is_positive(number):
    return 1 if number > 0 else -1


def classify_action(vector_move):
    if vector_move == [2, 0]:
        return [1, 0]
    if vector_move == [-2, 0]:
        return [-1, 0]
    if vector_move == [0, 2]:
        return [0, 1]
    if vector_move == [0, -2]:
        return [0, -1]

    return [is_positive(vector_move[0]), is_positive(vector_move[1])]


def create_moves_table(lines, corners):
    n = abs(corners[3] - corners[2])
    m = abs(corners[1] - corners[0])
    start_point = [abs(corners[0]), abs(corners[2])]
    positions_list = [[start_point[0], start_point[1]] for x in range(NUMBER_LINES)]
    moves_table = [[0 for x in range(m + 1)] for y in range(n + 1)]
    moves_table[start_point[0]][start_point[1]] = 1
    commands = [line.split(" ") for line in lines]
    for command in commands:
        type = command[0]
        value = int(command[1])

        while value != 0:
            for i in range(NUMBER_LINES):
                if i == 0:
                    if type == 'R':
                        positions_list[i][0] += 1
                    elif type == 'L':
                        positions_list[i][0] -= 1
                    elif type == 'U':
                        positions_list[i][1] += 1
                    else:
                        positions_list[i][1] -= 1
                else:
                    if do_move(positions_list[i - 1], positions_list[i]):
                        vector_move = [positions_list[i - 1][0] - positions_list[i][0],
                                       positions_list[i - 1][1] - positions_list[i][1]]
                        action_vector = classify_action(vector_move)
                        positions_list[i] = [positions_list[i][0] + action_vector[0],
                                             positions_list[i][1] + action_vector[1]]
                        if i == (NUMBER_LINES - 1):
                            moves_table[positions_list[i][1]][positions_list[i][0]] = 1
                    else:
                        break
            value -= 1

    return moves_table


filename = "text.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

sum_table = [sum(line) for line in create_moves_table(lines, find_height_and_width(lines))]
print(sum(sum_table))
