MAXIMUMS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def main():
    with open("day2_1_input.txt") as fp:
        lines = fp.readlines()
    
    game_number = 1
    game_sum = 0
    for line in lines:
        possible = True
        _, game = line.split(":")
        pulls = game.split(";")
        for pull in pulls:
            print("Pull: ", pull)
            colors = pull.split(",")
            for single_color in colors:
                num, color = single_color.split()
                num = int(num)
                color = color.strip()
                if num > MAXIMUMS[color]:
                    possible = False
                    print("Not possible")
        if possible:
            game_sum += game_number
        game_number += 1
    
    print(game_sum)



if __name__ == '__main__':
    main()
