from sys import maxsize

"""
Read each input from file, return the maximum calories
that any single elf is holding. Their consecutive order
is separated by a single empty line.
"""


def day_01(in_filename):
    # amount carried by the current richest elf
    max_calories = -maxsize

    with open(in_filename) as file_in:
        # count calories held by current elf
        curr_calories = 0
        # each line is a calorie amount or empty new line
        for line in file_in:
            line = line.strip()
            # new line, new elf
            if line == '':
                if curr_calories > max_calories:
                    max_calories = curr_calories
                # increment current elf and reset calories
                curr_calories = 0
            else:
                curr_calories += int(line)
        # check if current elf has higher calories, return max
        return max(max_calories, curr_calories)


if __name__ == '__main__':
    input_file = 'input.txt'
    print('Part1: {}'.format(day_01(input_file)))
