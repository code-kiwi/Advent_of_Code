import sys
from copy import deepcopy


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


def calc(result):
    sol = 0
    for line in result:
        for char in line:
            if char == "#":
                sol += 1
    return sol


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

        sol = 0

        # Solving
        line = 0
        col = 0
        dir = "r"
        memory = []
        current_result = deepcopy(result)
        solve(grid, current_result, memory, line, col, dir)
        sol = max(sol, calc(current_result))

        line = 0
        col = 0
        dir = "d"
        memory = []
        current_result = deepcopy(result)
        solve(grid, current_result, memory, line, col, dir)
        sol = max(sol, calc(current_result))

        line = 0
        col = len(grid[0]) - 1
        dir = "l"
        memory = []
        current_result = deepcopy(result)
        solve(grid, current_result, memory, line, col, dir)
        sol = max(sol, calc(current_result))

        line = 0
        col = len(grid[0]) - 1
        dir = "d"
        memory = []
        current_result = deepcopy(result)
        solve(grid, current_result, memory, line, col, dir)
        sol = max(sol, calc(current_result))

        line = len(grid) - 1
        col = 0
        dir = "u"
        memory = []
        current_result = deepcopy(result)
        solve(grid, current_result, memory, line, col, dir)
        sol = max(sol, calc(current_result))

        line = len(grid) - 1
        col = 0
        dir = "r"
        memory = []
        current_result = deepcopy(result)
        solve(grid, current_result, memory, line, col, dir)
        sol = max(sol, calc(current_result))

        line = len(grid) - 1
        col = len(grid[0]) - 1
        dir = "u"
        memory = []
        current_result = deepcopy(result)
        solve(grid, current_result, memory, line, col, dir)
        sol = max(sol, calc(current_result))

        line = len(grid) - 1
        col = len(grid[0]) - 1
        dir = "l"
        memory = []
        current_result = deepcopy(result)
        solve(grid, current_result, memory, line, col, dir)
        sol = max(sol, calc(current_result))
        print("ANGLES OK")
        line = 0
        for col in range(1, len(grid[0]) - 1):
            dir = "d"
            memory = []
            current_result = deepcopy(result)
            solve(grid, current_result, memory, line, col, dir)
            sol = max(sol, calc(current_result))
        print("LINE 0 OK")
        line = len(grid) - 1
        for col in range(1, len(grid[0]) - 1):
            dir = "d"
            memory = []
            current_result = deepcopy(result)
            solve(grid, current_result, memory, line, col, dir)
            sol = max(sol, calc(current_result))
        print("LAST LINE OK")
        col = 0
        for line in range(1, len(grid) - 1):
            dir = "r"
            memory = []
            current_result = deepcopy(result)
            solve(grid, current_result, memory, line, col, dir)
            sol = max(sol, calc(current_result))
        print("COL 0 OK")
        col = len(grid[0]) - 1
        for line in range(1, len(grid) - 1):
            dir = "l"
            memory = []
            current_result = deepcopy(result)
            solve(grid, current_result, memory, line, col, dir)
            sol = max(sol, calc(current_result))
        print("LAST COL OK")
        print(sol)


if __name__ == "__main__":
    main_func()
