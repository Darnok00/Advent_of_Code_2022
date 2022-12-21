def find_three_the_most_calories(calories_table):
    actual_max = 0
    max_table = []

    for element in calories_table:
        if element != '':
            actual_max += int(element)
        else:
            if len(max_table) < 3:
                max_table.append(actual_max)
            else:
                actual_min_table = min(max_table)
                if actual_max > actual_min_table:
                    index = max_table.index(actual_min_table)
                    max_table[index] = actual_max
            actual_max = 0
    return sum(max_table)


filename = "text.txt"

with open(filename) as file:
    calories = [line.rstrip() for line in file]

print(find_three_the_most_calories(calories))


