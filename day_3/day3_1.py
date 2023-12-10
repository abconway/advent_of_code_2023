import re


def main():
    with open("day_3/day3_input.txt") as fp:
        lines = fp.readlines()
    
    prog = re.compile(r"([^0-9\.])")

    cache = []
    # for line in lines:
    #     results = prog.findall(line.rstrip())
    #     print(results)
    line = lines[1]
    index = 0
    while True:
        match = prog.search(line, index)
        print(match)


if __name__ == '__main__':
    main()
