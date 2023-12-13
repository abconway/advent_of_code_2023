test_input = [
    "0 3 6 9 12 15\n",
    "1 3 6 10 15 21\n",
    "10  13  16  21  30  45\n",
]


def parse_input(data):
    sequences = []
    for line in data:
        raw_sequence = line.strip().split()
        sequence = []
        for item in raw_sequence:
            sequence.append(int(item))
        sequences.append(sequence)
    return sequences


def is_zeros(sequence):
    for item in sequence:
        if item != 0:
            return False
    return True


def get_differences(sequence):
    differences = []
    for i in range(1, len(sequence)):
        differences.append(sequence[i] - sequence[i - 1])
    return differences


def get_prediction(sequence):
    index = len(sequence) - 2
    while index > 0:
        num = sequence[index][0]
        next_num = sequence[index - 1][0]
        sequence[index - 1].insert(0, next_num - num)
        index -= 1
    # print(sequence)
    return sequence[0][0]


def get_sequence_predictions(sequences):
    predictions = []
    for sequence in sequences:
        sequence = [sequence]
        while True:
            differences = get_differences(sequence[-1])
            sequence.append(differences)
            if is_zeros(differences):
                break
        # print(sequence)
        predictions.append(get_prediction(sequence))
    return predictions


def main():
    with open("day_9/day9_input.txt") as fp:
        lines = fp.readlines()
    sequences = parse_input(lines)
    # sequences = parse_input(test_input)
    predictions = get_sequence_predictions(sequences)
    print(sum(predictions))
        
        

if __name__ == '__main__':
    main()
