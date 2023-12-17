import sys


def print_grid(grid):
    for line in grid:
        for char in line:
            print(char, end="")
        print()
    print()


def solve(grid, res, mem, line, col, dir):
    if line < 0 or line >= len(grid) or col < 0 or col >= len(grid[0]):
        return
    key = str(line) + "," + str(col) + dir
    if key in mem:
        return
    mem.append(key)

    res[line][col] = "#"
    curr = grid[line][col]

    if curr == ".":
        if dir == "u":
            next_line = line - 1
            next_col = col
        elif dir == "d":
            next_line = line + 1
            next_col = col
        elif dir == "l":
            next_line = line
            next_col = col - 1
        elif dir == "r":
            next_line = line
            next_col = col + 1
        solve(grid, res, mem, next_line, next_col, dir)
    elif curr == "/":
        if dir == "u":
            next_line = line
            next_col = col + 1
            dir = "r"
        elif dir == "d":
            next_line = line
            next_col = col - 1
            dir = "l"
        elif dir == "l":
            next_line = line + 1
            next_col = col
            dir = "d"
        elif dir == "r":
            next_line = line - 1
            next_col = col
            dir = "u"
        solve(grid, res, mem, next_line, next_col, dir)
    elif curr == "b":
        if dir == "u":
            next_line = line
            next_col = col - 1
            dir = "l"
        elif dir == "d":
            next_line = line
            next_col = col + 1
            dir = "r"
        elif dir == "l":
            next_line = line - 1
            next_col = col
            dir = "u"
        elif dir == "r":
            next_line = line + 1
            next_col = col
            dir = "d"
        solve(grid, res, mem, next_line, next_col, dir)
    elif curr == "|":
        if dir == "u":
            next_line = line - 1
            next_col = col
            solve(grid, res, mem, next_line, next_col, dir)
        elif dir == "d":
            next_line = line + 1
            next_col = col
            solve(grid, res, mem, next_line, next_col, dir)
        elif dir == "l" or dir == "r":
            next_line = line - 1
            next_col = col
            dir = "u"
            solve(grid, res, mem, next_line, next_col, dir)
            next_line = line + 1
            next_col = col
            dir = "d"
            solve(grid, res, mem, next_line, next_col, dir)
    elif curr == "-":
        if dir == "u" or dir == "d":
            next_line = line
            next_col = col - 1
            dir = "l"
            solve(grid, res, mem, next_line, next_col, dir)
            next_line = line
            next_col = col + 1
            dir = "r"
            solve(grid, res, mem, next_line, next_col, dir)
        elif dir == "l":
            next_line = line
            next_col = col - 1
            solve(grid, res, mem, next_line, next_col, dir)
        elif dir == "r":
            next_line = line
            next_col = col + 1
            solve(grid, res, mem, next_line, next_col, dir)


def main_func():
    with open(sys.argv[1], "r") as file:
        sys.setrecursionlimit(10000)
        # Getting the grid (bachslashes replaced by 'b' for convenience) and creating result grid
        result = []
        grid = list(map(lambda x: list(x.strip()), file.readlines()))
        for i, line in enumerate(grid):
            result.append([])
            for j, char in enumerate(line):
                if char == "\\":
                    grid[i][j] = "b"
                result[i].append(".")

        # Solving
        sol = 0
        memory = []
        solve(grid, result, memory, 0, 0, "r")

        # Getting the result
        sol = 0
        for line in result:
            for char in line:
                if char == "#":
                    sol += 1
        print(sol)


if __name__ == "__main__":
    main_func()
