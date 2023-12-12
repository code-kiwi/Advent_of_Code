def get_line_struct(line):
    res = []
    in_word = False
    count = 0
    for i in range(len(line)):
        if not in_word and line[i] == ".":
            continue
        if not (in_word) and line[i] == "#":
            in_word = True
            count += 1
        elif in_word and line[i] == "#":
            count += 1
        elif in_word and line[i] == ".":
            in_word = False
            res.append(count)
            count = 0
    if count != 0:
        res.append(count)
    return res


def char_indexes(c, str):
    res = []
    for i, char in enumerate(str):
        if char == c:
            res.append(i)
    return res


def test_combs(line, indexes):
    res = 0
    check = line["numbers"]
    len_indexes = len(indexes)
    nb_combs = 2**len_indexes
    for i in range(nb_combs):
        curr_line = line["draw"].copy()
        comb = bin(i)[2:].zfill(len_indexes)
        # Applying comb to current line
        for i, c in enumerate(comb):
            if c == "0":
                curr_line[indexes[i]] = "."
            else:
                curr_line[indexes[i]] = "#"
        # Checking for result
        curr_line_struct = get_line_struct(curr_line)
        if curr_line_struct == check:
            res += 1
    return res


def main_func():
    with open("./input1.txt", "r") as file:
        # with open("./testinput.txt", "r") as file:
        # Extracting data from file
        data = []
        lines = list(map(lambda x: x.strip(), file.readlines()))
        for line in lines:
            line_elts = line.split(" ")
            line_draw = list(line_elts[0])
            line_numbers = line_elts[1].split(",")
            data.append(
                {
                    "draw": line_draw,
                    "numbers": list(map(lambda x: int(x), line_numbers)),
                    "tot": 0,
                }
            )

        # Solving
        res = 0
        for line in data:
            indexes = char_indexes("?", line["draw"])
            line["tot"] = test_combs(line, indexes)
            res += line["tot"]
        print(res)


if __name__ == "__main__":
    main_func()
