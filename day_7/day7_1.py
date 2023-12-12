from collections import Counter

test_input = (
"""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
)

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
ranks = ["5OAK", "4OAK", "FULL", "3OAK", "2PAIR", "PAIR", "HIGH"]
hands_cache = {rank: [] for rank in ranks}


def parse_line(line):
    return line.split()


def classify_hand_rank(hand):
    c = Counter(hand)
    most_common = c.most_common(1)[0][1]
    if most_common == 5:
        return "5OAK"
    if most_common == 4:
        return "4OAK"
    if most_common == 3:
        next_most_common = c.most_common(2)[1][1]
        if next_most_common == 2:
            return "FULL"
        return "3OAK"
    if most_common == 2:
        next_most_common = c.most_common(2)[1][1]
        if next_most_common == 2:
            return "2PAIR"
        return "PAIR"
    return "HIGH"


def main():
    with open("day_7/day7_input.txt") as fp:
        lines = fp.readlines()
    for line in test_input.split('\n'):
        line = line.strip()
        if line:
            hand, bid = parse_line(line)
            rank = classify_hand_rank(hand)
            hands_cache[rank].append((hand, bid))
    print(hands_cache)


if __name__ == '__main__':
    main()
