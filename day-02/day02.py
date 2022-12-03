

def day_01_part_1(in_filename):
    X, Y, Z = 1, 2, 3
    WIN, DRAW, LOSE = 6, 3, 0
    outcomes = {
        'A X': X+DRAW,
        'A Y': Y+WIN,
        'A Z': Z+LOSE,
        'B X': X+LOSE,
        'B Y': Y+DRAW,
        'B Z': Z+WIN,
        'C X': X+WIN,
        'C Y': Y+LOSE,
        'C Z': Z+DRAW,
    }

    matches = []
    with open(in_filename) as file_in:
        matches = [line.strip() for line in file_in]  # list of first char

    total = 0
    for match in matches:
        total += outcomes[match]

    return total


if __name__ == '__main__':
    input_file = 'input.txt'
    print('Part 1: {}'.format(day_01_part_1(input_file)))
