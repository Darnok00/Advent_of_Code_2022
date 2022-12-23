def create_vertical_lines(horizontal_lines):
    vertical_lines = []
    number_horizontal_lines = len(horizontal_lines)
    number_vertical_lines = len(horizontal_lines[0])
    for i in range(number_vertical_lines):
        vertical_lines.append([])
        for j in range(number_horizontal_lines):
            vertical_lines[-1].append(horizontal_lines[j][i])

    return vertical_lines


def check_visibility_line(line):
    max_number = -1
    array_visibility = []
    for i in range(len(line)):
        actual_number = int(line[i])
        if actual_number > max_number:
            max_number = actual_number
            array_visibility.append(i)
    return array_visibility


def create_visibility_table(vertical_lines, horizontal_lines):
    n = len(horizontal_lines)
    m = len(vertical_lines)
    visibility_table = [[0 for x in range(m)] for y in range(n)]
    reversed_vertical_lines = [line[::-1] for line in vertical_lines]
    reversed_horizontal_lines = [line[::-1] for line in horizontal_lines]

    for i in range(n):
        array_visibility = check_visibility_line(horizontal_lines[i])
        for index in array_visibility:
            visibility_table[i][index] = 1

        array_visibility = check_visibility_line(reversed_horizontal_lines[i])
        for index in array_visibility:
            visibility_table[i][m - index - 1] = 1

    for i in range(m):
        array_visibility = check_visibility_line(vertical_lines[i])
        for index in array_visibility:
            visibility_table[index][i] = 1

        array_visibility = check_visibility_line(reversed_vertical_lines[i])
        for index in array_visibility:
            visibility_table[n - index - 1][i] = 1

    return visibility_table

filename = "text.txt"

with open(filename) as file:
    horizontal_lines = [line.rstrip() for line in file]

visibility_table = create_visibility_table(create_vertical_lines(horizontal_lines), horizontal_lines)
sum_visibility_table = [sum(array) for array in visibility_table]
print(sum(sum_visibility_table))
