def parse_input(data):
    output = []
    for line in data:
        output.append(list(line))
    return output


def find_galaxies(space_map):
    galaxies = []
    for r, row in enumerate(space_map):
        for c, value in enumerate(row):
            if value == '#':
                galaxies.append((r, c))
    return galaxies


def find_empty_rows(space_map):
    empty_rows = {}
    for r, row in enumerate(space_map):
        empty = True
        for char in row:
            if char == '#':
                empty = False
                break
        if empty:
            empty_rows[r] = True
    return empty_rows


def main():
    with open("day_11/day11_input.txt") as fp:
        lines = fp.readlines()
    space_map = parse_input(lines)
    galaxies = find_galaxies(space_map)
    # print(galaxies)
    empty_rows = find_empty_rows(space_map)
    print(empty_rows.keys())

        
if __name__ == '__main__':
    main()
