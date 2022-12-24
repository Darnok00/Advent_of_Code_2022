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


def tail_move(head_position, tail_position):
    if abs(head_position[0] - tail_position[0]) <= 1 and abs(head_position[1] - tail_position[1]) <= 1:
        return False
    return True


def create_moves_table(lines, corners):
    n = abs(corners[3] - corners[2])
    m = abs(corners[1] - corners[0])
    start_point = [abs(corners[0]), abs(corners[2])]
    head_position = [start_point[0], start_point[1]]
    tail_position = [start_point[0], start_point[1]]
    moves_table = [[0 for x in range(m + 1)] for y in range(n + 1)]
    moves_table[start_point[0]][start_point[1]] = 1
    commands = [line.split(" ") for line in lines]
    for command in commands:
        type = command[0]
        value = int(command[1])
        if type == 'R':
            while value != 0:
                head_position[0] += 1
                if tail_move(head_position, tail_position):
                    tail_position = [head_position[0] - 1, head_position[1]]
                    moves_table[tail_position[1]][tail_position[0]] = 1
                value -= 1
        elif type == 'L':
            while value != 0:
                head_position[0] -= 1
                if tail_move(head_position, tail_position):
                    tail_position = [head_position[0] + 1, head_position[1]]
                    moves_table[tail_position[1]][tail_position[0]] = 1
                value -= 1
        elif type == 'D':
            while value != 0:
                head_position[1] -= 1
                if tail_move(head_position, tail_position):
                    tail_position = [head_position[0], head_position[1] + 1]
                    moves_table[tail_position[1]][tail_position[0]] = 1
                value -= 1
        else:
            while value != 0:
                head_position[1] += 1
                if tail_move(head_position, tail_position):
                    tail_position = [head_position[0], head_position[1] - 1]
                    moves_table[tail_position[1]][tail_position[0]] = 1
                value -= 1

    return moves_table


filename = "text.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

sum_table = [sum(line) for line in create_moves_table(lines, find_height_and_width(lines))]
print(sum(sum_table))
