def processing_lines(lines):
    line = lines[0]
    i = 0

    while line[1] != '1':
        i += 1
        line = lines[i]

    height = i
    width = int(line[-1])

    stacks = []
    for x in range(width):
        stacks.append([])

    for i in range(height-1,-1,-1):
        line = lines[i]
        for j in range(1,4*width-2,4):
            if line[j] != ' ':
                stacks[j//4].append(line[j])

    return stacks

def moves(lines):
    stacks = processing_lines(lines)

    for line in lines:
        elements = line.split(" ")
        if elements[0] != 'move':
            continue

        number, resource, destination = elements[1], elements[3], elements[5]
        number = int(number)
        while number != 0:
            stacks[int(destination)-1].append(stacks[int(resource)-1].pop())
            number -= 1

    elements_on_top = [stack[-1] for stack in stacks]
    return elements_on_top


filename = 'text.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

print(('').join(moves(lines)))
