import math


def main():
    with open("day2_1_input.txt") as fp:
        lines = fp.readlines()
    
    power_sum = 0
    for line in lines:
        maximums = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        _, game = line.split(":")
        pulls = game.split(";")
        for pull in pulls:
            print("Pull: ", pull)
            colors = pull.split(",")
            for single_color in colors:
                num, color = single_color.split()
                num = int(num)
                color = color.strip()
                if num > maximums[color]:
                    maximums[color] = num
        game_power = math.prod(maximums.values())
        power_sum += game_power
    
    print(power_sum)



if __name__ == '__main__':
    main()
