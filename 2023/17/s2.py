from heapq import heappush, heappop
import sys


def main_func():
    with open(sys.argv[1], "r") as file:
        grid = list(map(lambda x: list(map(int, x.strip())), file.readlines()))

        seen = set()
        # Our state is: (heat_loss, row, col, d_row, d_col, nb_steps_in_current_direction)
        priority_queue = [(0, 0, 0, 0, 0, 0)]
        while priority_queue:
            # Getting state info
            heat_loss, row, col, dir_row, dir_col, nb_steps_cur_dir = heappop(
                priority_queue
            )

            # Our break condition (we reached the end of the map)
            if row == len(grid) - 1 and col == len(grid[0]) - 1 and nb_steps_cur_dir >= 4:
                # Our priority queue ensures us that we are in the minimum heat loss, because we always unqueue our minimum heat_loss
                print(heat_loss)
                break

            # If our current state is already seen we do not treat it (heat_loss is not part of the state in order to avoid loops)
            if (row, col, dir_row, dir_col, nb_steps_cur_dir) in seen:
                continue

            # Then the current state is added to the seen states
            seen.add((row, col, dir_row, dir_col, nb_steps_cur_dir))

            # If we can move in the same direction, we add next state to the heapq going in the same direction
            if nb_steps_cur_dir < 10 and (dir_row, dir_col) != (0, 0):
                next_row, next_col = row + dir_row, col + dir_col
                if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                    heappush(
                        priority_queue,
                        (
                            heat_loss + grid[next_row][next_col],
                            next_row,
                            next_col,
                            dir_row,
                            dir_col,
                            nb_steps_cur_dir + 1,
                        ),
                    )

            # Then, we can go in the other directions
            if (dir_row, dir_col) == (0, 0) or nb_steps_cur_dir >= 4:
                for next_dir_row, next_dir_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    # We cannot go in the same direction as before nor in the opposite direction
                    if (
                        (next_dir_row, next_dir_col) == (dir_row, dir_col)
                        or (next_dir_row, next_dir_col) == (-dir_row, -dir_col)
                    ):
                        continue
                    next_row, next_col = row + next_dir_row, col + next_dir_col
                    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                        heappush(
                            priority_queue,
                            (
                                heat_loss + grid[next_row][next_col],
                                next_row,
                                next_col,
                                next_dir_row,
                                next_dir_col,
                                1,
                            ),
                        )


if __name__ == "__main__":
    main_func()
