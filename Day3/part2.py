def count_for_backpack(bacpack_table1, bacpack_table2, bacpack_table3):

    intersection2_3 = set(bacpack_table2).intersection(bacpack_table3)
    intersection_full = ', '.join(set(bacpack_table1).intersection(intersection2_3))

    ascii_item = ord(str(intersection_full)[0])
    priority_item = ascii_item - 38 if ascii_item < 91 else ascii_item - 96

    return priority_item


def sum_all_priorities(bacpacks_table):
    sum_priority = 0
    for i in range(0,len(bacpacks_table),3):
        sum_priority += count_for_backpack(bacpacks_table[i], bacpacks_table[i+1], bacpacks_table[i+2])
    return sum_priority

filename = 'text.txt'

with open(filename) as file:
    items = [line.rstrip() for line in file]

print(sum_all_priorities(items))
