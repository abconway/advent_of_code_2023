def parse_line(line: str):
    found_colon = False
    found_vertical_bar = False
    found_first_score = False
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
                if not found_first_score:
                    score = 1
                    found_first_score = True
                else:
                    score *= 2
    return score


def main():
    with open("day_4/day4_input.txt") as fp:
        lines = fp.readlines()

    total_score = 0
    for index, line in enumerate(lines):
        score = parse_line(line)
        total_score += score
    
    print(total_score)


if __name__ == '__main__':
    main()
