import string


def main():
    with open("day1_1_input.txt") as fp:
        lines = fp.readlines()
    
    total = 0
    for line in lines:
        first_digit = None
        last_digit = None
        for i in line:
            if i in string.digits:
                first_digit = i
                break
        for i in line[::-1]:
            if i in string.digits:
                last_digit = i
                break
        num = int(first_digit + last_digit)
        print(line, num)
        total += num
    
    print(total)


if __name__ == '__main__':
    main()
