import sys


def build_grid(data):
    grid = [["."]]
    x, y = 0, 0
    x_max, y_max = 0, 0
    for curr in data:
        dir, nb, col = curr.values()
        if dir == "U":
            for _ in range(nb):
                if x == 0:
                    grid = [(y_max + 1) * ["."]] + grid
                else:
                    x -= 1
                grid[x][y] = "#"
        elif dir == "D":
            for _ in range(nb):
                x += 1
                x_max = max(x, x_max)
                if x_max >= len(grid):
                    grid += [(y_max + 1) * ["."]]
                grid[x][y] = "#"
        elif dir == "L":
            for _ in range(nb):
                if y == 0:
                    for i in range(len(grid)):
                        grid[i] = ["."] + grid[i]
                else:
                    y -= 1
                grid[x][y] = "#"
        else:
            for _ in range(nb):
                y += 1
                y_max = max(y, y_max)
                for line in grid:
                    line += (y_max - len(line) + 1) * ["."]
                grid[x][y] = "#"
    return grid


def flood_fill(grid, r, c, nr, nc):
    queue = [(r, c)]
    i = 0
    unqueued = set()

    while i < len(queue):
        curr = queue[i]
        i += 1
        r_curr, c_curr = curr
        if (
            curr in unqueued
            or not 0 < r_curr < nr
            or not 0 < c_curr < nc
            or grid[r_curr][c_curr] == "#"
        ):
            continue
        unqueued.add(curr)
        grid[r_curr][c_curr] = "#"
        queue.append((r_curr - 1, c_curr))
        queue.append((r_curr + 1, c_curr))
        queue.append((r_curr, c_curr - 1))
        queue.append((r_curr, c_curr + 1))


def main_func():
    with open(sys.argv[1], "r") as file:
        # Getting input data
        data = [
            {
                "dir": line_data[0],
                "nb": int(line_data[1]),
                "col": line_data[2].strip("()"),
            }
            for line_data in (line.split() for line in file.readlines())
        ]
        for line_data in data:
            hex = line_data["col"]
            dir = "R" if hex[-1] == "0" else ("D" if hex[-1] == "1" else ("L" if hex[-1] == "2" else "U"))
            nb = int(hex[1:-1], 16)
            line_data["dir"] = dir
            line_data["nb"] = nb

        # Building the grid and filling the shape
        grid = build_grid(data)

        # Searching for the flood-fill starting point
        nbr, nbc = len(grid), len(grid[0])
        r0, c0 = 0, 0
        found = False
        for r in range(nbr):
            for c in range(nbc):
                if grid[r][c] == "#":
                    r0, c0 = r, c
                    found = True
                    break
            if found:
                break
        r0 += 1
        while grid[r0][c0] != ".":
            c0 += 1
        flood_fill(grid, r0, c0, nbr, nbc)

        res = 0
        for line in grid:
            for char in line:
                if char == "#":
                    res += 1
        print(res)


if __name__ == "__main__":
    main_func()
