from sys import maxsize

"""
Read each input from file, return the maximum calories
that any single elf is holding. Their consecutive order
is separated by a single empty line.

I was not focused on the most simple and elegant solution,
but one that can solve the problem in one iteration.
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
    max_cals = [-maxsize] * 3  # 3 largest calorie counts

    def replace_max_if_larger(new_val):  # 2-4 comparisons
        # the value in first index will always be <=
        # to the next two values because the list
        # is sorted each time
        if new_val > max_cals[0]:
            max_cals[0] = new_val
        max_cals.sort()

    with open(in_filename) as file_in:
        # count calories held by current elf
        curr_calories = 0
        # each line is a calorie amount or empty new line
        for line in file_in:
            line = line.strip()
            # new line, new elf
            if line == '':
                replace_max_if_larger(curr_calories)
                # increment current elf and reset calories
                curr_calories = 0
            else:
                curr_calories += int(line)
        replace_max_if_larger(curr_calories)

        # check if current elf has higher calories, return max
        return sum(max_cals)


if __name__ == '__main__':
    input_file = 'input.txt'
    print('Part 1: {}'.format(day_01_part_1(input_file)))
    print('Part 2: {}'.format(day_01_part_2(input_file)))
