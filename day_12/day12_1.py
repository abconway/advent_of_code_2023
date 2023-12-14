def parse_input(data):
    springs = []
    for line in data:
        conditions, counts = line.split(' ')
        int_counts = [
            int(count)
            for count in counts.strip().split(',')
        ]
        springs.append((list(conditions), int_counts))
    return springs


def get_unknowns(conditions):
    num = 0
    for char in conditions:
        if char == '?':
            num += 1
    return num


def calculate_arrangements(spring):
    conditions, counts = spring
    print(conditions)
    print(counts)
    unknowns = get_unknowns(conditions)
    print(unknowns)
    print(sum(counts))
    for count in counts:
        index = 0


def main():
    with open("day_12/day12_input.txt") as fp:
        lines = fp.readlines()
    springs = parse_input(lines)
    # print(springs)
    for spring in springs:
        pass
    calculate_arrangements(springs[0])


        
if __name__ == '__main__':
    main()
