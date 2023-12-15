import sys


def print_grid(grid):
    for line in grid:
        for char in line:
            print(char, end="")
        print()


def tilt_north(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                i_rock = i
                while i_rock - 1 >= 0 and grid[i_rock - 1][j] == ".":
                    grid[i_rock][j] = "."
                    grid[i_rock - 1][j] = "O"
                    i_rock -= 1


def eval_grid_order(grid):
    order = len(grid)
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                res += order
        order -= 1
    return res


def main_func():
    with open(sys.argv[1], "r") as file:
        grid = list(map(lambda x: list(x.strip()), file.readlines()))
        print_grid(grid)
        print()

        tilt_north(grid)
        print_grid(grid)

        print(eval_grid_order(grid))


if __name__ == "__main__":
    main_func()
