import sys

def up_ok(grid, pos):
    line_up = pos[0] - 1
    if line_up < 0:
        return False
    up_char = grid[line_up][pos[1]]
    if (
        (line_up == 0 and up_char == "|")
        or (pos[1] == 0 and up_char == "7")
        or (pos[1] == len(grid[line_up]) - 1 and up_char == "F")
    ):
        return False
    if up_char in ["|", "F", "7", "S"]:
        return True
    return False


def down_ok(grid, pos):
    line_down = pos[0] + 1
    len_grid = len(grid)
    if line_down >= len_grid:
        return False
    down_char = grid[line_down][pos[1]]
    if (
        (line_down == len_grid - 1 and down_char == "|")
        or (pos[1] == 0 and down_char == "J")
        or (pos[1] == len(grid[line_down]) - 1 and down_char == "L")
    ):
        return False
    if down_char in ["|", "J", "L", "S"]:
        return True
    return False


def left_ok(grid, pos):
    col_left = pos[1] - 1
    if col_left < 0:
        return False
    left_char = grid[pos[0]][col_left]
    if (
        (col_left == 0 and left_char == "-")
        or (pos[0] == 0 and left_char == "L")
        or (pos[0] == len(grid) - 1 and left_char == "F")
    ):
        return False
    if left_char in ["-", "L", "F", "S"]:
        return True
    return False


def right_ok(grid, pos):
    col_right = pos[1] + 1
    width_grid = len(grid[pos[0]])
    if col_right >= width_grid:
        return False
    right_char = grid[pos[0]][col_right]
    if (
        (col_right == width_grid - 1 and right_char == "-")
        or (pos[0] == 0 and right_char == "J")
        or (pos[0] == len(grid) - 1 and right_char == "7")
    ):
        return False
    if right_char in ["-", "J", "7", "S"]:
        return True
    return False


def solver(grid, pos, previous, start=False):
    print(pos)
    # input()
    current = grid[pos[0]][pos[1]]
    if current == "S" and not (start):
        return 1

    if current == "S":
        is_up_ok = up_ok(grid, pos)
        is_down_ok = down_ok(grid, pos)
        is_left_ok = left_ok(grid, pos)
        is_right_ok = right_ok(grid, pos)

        val_up = solver(grid, (pos[0] - 1, pos[1]), pos) if (is_up_ok) else 0
        val_down = solver(grid, (pos[0] + 1, pos[1]), pos) if (is_down_ok) else 0
        val_left = solver(grid, (pos[0], pos[1] - 1), pos) if (is_left_ok) else 0
        val_right = solver(grid, (pos[0], pos[1] + 1), pos) if (is_right_ok) else 0
        return max(val_up, val_down, val_left, val_right)

    if current == "|":
        is_up_ok = up_ok(grid, pos) if previous[0] != pos[0] - 1 else False
        is_down_ok = down_ok(grid, pos) if previous[0] != pos[0] + 1 else False
        val_up = 1 + solver(grid, (pos[0] - 1, pos[1]), pos) if (is_up_ok) else 0
        val_down = 1 + solver(grid, (pos[0] + 1, pos[1]), pos) if (is_down_ok) else 0
        return max(val_up, val_down)

    if current == "-":
        is_left_ok = left_ok(grid, pos) if previous[1] != pos[1] - 1 else False
        is_right_ok = right_ok(grid, pos) if previous[1] != pos[1] + 1 else False
        val_left = 1 + solver(grid, (pos[0], pos[1] - 1), pos) if (is_left_ok) else 0
        val_right = 1 + solver(grid, (pos[0], pos[1] + 1), pos) if (is_right_ok) else 0
        return max(val_left, val_right)

    if current == "L":
        is_up_ok = up_ok(grid, pos) if previous[0] != pos[0] - 1 else False
        is_right_ok = right_ok(grid, pos) if previous[1] != pos[1] + 1 else False
        val_up = 1 + solver(grid, (pos[0] - 1, pos[1]), pos) if (is_up_ok) else 0
        val_right = 1 + solver(grid, (pos[0], pos[1] + 1), pos) if (is_right_ok) else 0
        return max(val_up, val_right)

    if current == "J":
        is_up_ok = up_ok(grid, pos) if previous[0] != pos[0] - 1 else False
        is_left_ok = left_ok(grid, pos) if previous[1] != pos[1] - 1 else False
        val_up = 1 + solver(grid, (pos[0] - 1, pos[1]), pos) if (is_up_ok) else 0
        val_left = 1 + solver(grid, (pos[0], pos[1] - 1), pos) if (is_left_ok) else 0
        return max(val_up, val_left)

    if current == "7":
        is_down_ok = down_ok(grid, pos) if previous[0] != pos[0] + 1 else False
        is_left_ok = left_ok(grid, pos) if previous[1] != pos[1] - 1 else False
        val_down = 1 + solver(grid, (pos[0] + 1, pos[1]), pos) if (is_down_ok) else 0
        val_left = 1 + solver(grid, (pos[0], pos[1] - 1), pos) if (is_left_ok) else 0
        return max(val_down, val_left)

    if current == "F":
        is_down_ok = down_ok(grid, pos) if previous[0] != pos[0] + 1 else False
        is_right_ok = right_ok(grid, pos) if previous[1] != pos[1] + 1 else False
        val_down = 1 + solver(grid, (pos[0] + 1, pos[1]), pos) if (is_down_ok) else 0
        val_right = 1 + solver(grid, (pos[0], pos[1] + 1), pos) if (is_right_ok) else 0
        return max(val_down, val_right)


def main_func():
    sys.setrecursionlimit(999999)
    with open("./input1.txt", "r") as file:
    # with open("./testinput11.txt", "r") as file:
        grid = list(map(lambda line: line.strip(), file.readlines()))

        # Finding start position
        for i, line in enumerate(grid):
            for j in range(len(line)):
                if line[j] == "S":
                    start_pos = (i, j)
        res = solver(grid, start_pos, start_pos, True)
        print(res)


if __name__ == "__main__":
    main_func()
