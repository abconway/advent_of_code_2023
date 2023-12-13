from collections import Counter
from functools import cmp_to_key


test_input = (
"""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
)

cards = {
    "A": 12, 
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}
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


def compare_hands(hand1, hand2):
    index = 0
    while index < 5:
        card1 = hand1[0][index]
        card2 = hand2[0][index]
        card1_value = cards[card1]
        card2_value = cards[card2]
        if card1_value == card2_value:
            index += 1
            continue
        if card1_value < card2_value:
            return -1
        return 1

def sort_hands(hands):
    return sorted(hands, key=cmp_to_key(compare_hands))


def main():
    with open("day_7/day7_input.txt") as fp:
        lines = fp.readlines()
    # for line in test_input.split('\n'):
    for line in lines:
        line = line.strip()
        if line:
            hand, bid = parse_line(line)
            rank = classify_hand_rank(hand)
            hands_cache[rank].append((hand, bid))
    total_winnings = 0
    hand_rank = 1
    for rank in reversed(ranks):
        hands = sort_hands(hands_cache[rank])
        for _, bid in hands:
            total_winnings += hand_rank * int(bid)
            hand_rank += 1
    print("Total winnings: ", total_winnings)


if __name__ == '__main__':
    main()
