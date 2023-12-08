def get_range(input):
    range = list(map(lambda x: int(x), input.split(" ")))
    return {"start": range[0], "end": range[0] + range[2] - 1, "start_corr": range[1]}


def get_seeds_data(line):
    res = []
    final_res = []
    data = line.split(":")[1].strip().split(" ")
    for element in data:
        if element.isdigit():
            res.append(int(element))
    for index, elem in enumerate(res):
        if index % 2 == 0:
            final_res.append({"seed_start": res[index], "seed_len": res[index + 1]})
    return final_res


def get_maps_info(lines):
    maps = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": [],
    }
    i = 2
    for key in maps.keys():
        if lines[i].startswith(key):
            i += 1
            while i < len(lines) and lines[i] != "\n":
                maps[key].append(get_range(lines[i].strip()))
                i += 1
            i += 1
    return maps


def get_corresponding_index(index, ranges):
    for range in ranges:
        if index >= range["start"] and index <= range["end"]:
            return range["start_corr"] + index - range["start"]
    return index


def is_valid_seed(given_ranges, seed):
    for given_range in given_ranges:
        if (
            seed >= given_range["seed_start"]
            and seed < given_range["seed_start"] + given_range["seed_len"]
        ):
            return True
    return False


def main_func():
    with open("./input1.txt", "r") as file:
        # with open("./testinput.txt", "r") as file:
        lines = file.readlines()
        seeds = get_seeds_data(lines[0])
        maps = get_maps_info(lines)
        min_loc = -1

        # Trying each location one by one until we find a matching seed
        loc = 0
        mul = 1
        while True:
            if loc % mul == 0:
                print(loc)
                mul *= 10
            humid = get_corresponding_index(loc, maps["humidity-to-location"])
            temp = get_corresponding_index(humid, maps["temperature-to-humidity"])
            light = get_corresponding_index(temp, maps["light-to-temperature"])
            water = get_corresponding_index(light, maps["water-to-light"])
            fert = get_corresponding_index(water, maps["fertilizer-to-water"])
            soil = get_corresponding_index(fert, maps["soil-to-fertilizer"])
            seed = get_corresponding_index(soil, maps["seed-to-soil"])
            if is_valid_seed(seeds, seed):
                break
            loc += 1
        print(loc)


if __name__ == "__main__":
    main_func()
