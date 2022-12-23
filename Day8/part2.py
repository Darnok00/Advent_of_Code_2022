def create_vertical_lines(horizontal_lines):
    vertical_lines = []
    number_horizontal_lines = len(horizontal_lines)
    number_vertical_lines = len(horizontal_lines[0])
    for i in range(number_vertical_lines):
        vertical_lines.append([])
        for j in range(number_horizontal_lines):
            vertical_lines[-1].append(horizontal_lines[j][i])

    return vertical_lines


def search_best_point_value(vertical_lines, horizontal_lines):
    n = len(horizontal_lines)
    m = len(vertical_lines)
    best_value = 0

    for i in range(n):
        for j in range(m):
            down_sum, up_sum, left_sum, right_sum = 0,0,0,0
            vertical_line, horizontal_line = vertical_lines[j], horizontal_lines[i]
            for index in range(i+1, n, 1):
                down_sum += 1
                if vertical_line[i] <= vertical_line[index]:
                    break
            for index in range(i-1, -1, -1):
                up_sum += 1
                if vertical_line[i] <= vertical_line[index]:
                    break

            for index in range(j+1, m, 1):
                right_sum += 1
                if horizontal_line[j] <= horizontal_line[index]:
                    break
            for index in range(j-1, -1, -1):
                left_sum += 1
                if horizontal_line[j] <= horizontal_line[index]:
                    break

            actual_value = down_sum*left_sum*up_sum*right_sum
            if best_value < actual_value:
                best_value = actual_value

    return best_value


filename = "text.txt"

with open(filename) as file:
    horizontal_lines = [line.rstrip() for line in file]

print(search_best_point_value(create_vertical_lines(horizontal_lines), horizontal_lines))
