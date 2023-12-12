example = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''.split('\n')


def parse_seeds(line):
    _, seeds = line.split(':')
    seeds = seeds.strip().split(' ')
    return seeds


def parse_map(data, index):
    map_data = []
    while True:
        try:
            line = data[index].strip()
            index += 1
        except IndexError:
            break
        if line.endswith(":"):
            print("line ends with :")
            continue
        if not line or line.isspace():
            break
        map_data.append(line.split())
    return map_data, index


def number_is_in_range(num: int, start: int, width: int) -> bool:
    # print(f"Checking if {num} is between {start} and {start + width}")
    if num >= start and num < int(start + width):
        # print("It is!")
        return True
    return False


def convert(input_value, map_data):
    for mapping in map_data:
        dest, source, width = mapping
        if number_is_in_range(input_value, int(source), int(width)):
            return int(dest) + (input_value - int(source))
    return input_value

def parse_input(data):
    seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    index = 0
    seeds = parse_seeds(data[index])
    index += 2

    seed_to_soil, index = parse_map(data, index)
    soil_to_fertilizer, index = parse_map(data, index)
    fertilizer_to_water, index = parse_map(data, index)
    water_to_light, index = parse_map(data, index)
    light_to_temperature, index = parse_map(data, index)
    temperature_to_humidity, index = parse_map(data, index)
    humidity_to_location, index = parse_map(data, index)


    return (
        seeds,
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location
    )


def main():
    with open("day_5/day5_input.txt") as fp:
        lines = fp.readlines()

    (
        seeds,
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location
    ) = parse_input(lines)

    soils = []
    for seed in seeds:
        soils.append(convert(int(seed), seed_to_soil))
    
    fertilizers = []
    for soil in soils:
        fertilizers.append(convert(soil, soil_to_fertilizer))

    waters = []
    for fertilizer in fertilizers:
        waters.append(convert(fertilizer, fertilizer_to_water))

    lights = []
    for water in waters:
        lights.append(convert(water, water_to_light))
    
    temperatures = []
    for light in lights:
        temperatures.append(convert(light, light_to_temperature))

    humiditys = []
    for temperature in temperatures:
        humiditys.append(convert(temperature, temperature_to_humidity))
    
    locations = []
    for humidity in humiditys:
        locations.append(convert(humidity, humidity_to_location))
    
    print(min(locations))


if __name__ == '__main__':
    main()
