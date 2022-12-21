def calculate_points(data):
    counting_rules = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6
    }
    points = 0
    for match in data:
        points += counting_rules[match]

    return points


filename = 'text.txt'

with open(filename) as file:
    matches = [line.rstrip() for line in file]


print(calculate_points(matches))