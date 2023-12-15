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

        # Finding path
        current = "AAA"
        count = 0
        index = 0
        while current != "ZZZ":
            print(current)
            next_direction = instructions[index]
            index += 1
            index %= len(instructions)
            current = directions[current][next_direction]
            count += 1
        print(count)


if __name__ == "__main__":
    main_func()
