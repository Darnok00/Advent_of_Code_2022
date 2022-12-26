import copy


def parse_line(line):
    stack = []
    for i in range(len(line)):
        mark = line[i]
        if mark == '[':
            stack.append(mark)
        elif mark == ']':
            temp_aray = []
            while stack[-1] != '[':
                temp_aray.append(stack.pop())
            temp_aray = temp_aray[::-1]
            stack.pop()
            stack.append(temp_aray)
        elif mark != ',':
            if line[i+1] != ',' and line[i+1] != ']':
                mark += line[i+1]
                i += 1
            stack.append(int(mark))

    return stack[0]


def compare_two_integer(left, right):
    if left < right:
        return 1
    if left == right:
        return 0
    if left > right:
        return -1


# 0 - 2 List, 1 - Left is list - Right is int, 2 - Left is int - Right is list, 3 - 2 Integer
def get_result_compare(left_element, right_element):
    if isinstance(left_element, list) and isinstance(right_element, list):
        result = compare_two_list(left_element, right_element)
    elif isinstance(left_element, list):
        result = compare_two_list(left_element, [right_element])
    elif isinstance(right_element, list):
        result = compare_two_list([left_element], right_element)
    else:
        result = compare_two_integer(left_element, right_element)

    return result


def compare_two_list(left, right):
    l = len(left)
    r = len(right)
    size = min(l, r)
    for i in range(size):
        left_element, right_element = left[i], right[i]
        result_compare = get_result_compare(left_element, right_element)
        if abs(result_compare) == 1:
            return result_compare
    if l < r:
        return 1
    elif l > r:
        return -1
    else:
        return 0


def compare_pairs(lines):
    compare_array = []
    for i in range(0,len(lines),3):
        left = parse_line(lines[i])
        right = parse_line(lines[i+1])
        if compare_two_list(left, right) == 1:
            compare_array.append(i//3 + 1)

    return compare_array


filename = "text.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

print(sum(compare_pairs(lines)))
