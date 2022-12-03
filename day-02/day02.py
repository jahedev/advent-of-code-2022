WINN, DRAW, LOSE = 6, 3, 0
X, Y, Z = 1, 2, 3

outcomes = {
    'A X': X+DRAW, 'A Y': Y+WINN, 'A Z': Z+LOSE,
    'B X': X+LOSE, 'B Y': Y+DRAW, 'B Z': Z+WINN,
    'C X': X+WINN, 'C Y': Y+LOSE, 'C Z': Z+DRAW,
}


def day_02_part_1(in_filename):
    matches = []
    with open(in_filename) as file_in:
        matches = [line.strip() for line in file_in]
    total = 0
    for match in matches:
        total += outcomes[match]
    return total


def day_02_part_2(in_filename):
    new_outcomes = {
        'A X': outcomes['A Z'], 'A Y': outcomes['A X'], 'A Z': outcomes['A Y'],
        'B X': outcomes['B X'], 'B Y': outcomes['B Y'], 'B Z': outcomes['B Z'],
        'C X': outcomes['C Y'], 'C Y': outcomes['C Z'], 'C Z': outcomes['C X'],
    }
    matches = []
    with open(in_filename) as file_in:
        matches = [line.strip() for line in file_in]
    total = 0
    for match in matches:
        total += new_outcomes[match]
    return total


if __name__ == '__main__':
    input_file = 'input.txt'
    print('Part 1: {}'.format(day_02_part_1(input_file)))
    print('Part 2: {}'.format(day_02_part_2(input_file)))
