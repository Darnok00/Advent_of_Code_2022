import copy
from dijkstar import Graph, find_path


def create_height_map(lines):
    height_map = []
    start_points = []

    for line in lines:
        height_map.append([])
        for letter in line:
            if letter == 'S' or letter == 'a':
                value = 0
                start_points.append([len(height_map[-1]), len(height_map) - 1])
            elif letter == 'E':
                value = 25
                end_point = [len(height_map[-1]), len(height_map) - 1]
            else:
                value = ord(letter) - 97
            height_map[-1].append(value)

    return height_map, start_points, end_point


def possible_moves(height_map, actual_position):
    moves_array = [False] * 4
    x, y = actual_position[0], actual_position[1]
    # move right
    if x != len(height_map[0]) - 1 and (height_map[y][x + 1] - height_map[y][x]) <= 1:
        moves_array[0] = True
    # move left
    if x != 0 and (height_map[y][x - 1] - height_map[y][x]) <= 1:
        moves_array[1] = True
    # move up
    if y != 0 and (height_map[y - 1][x] - height_map[y][x]) <= 1:
        moves_array[2] = True
    # move doww
    if y != len(height_map) - 1 and (height_map[y + 1][x] - height_map[y][x]) <= 1:
        moves_array[3] = True

    return moves_array


def create_graph_roads(height_map):
    graph_roads = Graph()
    n = len(height_map)
    m = len(height_map[0])
    for i in range(n):
        for j in range(m):
            index = m * i + j
            actual_position = [j, i]
            possibilities = copy.deepcopy(possible_moves(height_map, actual_position))
            if possibilities[0]:
                graph_roads.add_edge(index, index + 1, 1)
            if possibilities[1]:
                graph_roads.add_edge(index, index - 1, 1)
            if possibilities[2]:
                graph_roads.add_edge(index, index - m, 1)
            if possibilities[3]:
                graph_roads.add_edge(index, index + m, 1)

    return graph_roads


def find_the_best_road(graph_roads, start_points, end_point, m):
    end_index = end_point[1] * m + end_point[0]
    best_roads_values = []
    for start_point in start_points:
        start_index = start_point[1] * m + start_point[0]
        try:
            best_roads_values.append(find_path(graph_roads, start_index, end_index)[-1])
        except:
            continue

    return min(best_roads_values)


filename = "text.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

height_map, start_point, end_point = create_height_map(lines)
graph = create_graph_roads(height_map)
m = len(height_map[0])
print(find_the_best_road(graph, start_point, end_point, m))
