def currents_ok(currents):
    for current in currents:
        if current[2] != "Z":
            return False
    return True


def main_func():
    with open("./input1.txt", "r") as file:
        # with open("./testinput.txt", "r") as file:
        lines = file.readlines()

        # Extracting data
        instructions = lines[0].strip()
        directions = {}
        i = 2
        while i < len(lines):
            line = lines[i].strip()
            line_elems = line.split("=")
            line_key = line_elems[0].strip()
            line_directions = line_elems[1].strip().strip("()").split(",")
            directions[line_key] = {
                "L": line_directions[0].strip(),
                "R": line_directions[1].strip(),
            }
            i += 1

        # Initializing all currents
        currents = []
        for key in directions.keys():
            if key[2] == "A":
                currents.append(key)
        results = []
        for new_index, current in enumerate(currents):
            results.append(0)

        # Finding paths for all currents

        for new_index, current in enumerate(currents):
            count = 0
            index = 0
            while currents[new_index][2] != "Z":
                next_direction = instructions[index]
                index += 1
                index %= len(instructions)
                currents[new_index] = directions[currents[new_index]][next_direction]
                count += 1
            results[new_index] = count
        print(results)


if __name__ == "__main__":
    main_func()
