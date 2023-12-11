import re


def read_number(line: str, index: int) -> int:
    starting_index = index
    num_string = ''
    while True:
        value = line[index]
        if not value.isdigit():
            break
        num_string += value
        index += 1
    return (int(num_string), starting_index, index)


def read_number_to_left(line: str, index: int):
    number_string = ''
    tmp_index = index
    while tmp_index >= 0:
        next_character = line[tmp_index]
        if next_character.isdigit():
            number_string = next_character + number_string
            tmp_index -= 1
            continue
        break
    return number_string


def read_number_to_right(line: str, index: int):
    number_string = ''
    tmp_index = index
    while tmp_index < len(line):
        next_character = line[tmp_index]
        if next_character.isdigit():
            number_string =  number_string + next_character
            tmp_index += 1
            continue
        break
    return number_string


def read_number_to_left_and_right(line: str, index: int):
    number_string = read_number_to_left(line, index)
    number_string += read_number_to_right(line, index + 1)
    return number_string

        

def main():
    with open("day_3/day3_input.txt") as fp:
        lines = fp.readlines()

    sum = 0
    for row, line in enumerate(lines):
        line = line.rstrip()
        column = 0
        current_number = ''
        while column < len(line):
            value = line[column]
            if value == '.':
                current_number = ''
            elif value.isdigit():
                current_number += value
            elif value == '*':  # a symbol!
                numbers_found = []
                print("Found a symbol: ", value)
                # Did we just finish a number to the right?
                if len(current_number) > 0:
                    print("Adding number: ", current_number)
                    # sum += int(current_number)
                    numbers_found.append(int(current_number))
                    current_number = ''
                # check for a numbers above
                if (row - 1) >= 0:
                    above_row = lines[row - 1].rstrip()
                    # Check directly above
                    above_number = above_row[column]
                    if above_number.isdigit():
                        above_number = read_number_to_left_and_right(above_row, column)
                        print("Adding number: ", above_number)
                        # sum += int(above_number)
                        numbers_found.append(int(above_number))
                    else:
                        # check above left for a number
                        if (column - 1) >= 0:
                            above_number = above_row[column - 1]
                            if above_number.isdigit():
                                # read left for number
                                above_number = read_number_to_left(above_row, column - 1)
                                # sum += int(above_number)
                                numbers_found.append(int(above_number))
                                print("Adding number: ", above_number)
                                above_number = ''
                        # check above right for a number
                        if (column + 1) < len(above_row):
                            above_number = above_row[column + 1]
                            if above_number.isdigit():
                                # read right for number
                                above_number = read_number_to_right(above_row, column + 1)
                                # sum += int(above_number)
                                numbers_found.append(int(above_number))
                                print("Adding number: ", above_number)
                                above_number = ''
                # check for numbers below
                if (row + 1) < len(lines):
                    below_row = lines[row + 1].rstrip()
                    # check directly below
                    below_number = below_row[column]
                    if below_number.isdigit():
                        below_number = read_number_to_left_and_right(below_row, column)
                        print("Adding number: ", below_number)
                        # sum += int(below_number)
                        numbers_found.append(int(below_number))
                    else:
                        # check below left for a number
                        if (column - 1) >= 0:
                            below_number = below_row[column - 1]
                            if below_number.isdigit():
                                # read left for number
                                below_number = read_number_to_left(below_row, column - 1)
                                # sum += int(below_number)
                                numbers_found.append(int(below_number))
                                print("Adding number: ", below_number)
                                below_number = ''
                        # check below right for a number
                        if (column + 1) < len(below_row):
                            below_number = below_row[column + 1]
                            if below_number.isdigit():
                                # read right for number
                                below_number = read_number_to_right(below_row, column + 1)
                                # sum += int(below_number)
                                numbers_found.append(int(below_number))
                                print("Adding number: ", below_number)
                                below_number = ''
                # check for a number to the right
                if (column + 1) < len(line):
                    number_to_right = line[column + 1]
                    if number_to_right.isdigit():
                        tmp_index = column + 2
                        while tmp_index < len(line):
                            next_character = line[tmp_index]
                            if next_character.isdigit():
                                number_to_right = number_to_right + next_character
                                tmp_index += 1
                                continue
                            break
                        print("Adding number: ", number_to_right)
                        # sum += int(number_to_right)
                        numbers_found.append(int(number_to_right))
                        number_to_right = ''
                        column = tmp_index
                        print(numbers_found)
                        if len(numbers_found) == 2:
                            product = int(numbers_found[0]) * int(numbers_found[1])
                            sum += product
                        continue
                print(numbers_found)
                if len(numbers_found) == 2:
                    product = int(numbers_found[0]) * int(numbers_found[1])
                    sum += product
            column += 1

    print(sum)



if __name__ == '__main__':
    main()
