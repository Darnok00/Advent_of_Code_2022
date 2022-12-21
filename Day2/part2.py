def calculate_points(data):
    counting_rules = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7
    }
    points = 0
    for match in data:
        points += counting_rules[match]

    return points


filename = 'text.txt'

with open(filename) as file:
    matches = [line.rstrip() for line in file]


print(calculate_points(matches))