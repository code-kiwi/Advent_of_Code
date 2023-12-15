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


def main_func():
    with open("./input1.txt", "r") as file:
    # with open("./testinput11.txt", "r") as file:
        grid = list(map(lambda line: line.strip(), file.readlines()))

        # Finding start position
        for i, line in enumerate(grid):
            for j in range(len(line)):
                if line[j] == "S":
                    start_pos = (i, j)

        previous_pos = []
        invalid = []
        pos = start_pos
        while True:
            current = grid[pos[0]][pos[1]]
            up_pos = (pos[0] - 1, pos[1])
            down_pos = (pos[0] + 1, pos[1])
            left_pos = (pos[0], pos[1] - 1)
            right_pos = (pos[0], pos[1] + 1)

            # Solution is found
            if current == "S" and len(previous_pos) != 0:
                break

            # Starting point
            if current == "S":
                is_up_ok = up_ok(grid, pos) and up_pos not in invalid
                if is_up_ok:
                    previous_pos.append(pos)
                    pos = up_pos
                    continue
                if up_pos not in previous_pos:
                    invalid.append(up_pos)
                is_down_ok = down_ok(grid, pos) and down_pos not in invalid
                if is_down_ok:
                    previous_pos.append(pos)
                    pos = down_pos
                    continue
                if down_pos not in previous_pos:
                    invalid.append(down_pos)
                is_left_ok = left_ok(grid, pos) and left_pos not in invalid
                if is_left_ok:
                    previous_pos.append(pos)
                    pos = left_pos
                    continue
                if left_pos not in previous_pos:
                    invalid.append(left_pos)
                is_right_ok = right_ok(grid, pos) and right_pos not in invalid
                if is_right_ok:
                    previous_pos.append(pos)
                    pos = right_pos
                    continue
                if right_pos not in previous_pos:
                    invalid.append(right_pos)

            # Other cases
            previous = previous_pos[-1]

            if current == "|":
                is_up_ok = (
                    previous != up_pos and up_ok(grid, pos) and up_pos not in invalid
                )
                if is_up_ok:
                    previous_pos.append(pos)
                    pos = up_pos
                    continue
                if up_pos not in previous_pos:
                    invalid.append(up_pos)
                is_down_ok = (
                    previous != down_pos
                    and down_ok(grid, pos)
                    and down_pos not in invalid
                )
                if is_down_ok:
                    previous_pos.append(pos)
                    pos = down_pos
                    continue
                if down_pos not in previous_pos:
                    invalid.append(down_pos)

            if current == "-":
                is_left_ok = (
                    previous != left_pos
                    and left_ok(grid, pos)
                    and left_pos not in invalid
                )
                if is_left_ok:
                    previous_pos.append(pos)
                    pos = left_pos
                    continue
                if left_pos not in previous_pos:
                    invalid.append(left_pos)
                is_right_ok = (
                    previous != right_pos
                    and right_ok(grid, pos)
                    and right_pos not in invalid
                )
                if is_right_ok:
                    previous_pos.append(pos)
                    pos = right_pos
                    continue
                if right_pos not in previous_pos:
                    invalid.append(right_pos)

            if current == "L":
                is_up_ok = (
                    previous != up_pos and up_ok(grid, pos) and up_pos not in invalid
                )
                if is_up_ok:
                    previous_pos.append(pos)
                    pos = up_pos
                    continue
                if up_pos not in previous_pos:
                    invalid.append(up_pos)
                is_right_ok = (
                    previous != right_pos
                    and right_ok(grid, pos)
                    and right_pos not in invalid
                )
                if is_right_ok:
                    previous_pos.append(pos)
                    pos = right_pos
                    continue
                if right_pos not in previous_pos:
                    invalid.append(right_pos)

            if current == "J":
                is_up_ok = (
                    previous != up_pos and up_ok(grid, pos) and up_pos not in invalid
                )
                if is_up_ok:
                    previous_pos.append(pos)
                    pos = up_pos
                    continue
                if up_pos not in previous_pos:
                    invalid.append(up_pos)
                is_left_ok = (
                    previous != left_pos
                    and left_ok(grid, pos)
                    and left_pos not in invalid
                )
                if is_left_ok:
                    previous_pos.append(pos)
                    pos = left_pos
                    continue
                if left_pos not in previous_pos:
                    invalid.append(left_pos)

            if current == "7":
                is_down_ok = (
                    previous != down_pos
                    and down_ok(grid, pos)
                    and down_pos not in invalid
                )
                if is_down_ok:
                    previous_pos.append(pos)
                    pos = down_pos
                    continue
                if down_pos not in previous_pos:
                    invalid.append(down_pos)
                is_left_ok = (
                    previous != left_pos
                    and left_ok(grid, pos)
                    and left_pos not in invalid
                )
                if is_left_ok:
                    previous_pos.append(pos)
                    pos = left_pos
                    continue
                if left_pos not in previous_pos:
                    invalid.append(left_pos)

            if current == "F":
                is_down_ok = (
                    previous != down_pos
                    and down_ok(grid, pos)
                    and down_pos not in invalid
                )
                if is_down_ok:
                    previous_pos.append(pos)
                    pos = down_pos
                    continue
                if down_pos not in previous_pos:
                    invalid.append(down_pos)
                is_right_ok = (
                    previous != right_pos
                    and right_ok(grid, pos)
                    and right_pos not in invalid
                )
                if is_right_ok:
                    previous_pos.append(pos)
                    pos = right_pos
                    continue
                if right_pos not in previous_pos:
                    invalid.append(right_pos)

            # Current position is invalid
            invalid.append(previous_pos.pop())
            pos = previous

        print(len(previous_pos) // 2)


if __name__ == "__main__":
    main_func()
