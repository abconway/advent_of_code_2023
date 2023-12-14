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


def rotate_map(space_map):
    rotated = [[] for _ in range(len(space_map[0]))]
    for r, row in enumerate(space_map):
        for c, value in enumerate(row):
            rotated[c].append(value)
    return rotated


def find_empty_columns(space_map):
    rotated_map = rotate_map(space_map)
    return find_empty_rows(rotated_map)


class Range:
    def __init__(self, a, b):
        if a < b:
            self.min = a
            self.max = b
        else:
            self.min = b
            self.max = a
    
    @property
    def width(self):
        return self.max - self.min
    
    def is_in_range(self, x):
        if x >= self.min and x <= self.max:
            return True
        return False


def find_shortest_path(one, two, empty_rows, empty_columns, factor=1):
    r1, c1 = one
    r2, c2 = two
    r_range = Range(r1, r2)
    c_range = Range(c1, c2)
    expansion_additions = 0
    for empty in empty_rows:
        if r_range.is_in_range(empty):
            expansion_additions +=1
    for empty in empty_columns:
        if c_range.is_in_range(empty):
            expansion_additions += 1
    return r_range.width + c_range.width + (expansion_additions * factor)


def find_shortest_paths_sum(galaxies, empty_rows, empty_columns):
    sum = 0
    for i, galaxy in enumerate(galaxies):
        for other_galaxy in galaxies[i + 1:]:
            dist = find_shortest_path(galaxy, other_galaxy, empty_rows, empty_columns)
            sum += dist
    return sum


def main():
    with open("day_11/day11_input.txt") as fp:
        lines = fp.readlines()
    space_map = parse_input(lines)
    galaxies = find_galaxies(space_map)
    empty_rows = find_empty_rows(space_map)
    empty_columns = find_empty_columns(space_map)
    sum = find_shortest_paths_sum(galaxies, empty_rows, empty_columns)
    print(sum)
        
if __name__ == '__main__':
    main()
