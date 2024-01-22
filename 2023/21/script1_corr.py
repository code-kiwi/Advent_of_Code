import sys
from collections import deque


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))

        start_pos = next(
            (row, col)
            for row, row_content in enumerate(lines)
            for col, char in enumerate(row_content)
            if char == "S"
        )

        ans = set()
        seen = {start_pos}
        q = deque([(start_pos[0], start_pos[1], 64)])
        while q:
            row, col, r_steps = q.popleft()
            if r_steps % 2 == 0:
                ans.add((row, col))
            if r_steps == 0:
                continue
            for new_row, new_col in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if (
                    new_row < 0
                    or new_row >= len(lines)
                    or new_col < 0
                    or new_col >= len(lines[0])
                    or lines[new_row][new_col] == "#"
                    or ((new_row, new_col) in seen)
                ):
                    continue
                seen.add((new_row, new_col))
                q.append((new_row, new_col, r_steps - 1))
        print(len(ans))


if __name__ == "__main__":
    main_func()
