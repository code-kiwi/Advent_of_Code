def get_range(input):
    range = list(map(lambda x: int(x), input.split(' ')))
    return {'start': range[1], 'end': range[1] +
            range[2] - 1, 'start_corr': range[0]}


def get_seeds_data(line):
    res = []
    final_res = []
    data = line.split(':')[1].strip().split(' ')
    for element in data:
        if element.isdigit():
            res.append(int(element))
    for index, elem in enumerate(res):
        if (index % 2 == 0):
            final_res.append(
                {'seed_start': res[index], 'seed_len': res[index + 1]})
    return final_res


def get_maps_info(lines):
    maps = {
        'seed-to-soil': [],
        'soil-to-fertilizer': [],
        'fertilizer-to-water': [],
        'water-to-light': [],
        'light-to-temperature': [],
        'temperature-to-humidity': [],
        'humidity-to-location': []
    }
    i = 2
    for key in maps.keys():
        if (lines[i].startswith(key)):
            i += 1
            while (i < len(lines) and lines[i] != '\n'):
                maps[key].append(get_range(lines[i].strip()))
                i += 1
            i += 1
    return maps


def get_corresponding_index(seed, ranges):
    for range in ranges:
        if (seed >= range['start'] and seed <= range['end']):
            return (range['start_corr'] + seed - range['start'])
    return seed


def main_func():
    with open('./input3.txt', 'r') as file:
    #with open('./testinput.txt', 'r') as file:
        lines = file.readlines()
        seeds = get_seeds_data(lines[0])
        maps = get_maps_info(lines)
        min_loc = -1
        for seed in seeds:
            i = 0
            while (i < seed['seed_len']):
                soil = get_corresponding_index(seed['seed_start'] + i, maps['seed-to-soil'])
                fert = get_corresponding_index(soil, maps['soil-to-fertilizer'])
                water = get_corresponding_index(fert, maps['fertilizer-to-water'])
                light = get_corresponding_index(water, maps['water-to-light'])
                temp = get_corresponding_index(light, maps['light-to-temperature'])
                humid = get_corresponding_index(
                    temp, maps['temperature-to-humidity'])
                loc = get_corresponding_index(humid, maps['humidity-to-location'])
                if (min_loc == -1):
                    min_loc = loc
                else:
                    min_loc = min(min_loc, loc)
                i += 1
        print(min_loc)


if __name__ == '__main__':
    main_func()
