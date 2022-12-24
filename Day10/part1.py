def power_signals(commands):
    commands = [command.split(" ") for command in commands]
    number_cycles = 0
    actual_power_signal = 1
    total_power_signal = 0
    designated_cycles = [20, 60, 100, 140, 180, 220]

    for command in commands:
        type = command[0]
        number_cycles += 1
        if number_cycles in designated_cycles:
            total_power_signal += actual_power_signal*number_cycles

        if type == 'addx':
            number_cycles += 1
            if (number_cycles) in designated_cycles:
                total_power_signal += (number_cycles) * actual_power_signal
            actual_power_signal += int(command[1])

    return total_power_signal


filename = "text.txt"

with open(filename) as file:
    commands = [line.rstrip() for line in file]

print(power_signals(commands))