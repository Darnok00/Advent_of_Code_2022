def find_the_most_calories(calories_table):
    max_kcal = -1
    actual_max = 0

    for element in calories_table:
        if element != '':
            actual_max += int(element)
        else:
            if max_kcal < actual_max:
                max_kcal = actual_max
            actual_max = 0

    return max_kcal


filename = "text.txt"

with open(filename) as file:
    calories = [line.rstrip() for line in file]

print(find_the_most_calories(calories))


