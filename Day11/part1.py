import copy


NUMBER_ROUND = 20


class Monkey:
    def __init__(self, index, list_items, operator, operation_value, test_number, if_true_index, if_false_index):
        self.index = index
        self.list_items = list_items
        self.operator = operator
        self.operation_value = operation_value
        self.test_number = test_number
        self.if_true_index = if_true_index
        self.if_false_index = if_false_index


def create_init_monkeys_array(lines):
    parsing_lines = [line.split(" ") for line in lines]
    monkey_array = []
    monkey_data = []
    for line in parsing_lines:
        if len(line) == 1:
            continue

        elif line[0] == 'Monkey':
            monkey_data = []
            monkey_data.append(int(line[1][:-1]))

        elif line[2] == 'Starting':
            items_list = []
            elements = line[4:]
            for element in elements:
                item = int(element[:-1]) if element[-1] == ',' else int(element)
                items_list.append(item)
            monkey_data.append(items_list)

        elif line[2] == 'Operation:':
            if line[7] != 'old':
                monkey_data.append(line[6])
                monkey_data.append(int(line[7]))
            else:
                monkey_data.append('**')
                monkey_data.append(2)

        elif line[2] == 'Test:':
            monkey_data.append(int(line[5]))

        elif line[4] == 'If':
            monkey_data.append(int(line[9]))
            if line[5] == 'false:':
                new_monkey = Monkey(monkey_data[0], monkey_data[1], monkey_data[2], monkey_data[3],
                                    monkey_data[4], monkey_data[5], monkey_data[6])
                monkey_array.append(new_monkey)

    return monkey_array


def inspections_for_monkey(monkey, monkey_array):
    list_items = copy.deepcopy(monkey.list_items)
    monkey.list_items = []
    for item in list_items:
        if monkey.operator == '*':
            value = (item * monkey.operation_value) // 3
        elif monkey.operator == '+':
            value = (item + monkey.operation_value) // 3
        else:
            value = (item * item) // 3

        if value % monkey.test_number == 0:
            monkey_array[monkey.if_true_index].list_items.append(value)
        else:
            monkey_array[monkey.if_false_index].list_items.append(value)


def inspect_all_monkey_all_round(monkey_array):
    monkey_operation_counter = [0] * len(monkey_array)
    n = len(monkey_array)
    for i in range(NUMBER_ROUND):
        for j in range(n):
            monkey = monkey_array[j]
            monkey_operation_counter[monkey.index] += len(monkey.list_items)
            inspections_for_monkey(monkey, monkey_array)

    return monkey_operation_counter


filename = "text.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

sorted_array = sorted(inspect_all_monkey_all_round(create_init_monkeys_array(lines)))
print(sorted_array)
print(sorted_array[-1]*sorted_array[-2])
