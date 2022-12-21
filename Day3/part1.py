
def count_for_backpack(bacpack_table):
    n = len(bacpack_table)
    part1 = bacpack_table[: n//2]
    part2 = bacpack_table[ n//2:]

    item = ', '.join(set(part1).intersection(part2))
    ascii_item = ord(str(item)[0])
    priority_item = ascii_item - 38 if ascii_item < 91 else ascii_item - 96

    return priority_item


def sum_all_priorities(bacpacks_table):
    priority_table = [count_for_backpack(bacpack_table) for bacpack_table in bacpacks_table]
    return sum(priority_table)

filename = 'text.txt'

with open(filename) as file:
    items = [line.rstrip() for line in file]

print(sum_all_priorities(items))
