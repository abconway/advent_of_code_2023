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
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,
}
ranks = ["5OAK", "4OAK", "FULL", "3OAK", "2PAIR", "PAIR", "HIGH"]
hands_cache = {rank: [] for rank in ranks}


def parse_line(line):
    return line.split()


def classify_hand_rank(hand):
    if hand == 'JJJJJ':
        return '5OAK'
    c = Counter(hand)
    jokers = c.pop('J', 0)
    most_common = c.most_common(1)[0][1]
    if most_common == 5:
        return "5OAK"
    if most_common == 4:
        if jokers:
            return "5OAK"
        return "4OAK"
    if most_common == 3:
        if jokers:
            if jokers == 2:
                return '5OAK'
            return '4OAK'
        next_most_common = c.most_common(2)[1][1]
        if next_most_common == 2:
            return "FULL"
        return "3OAK"
    if most_common == 2:
        if jokers:
            if jokers == 3:
                return '5OAK'
            elif jokers == 2:
                return '4OAK'
        next_most_common = c.most_common(2)[1][1]
        if next_most_common == 2:
            if jokers:
                return 'FULL'
            return "2PAIR"
        if jokers:
            return '3OAK'
        return "PAIR"
    if jokers:
        if jokers == 4:
            return '5OAK'
        elif jokers == 3:
            return '4OAK'
        elif jokers == 2:
            return '3OAK'
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
