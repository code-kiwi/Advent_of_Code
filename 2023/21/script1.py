import sys


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))

        # Getting start position
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == "S":
                    start_pos = (row, col)
                    break
            if "start_pos" in locals():
                break

        curr_positions = [(start_pos[0], start_pos[1], 0)]
        reachable = {start_pos: 0}
        while curr_positions:
            print(curr_positions)
            input()
            row, col, steps = curr_positions.pop()
            if steps >= 64:
                continue
            north = (row - 1, col)
            south = (row + 1, col)
            west = (row, col - 1)
            east = (row, col + 1)
            steps += 1
            if north[0] >= 0 and lines[north[0]][north[1]] != "#":
                curr_positions.append((north[0], north[1], steps))
                if 64 % steps == 0 and north not in reachable.keys():
                    reachable[north] = steps + 1
            if south[0] < len(lines) and lines[south[0]][south[1]] != "#":
                curr_positions.append((south[0], south[1], steps))
                if 64 % steps == 0 and south not in reachable.keys():
                    reachable[south] = steps
            if west[1] >= 0 and lines[west[0]][west[1]] != "#":
                curr_positions.append((west[0], west[1], steps))
                if 64 % steps == 0 and west not in reachable.keys():
                    reachable[west] = steps
            if east[1] < len(lines[0]) and lines[east[0]][east[1]] != "#":
                curr_positions.append((east[0], east[1], steps))
                if 64 % steps == 0 and east not in reachable.keys():
                    reachable[east] = steps


if __name__ == "__main__":
    main_func()
