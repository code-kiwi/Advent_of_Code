from functools import reduce


def get_races_data(lines):
    data = []
    time = int(
        reduce(
            lambda x, y: x + y,
            list(filter(lambda x: x != "", lines[0].split(":")[1].strip().split(" "))),
        )
    )
    distance = int(
        reduce(
            lambda x, y: x + y,
            list(filter(lambda x: x != "", lines[1].split(":")[1].strip().split(" "))),
        )
    )
    data.append({"time": time, "distance": distance})
    return data


def main_func():
    with open("./input1.txt", "r") as file:
        # with open("./testinput.txt", "r") as file:
        lines = file.readlines()
        races = get_races_data(lines)
        res = 1
        for race in races:
            count = 0
            time = race["time"]
            distance = race["distance"]
            for i in range(time):
                distance_covered = (time - i) * i
                if distance_covered > distance:
                    count += 1
            res *= count
        print(res)


if __name__ == "__main__":
    main_func()
