def parse_seeds(line):
    _, seeds = line.split(':')
    seeds = seeds.strip().split(' ')
    seed_pairs = []
    current_pair = []
    for seed in seeds:
        current_pair.append(seed)
        if len(current_pair) == 2:
            seed_pairs.append(current_pair)
            current_pair = []
    return seed_pairs


def parse_map(data, index):
    map_data = []
    while True:
        try:
            line = data[index].strip()
            index += 1
        except IndexError:
            break
        if line.endswith(":"):
            continue
        if not line or line.isspace():
            break
        map_data.append(line.split())
    return map_data, index


def parse_input(data):
    seed_pairs = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    index = 0
    seed_pairs = parse_seeds(data[index])
    index += 2

    seed_to_soil, index = parse_map(data, index)
    soil_to_fertilizer, index = parse_map(data, index)
    fertilizer_to_water, index = parse_map(data, index)
    water_to_light, index = parse_map(data, index)
    light_to_temperature, index = parse_map(data, index)
    temperature_to_humidity, index = parse_map(data, index)
    humidity_to_location, index = parse_map(data, index)

    return (
        seed_pairs,
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location
    )


class Range():
    def __init__(self, min, width):
        self.min = min
        self.width = width

    @property
    def max(self):  # non-inclusive
        return self.min + self.width
    
    def intersect(self, range: "Range") -> ("Range", "Range"):
        if self.min >= range.min and self.min < range.max:
            if self.max < range.max:
                # print('# The "self" range is fully covered by "range"')
                return self, None
            else:
                # print('# The "self" ranges min is within the "range", but not the "self" maximum')
                return Range(min=self.min, width=range.max - self.min), Range(range.max, width=self.max - range.max)
        elif self.max >= range.min and self.max < range.max:
            # print('# The "self" ranges max is within the "range", but not the "self" minimum')
            return Range(min=range.min, width=self.max - range.min), Range(self.min, width=range.min - self.min)
        return None, self
    
    def shift(self, factor):
        # shift the range min by some factor (additive)
        return Range(min=self.min + factor, width=self.width)
    
    def set_max(self, new_max):
        self.width = new_max - self.min

    def __repr__(self) -> str:
        return f"Range(min={self.min}, max={self.max}, width={self.width})"

    
def convert_ranges(source_ranges, map_data):
    dest_ranges = []
    for range in source_ranges:
        uncovered_range = range
        for dest_min, source_min, width in map_data:
            if not uncovered_range:
                continue
            dest_min = int(dest_min)
            source_min = int(source_min)
            width = int(width)
            test_source_range = Range(source_min, width)
            source_to_dest_factor = dest_min - source_min
            i, uncovered_range = uncovered_range.intersect(test_source_range)
            if i:
                dest_ranges.append(i.shift(source_to_dest_factor))
        if uncovered_range and uncovered_range.width != 0:
            dest_ranges.append(uncovered_range)
    return dest_ranges


def main():
    with open("day_5/day5_input.txt") as fp:
        lines = fp.readlines()
    (
        seed_pairs,
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location
    ) = parse_input(lines)

    seed_ranges = []
    for seed_min, seed_width in seed_pairs:
        seed_min = int(seed_min)
        seed_width = int(seed_width)
        seed_ranges.append(Range(seed_min, seed_width))
    
    soil_ranges = convert_ranges(seed_ranges, seed_to_soil)
    fertilizer_ranges = convert_ranges(soil_ranges, soil_to_fertilizer)
    water_ranges = convert_ranges(fertilizer_ranges, fertilizer_to_water)
    light_ranges = convert_ranges(water_ranges, water_to_light)
    temperature_ranges = convert_ranges(light_ranges, light_to_temperature)
    humidity_ranges = convert_ranges(temperature_ranges, temperature_to_humidity)
    location_ranges = convert_ranges(humidity_ranges, humidity_to_location)

    print(len(location_ranges))
    print(location_ranges)
    location_mins = [range.min for range in location_ranges]
    print(min(location_mins))

if __name__ == '__main__':
    main()
