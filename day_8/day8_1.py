def parse_input(lines):
    directions = parse_directions(lines[0].strip())
    network = parse_network(lines[2:])
    return directions, network


def parse_directions(line):
    directions_map = {
        'L': 0,
        'R': 1,
    }
    directions = []
    for char in line:
        directions.append(directions_map[char])
    return directions


def parse_network(lines):
    network = {}
    for line in lines:
        node, pair = line.split('=')
        left, right = pair.split(',')
        node = node.strip()
        left = left.strip()[1:]
        right = right.strip()[:-1]
        network[node] = (left, right)
    return network


def main():
    with open("day_8/day8_input.txt") as fp:
        lines = fp.readlines()
    # for line in test_input.split('\n'):
    directions, network = parse_input(lines)
    steps = 0
    index = 0
    max = len(directions)
    current_node = 'AAA'
    while True:
        next_direction = directions[index]
        index += 1
        steps += 1
        next_node = network[current_node][next_direction]
        if next_node == 'ZZZ':
            break
        current_node = next_node
        if index >= max:
            index = 0
    print(steps)
        

if __name__ == '__main__':
    main()
