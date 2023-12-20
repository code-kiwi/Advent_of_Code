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


def fill(grid, r, c, nr, nc):
    if grid[r][c] == ".":
        grid[r][c] = "#"
    if 0 < r + 1 < nr and grid[r + 1][c] == ".":
        fill(grid, r + 1, c, nr, nc)
    if 0 < r - 1 < nr and grid[r - 1][c] == ".":
        fill(grid, r - 1, c, nr, nc)
    if 0 < c + 1 < nc and grid[r][c + 1] == ".":
        fill(grid, r, c + 1, nr, nc)
    if 0 < c - 1 < nc and grid[r][c - 1] == ".":
        fill(grid, r, c - 1, nr, nc)


def main_func():
    sys.setrecursionlimit(100000)
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
        fill(grid, r0, c0, nbr, nbc)

        for line in grid:
            print("".join(line))


if __name__ == "__main__":
    main_func()
