
class Node:
    def __init__(self, parent=None, childs=None, size=0, name=None, type=None):
        self.parent = parent
        self.childs = childs
        self.name = name
        self.size = size
        self.type = type

    def add_child(self, child):
        self.childs.append(child)

    def ls(self, elements):
        if self.childs is None:
            self.childs = []
        for element in elements:
            if element[0] == 'dir':
                child = Node(parent=self, name=element[1], type='dir')
            else:
                child = Node(parent=self, name=element[1], size=int(element[0]), type='file')
            self.add_child(child)

    def cd(self, name):
        if name == "..":
            return self.parent
        else:
            for child in self.childs:
                if child.name == name:
                    return child


def processing_lines(lines):
    actual_Node = Node(name="/", type='dir')
    parent = actual_Node
    lines = lines[1:]
    childs = []

    for i in range(len(lines)):
        split_line = lines[i].split(" ")
        if split_line[0] == '$':
            if len(childs) > 0:
                actual_Node.ls(childs)
                childs = []

            if split_line[1] == 'cd':
                actual_Node = actual_Node.cd(split_line[2])
        else:
            childs.append(split_line)

    if len(childs) > 0:
        actual_Node.ls(childs)

    return parent

def compare_size(directory):
    dir_size = 0
    for child in directory.childs:
        if child.type == 'dir':
            child.size = compare_size(child)
        dir_size += child.size

    return dir_size


def find_size(parent):
    total_size = parent.size
    empty_space = 70000000 - total_size
    space_needed = 30000000 - empty_space
    return space_needed

def create_size_array(parent, array, size):
    for child in parent.childs:
        if child.type == 'dir':
            if child.size >= size:
                array.append(child.size)
            create_size_array(child, array, size)
    if parent.name == '/':
        return array


filename = "text.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

parent = processing_lines(lines)
parent.size = compare_size(parent)
print(min(create_size_array(parent, [], find_size(parent))))

