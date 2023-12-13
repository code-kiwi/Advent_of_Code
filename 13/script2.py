def v_check(grid, forbidden):
    v_index = 1
    while v_index < len(grid[0]):
        if v_index == forbidden:
            v_index += 1
            continue
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
        if v_ok and v_index != forbidden:
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
        grid_index = 0
        while i < len(lines):
            grid_index += 1
            curr = []
            while i < len(lines) and lines[i] != "":
                curr.append(lines[i])
                i += 1

            # Vertical check
            v_index = v_check(curr, 0)
            found2 = False
            for i2 in range(len(curr)):
                for j2 in range(len(curr[i2])):
                    curr[i2] = (
                        curr[i2][:j2]
                        + ("." if curr[i2][j2] == "#" else "#")
                        + curr[i2][j2 + 1 :]
                    )
                    v_index2 = v_check(curr, v_index)
                    curr[i2] = (
                        curr[i2][:j2]
                        + ("." if curr[i2][j2] == "#" else "#")
                        + curr[i2][j2 + 1 :]
                    )
                    if v_index2 != -1 and v_index2 != v_index:
                        found2 = True
                        break
                if found2:
                    break
            if found2:
                res += v_index2
                i += 1
                continue

            # Horizontal check
            curr_hor = rotate(curr)

            h_index = v_check(curr_hor, 0)
            found2 = False
            for i2 in range(len(curr_hor)):
                for j2 in range(len(curr_hor[i2])):
                    curr_hor[i2] = (
                        curr_hor[i2][:j2]
                        + ("." if curr_hor[i2][j2] == "#" else "#")
                        + curr_hor[i2][j2 + 1 :]
                    )
                    h_index2 = v_check(curr_hor, h_index)
                    curr_hor[i2] = (
                        curr_hor[i2][:j2]
                        + ("." if curr_hor[i2][j2] == "#" else "#")
                        + curr_hor[i2][j2 + 1 :]
                    )
                    if h_index2 != -1 and h_index2 != h_index:
                        found2 = True
                        break
                if found2:
                    break
            if found2:
                res += 100 * h_index2
                i += 1
                continue
            i += 1
        print(res)


if __name__ == "__main__":
    main_func()
