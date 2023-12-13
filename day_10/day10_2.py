s = '7'
s_location = (83, 25)
movements = {
    'up': {
        "|": (True, (-1, 0), "up"),
        "-": (False, (), None),
        "L": (False, (), None),
        "J": (False, (), None),
        "7": (True, (0, -1), "left"),
        "F": (True, (0, 1), "right"),
        ".": (False, (), None),
    },
    'down': {
        "|": (True, (1, 0), "down"),
        "-": (False, (), None),
        "L": (True, (0, 1), "right"),
        "J": (True, (0, -1), "left"),
        "7": (False, (), None),
        "F": (False, (), None),
        ".": (False, (), None),
    },
    'left': {
        "|": (False, (), None),
        "-": (True, (0, -1), "left"),
        "L": (True, (-1, 0), "up"),
        "J": (False, (), None),
        "7": (False, (), None),
        "F": (True, (1, 0), "down"),
        ".": (False, (), None),
    },
    'right': {
        "|": (False, (), None),
        "-": (True, (0, 1), "right"),
        "L": (False, (), None),
        "J": (True, (-1, 0), "up"),
        "7": (True, (1, 0), "down"),
        "F": (False, (), None),
        ".": (False, (), None),
    },
}


def parse_input(lines):
    diagram = []
    for line in lines:
        diagram.append(list(line.strip()))
    return diagram


def find_s(diagram):
    for r, row in enumerate(diagram):
        for c, column in enumerate(row):
            if column == 'S':
                return (r, c)
    return None


def get_next_location(current, move):
    r, c = current
    dr, dc = move
    return (r + dr, c + dc)


def find_loop(diagram, start, s):
    loop = [start]
    current_location = start  # (83, 25)
    current_tile = s  # '7'
    current_direction = 'down'
    current_move = (1, 0)
    while True:
        next_location = get_next_location(current_location, current_move)
        r, c = next_location
        next_tile = diagram[r][c]
        if next_tile == 'S':
            break
        possible, next_move, next_direction = movements[current_direction][next_tile]
        loop.append(next_location)
        current_location = next_location
        current_tile = next_tile
        current_direction = next_direction
        current_move = next_move
    return loop


def paint_diagram(diagram, loop):
    for r, c in loop:
        diagram[r][c] = '*'
    return diagram


def shoelace_formula(polygonBoundary, absoluteValue = True):
    nbCoordinates = len(polygonBoundary)
    nbSegment = nbCoordinates - 1

    l = [(polygonBoundary[i+1][0] - polygonBoundary[i][0]) * (polygonBoundary[i+1][1] + polygonBoundary[i][1]) for i in range(nbSegment)]

    if absoluteValue:
        return abs(sum(l) / 2.)
    else:
        return sum(l) / 2.



def main():
    with open("day_10/day10_input.txt") as fp:
        lines = fp.readlines()
    diagram = parse_input(lines)
    # print(diagram)
    # print(find_s(diagram))
    loop = find_loop(diagram, s_location, s)
    # painted_diagram = paint_diagram(diagram, loop)
    # for row in diagram:
    #     print(''.join(row))
    area = int(shoelace_formula(loop))
    i = area + 1 - len(loop)//2
    print(i)

        

if __name__ == '__main__':
    main()
