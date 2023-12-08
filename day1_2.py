import string
import re


regex_string = r"(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))"
number_replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def main():
    with open("day1_1_input.txt") as fp:
        lines = fp.readlines()
    
    prog = re.compile(regex_string)

    total = 0
    for line in lines:
        first_digit = None
        last_digit = None
        result = list(prog.finditer(line))
        first_digit = result[0].group(1)
        if len(first_digit) > 1:
            first_digit = number_replacements[first_digit]
        last_digit = result[-1].group(1)
        if len(last_digit) > 1:
            last_digit = number_replacements[last_digit]
        num = int(first_digit + last_digit)
        print(result, num, line)
        total += num
    
    print(total)


if __name__ == '__main__':
    main()
