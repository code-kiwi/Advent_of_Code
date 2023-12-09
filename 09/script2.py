def is_done(line):
    for nb in line:
        if nb != 0:
            return False
    return True


def main_func():
    with open("./input2.txt", "r") as file:
        # with open("./testinput.txt", "r") as file:
        lines = file.readlines()

        # Getting information from lines
        lines_cleaned = []
        for line in lines:
            lines_cleaned.append(list(map(lambda x: int(x), line.split())))

        res = 0
        for line in lines_cleaned:
            store = []
            before = line
            while True:
                current = []
                for i in range(len(before) - 1):
                    current.append(before[i + 1] - before[i])
                store.append(before)
                before = current
                if is_done(current):
                    break

            prev = 0
            for current in store[::-1]:
                new_val = current[0] - prev
                current.insert(0, new_val)
                prev = new_val

            res += store[0][0]
        print(res)


if __name__ == "__main__":
    main_func()
