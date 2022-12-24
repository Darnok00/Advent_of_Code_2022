def power_signals(commands):
    commands = [command.split(" ") for command in commands]
    number_cycles = 0
    actual_power_signal = 1
    string = ''
    designated_cycles = [40, 80, 120, 160, 200, 240]

    for command in commands:
        type = command[0]
        number_cycles += 1
        pixel_position = number_cycles - 1
        ghost_table = [actual_power_signal - 1, actual_power_signal, actual_power_signal + 1]
        if pixel_position % 40 in ghost_table:
            string += "█"
        else:
            string += ' '
        if pixel_position % 40 == 39:
            print(string)
            string = ''

        if type == 'addx':
            number_cycles += 1
            pixel_position = number_cycles - 1
            ghost_table = [actual_power_signal - 1, actual_power_signal, actual_power_signal + 1]
            if pixel_position % 40 in ghost_table:
                string += "█"
            else:
                string += ' '
            if pixel_position % 40 == 39:
                print(string)
                string = ''

            actual_power_signal += int(command[1])

filename = "text.txt"

with open(filename) as file:
    commands = [line.rstrip() for line in file]

power_signals(commands)