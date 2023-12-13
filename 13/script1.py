def v_check(grid):
    v_index = 1
    while v_index < len(grid[0]):
        v_ok = True
        for line in grid:
            left = line[:v_index]
            right = line[v_index:]
            if len(left) < len(right):
                if not right.startswith(left[::-1]):
                    v_ok = False
            else:
                if not left.endswith(right[::-1]):
                    v_ok = False
            if not v_ok:
                break
        if v_ok:
            return v_index
        v_index += 1
    return -1


def rotate(grid):
    res = []
    col = len(grid[0]) - 1
    while col >= 0:
        res_line = []
        line = 0
        while line <= len(grid) - 1:
            res_line.append(grid[line][col])
            line += 1
        res.append("".join(res_line))
        col -= 1
    return res


def main_func():
    with open("./input1.txt", "r") as file:
        # with open("./testinput.txt", "r") as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        i = 0
        res = 0
        while i < len(lines):
            curr = []
            while i < len(lines) and lines[i] != "":
                curr.append(lines[i])
                i += 1

            # Vertical check
            v_index = v_check(curr)
            if v_index != -1:
                res += v_index
                i += 1
                continue

            # Horizontal check
            curr_hor = rotate(curr)
            v_index = v_check(curr_hor)
            if v_index != -1:
                res += 100 * v_index
                i += 1
                continue
            i += 1
        print(res)


if __name__ == "__main__":
    main_func()
