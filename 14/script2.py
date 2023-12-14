import sys
from copy import deepcopy


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


def tilt_south(grid):
    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                i_rock = i
                while i_rock + 1 < len(grid) and grid[i_rock + 1][j] == ".":
                    grid[i_rock][j] = "."
                    grid[i_rock + 1][j] = "O"
                    i_rock += 1


def tilt_west(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                j_rock = j
                while j_rock - 1 >= 0 and grid[i][j_rock - 1] == ".":
                    grid[i][j_rock] = "."
                    grid[i][j_rock - 1] = "O"
                    j_rock -= 1


def tilt_east(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i]) - 1, -1, -1):
            if grid[i][j] == "O":
                j_rock = j
                while j_rock + 1 < len(grid[i]) and grid[i][j_rock + 1] == ".":
                    grid[i][j_rock] = "."
                    grid[i][j_rock + 1] = "O"
                    j_rock += 1


def eval_grid_order(grid):
    order = len(grid)
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                res += order
        order -= 1
    return res


def cycle(grid):
    tilt_north(grid)
    tilt_west(grid)
    tilt_south(grid)
    tilt_east(grid)


def main_func():
    with open(sys.argv[1], "r") as file:
        grid = list(map(lambda x: list(x.strip()), file.readlines()))

        previous_states = []
        nb_cycles = 1000000000
        for _ in range(nb_cycles):
            state = "".join(list(map(lambda x: "".join(x), grid)))
            if state in previous_states:
                index_state = previous_states.index(state)
                remaining_states = (nb_cycles - index_state) % (
                    len(previous_states) - index_state
                )
                for _ in range(remaining_states):
                    cycle(grid)
                break
            else:
                previous_states.append(state)
                cycle(grid)
        print(eval_grid_order(grid))


if __name__ == "__main__":
    main_func()
