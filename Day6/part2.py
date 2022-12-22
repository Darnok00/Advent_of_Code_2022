def check_repetition(chars):
    chars = ''.join(sorted(chars))
    for i in range(13):
        if chars[i] == chars[ i +1]:
            return False
    return True


def find_first_mark(string):

    for i in range(13, len(string), 1):
        chars = string[i - 13: i +1]
        if check_repetition(chars):
            return i+1


filename = 'text.txt'

with open(filename) as file:
    string = [line.rstrip() for line in file]

print(find_first_mark(string[0]))
