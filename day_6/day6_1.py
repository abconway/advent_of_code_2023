def parse_line(line):
    _, times = line.split(":")
    times = times.split()
    return [int(time.strip()) for time in times]


def parse_input(data):
    times = parse_line(data[0])
    distances = parse_line(data[1])
    return list(zip(times, distances))


def calc_number_of_winning_plays(t, d):
    winning_plays = 0
    for speed in range(1, t):
        test_distance = speed * (t - speed)
        if test_distance > d:
            winning_plays += 1
    return winning_plays


def main():
    with open("day_6/day6_input.txt") as fp:
        lines = fp.readlines()
    wins_product = 1
    for time, distance in parse_input(lines):
        wins_product *= calc_number_of_winning_plays(time, distance)
    print(wins_product)



if __name__ == '__main__':
    main()
