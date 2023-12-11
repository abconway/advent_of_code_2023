def parse_line(line: str):
    found_colon = False
    found_vertical_bar = False
    score = 0
    winning_numbers = set()
    current_number = '' 
    for index, char in enumerate(line):
        if not found_colon:
            if char == ':':
                found_colon = True
            continue
        if not found_vertical_bar:
            if char.isdigit():
                current_number += char
            if char == ' ' and len(current_number) > 0:
                winning_numbers.add(int(current_number))
                current_number = ''
            elif char == '|':
                found_vertical_bar = True
            continue
        if char.isdigit():
            current_number += char
        if (char == ' ' or index == len(line) - 1) and len(current_number) > 0:
            num = int(current_number)
            current_number = ''
            if num in winning_numbers:
                score += 1
    return score


def main():
    with open("day_4/day4_input.txt") as fp:
        lines = fp.readlines()

    scores = {}
    number_of_scratch_cards = {}
    for index, line in enumerate(lines):
        score = parse_line(line)
        scores[index] = score
        number_of_scratch_cards[index] = 1

    for i in range(len(lines)):
        score = scores[i]
        for _ in range(number_of_scratch_cards[i]):
            for j in range(score):
                if i + j + 1 < len(lines):
                    number_of_scratch_cards[i + j + 1] += 1

    print(sum(number_of_scratch_cards.values()))


if __name__ == '__main__':
    main()
