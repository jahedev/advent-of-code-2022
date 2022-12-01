from sys import maxsize

"""
Read each input from file, return the maximum calories
that any single elf is holding. Their consecutive order
is separated by a single empty line.
"""


def day_01_part_1(in_filename):
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


def day_01_part_2(in_filename):
    # the elf who carries the most calories
    richest_elf = -1
    # amount carried by the current richest elf
    max_calories = -maxsize

    with open(in_filename) as file_in:
        curr_elf = 1
        curr_calories = 0
        for line in file_in:
            line = line.strip()
            # new line, new elf
            if line == '':
                curr_elf += 1
                if curr_calories > max_calories:
                    max_calories = curr_calories
                    richest_elf = curr_elf
                # increment current elf and reset calories
                curr_elf += 1
                curr_calories = 0
            else:
                curr_calories += int(line)
        # check once more for the last elf, return richest
        return curr_elf if curr_calories > max_calories else richest_elf


if __name__ == '__main__':
    input_file = 'input.txt'
    print('Part1: {}'.format(day_01_part_1(input_file)))
