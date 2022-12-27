import copy


def parse_line(line):
    split_line = line.split(' ')
    result_array = []
    for element in split_line:
        if element != '->':
            values = element.split(',')
            result_array.append([int(values[0]), int(values[1])])

    return result_array


def boundaries(parser_lines):
    minimum_x = min([min([coordinates[0] for coordinates in parser_line]) for parser_line in parser_lines])
    maximum_x = max([max([coordinates[0] for coordinates in parser_line]) for parser_line in parser_lines])
    minimum_y = min([min([coordinates[1] for coordinates in parser_line]) for parser_line in parser_lines])
    maximum_y = max([max([coordinates[1] for coordinates in parser_line]) for parser_line in parser_lines])

    return minimum_x, maximum_x, minimum_y, maximum_y


def create_start_map(parser_lines):
    minimum_x, maximum_x, minimum_y, maximum_y = boundaries(parser_lines)
    n = maximum_y
    m = maximum_x
    start_map = [[1 for x in range(2*m)] for y in range(n + 3)]
    for line in parser_lines:
        for i in range(len(line) - 1):
            x1 = line[i][0]
            x2 = line[i + 1][0]
            y1 = line[i][1]
            y2 = line[i + 1][1]

            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1

            for j in range(y1, y2 + 1, 1):
                for k in range(x1, x2 + 1, 1):
                    start_map[j][k] = 0

    for i in range(len(start_map[0])):
        start_map[-1][i] = 0

    # for line in start_map:
    #     string = ''
    #     for value in line:
    #         if value == 1:
    #             string += '.'
    #         elif value == 0:
    #             string += '#'
    #     print(string)

    return start_map


def simulate_sand_roads(start_map, sand_source_point):
    number_sand = 0
    actual_map = copy.deepcopy(start_map)
    while True:
        can_move = True
        actual_position = [sand_source_point[0], sand_source_point[1]]

        while can_move:
            x, y = actual_position
            if actual_map[sand_source_point[1]][sand_source_point[0]]!= 1:
                # for line in actual_map:
                #     string = ''
                #     for value in line:
                #         if value == 1:
                #             string += '.'
                #         elif value == 0:
                #             string += '#'
                #         else:
                #             string += 'o'
                #     print(string)
                return number_sand

            if actual_map[y + 1][x] == 1:
                actual_position = [x, y + 1]
            elif actual_map[y + 1][x - 1] == 1:
                actual_position = [x - 1, y + 1]
            elif actual_map[y + 1][x + 1] == 1:
                actual_position = [x + 1, y + 1]
            else:
                actual_map[y][x] = - 1
                can_move = False

        number_sand += 1


filename = "text.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

parser_lines = [parse_line(line) for line in lines]
starter_map = create_start_map(parser_lines)
print(simulate_sand_roads(starter_map, [500, 0]))
