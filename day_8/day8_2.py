def parse_input(lines):
    directions = parse_directions(lines[0].strip())
    network, starting_nodes, ending_nodes = parse_network(lines[2:])
    return directions, network, starting_nodes, ending_nodes


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
    starting_nodes = set()
    ending_nodes= set()
    for line in lines:
        node, pair = line.split('=')
        left, right = pair.split(',')
        node = node.strip()
        left = left.strip()[1:]
        right = right.strip()[:-1]
        network[node] = (left, right)
        if node.endswith('A'):
            starting_nodes.add(node)
        elif node.endswith('Z'):
            ending_nodes.add(node)
    return network, starting_nodes, ending_nodes


def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
 
# recursive implementation
def lcm_array(arr, idx):
   
    # lcm(a,b) = (a*b/gcd(a,b))
    if (idx == len(arr)-1):
        return arr[idx]
    a = arr[idx]
    b = lcm_array(arr, idx+1)
    return int(a*b/gcd(a,b)) # __gcd(a,b) is inbuilt library function


def main():
    with open("day_8/day8_input.txt") as fp:
        lines = fp.readlines()
    # for line in test_input.split('\n'):
    directions, network, starting_nodes, ending_nodes = parse_input(lines)
    
    # find the cycle length for each starting node
    cycle_length = dict()
    for starting_node in starting_nodes:
        steps = 0
        index = 0
        max = len(directions)
        current_node = starting_node
        while True:
            next_direction = directions[index]
            index += 1
            steps += 1
            next_nodes = []
            next_node = network[current_node][next_direction]
            if next_node in ending_nodes:
                break
            current_node = next_node
            if index >= max:
                index = 0
        cycle_length[starting_node] = steps
    print(cycle_length)
    lengths = list(cycle_length.values())
    lcm = lcm_array(lengths, 0)
    print(lcm)
        

if __name__ == '__main__':
    main()
