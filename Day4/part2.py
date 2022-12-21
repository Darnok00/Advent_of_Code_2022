def is_contain(pair):
    pair1, pair2 = pair.split(",")
    startA, endA = pair1.split("-")
    startB, endB = pair2.split("-")

    if int(startA) > int(endB) or int(endA) < int(startB):
        return 0
    else:
        return 1


def count_containing(pairs):
    is_contain_table = [is_contain(pair) for pair in pairs]
    return sum(is_contain_table)


filename = 'text.txt'

with open(filename) as file:
    pairs = [line.rstrip() for line in file]

print(count_containing(pairs))