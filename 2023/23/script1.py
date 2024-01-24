import sys

"""
We want to calculate a longest path (we previously only worked on shortest ones)
We can see that our input is a sort of labyrinth (the path is always one unit wide)
We also notice that there can be a lot of useless characters on our path (ex: A..........B is just AB with a weight of 10)
For most of our walkings, we have no choice to make
Then we will use a technique called "EDGE CONTRACTION"

"""


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))

        # Getting the start and end points
        start = (0, next(index for index, char in enumerate(lines[0]) if char == "."))
        end = (
            len(lines) - 1,
            next(
                index for index, char in enumerate(lines[len(lines) - 1]) if char == "."
            ),
        )

        # Getting all the points which represent a choice to make (plus start and end)
        points_of_interest = [start, end]
        for r, row in enumerate(lines):
            for c, char in enumerate(row):
                if char == "#":
                    continue
                neighbors = 0
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if (
                        0 <= nr < len(lines)
                        and 0 <= nc < len(lines[0])
                        and lines[nr][nc] != "#"
                    ):
                        neighbors += 1
                if neighbors >= 3:
                    points_of_interest.append((r, c))

        # Creating the graph (only adjacent points are connected because we cannot wolk on a tile twice)
        graph = {point: {} for point in points_of_interest}
        dirs = {
            "^": [(-1, 0)],
            "v": [(1, 0)],
            "<": [(0, -1)],
            ">": [(0, 1)],
            ".": [(1, 0), (-1, 0), (0, 1), (0, -1)],
        }
        for sr, sc in points_of_interest:
            stack = [(0, sr, sc)]
            seen = {(sr, sc)}
            while stack:
                n, r, c = stack.pop()
                if n != 0 and (r, c) in points_of_interest:
                    graph[(sr, sc)][(r, c)] = n
                    continue
                for dr, dc in dirs[lines[r][c]]:
                    nr = r + dr
                    nc = c + dc
                    if (
                        0 <= nr < len(lines)
                        and 0 <= nc < len(lines[0])
                        and lines[nr][nc] != "#"
                        and (nr, nc) not in seen
                    ):
                        stack.append((n + 1, nr, nc))
                        seen.add((nr, nc))

        # Now we have our graph we need to find the longest path
        # Longest path cannot be calculated easily, we just have to brute force every possible path to find it
        seen = set()

        def dfs(point):
            if point == end:
                return 0

            m = -float(
                "inf"
            )  # using infinity here enables us to add any number to it keeping -inf
            seen.add(point)  # in order to avoid cycles
            for next_point in graph[point]:
                m = max(m, graph[point][next_point] + dfs(next_point))
            seen.remove(
                point
            )  # we do not want to block point because there could be another path to it
            return m

        print(dfs(start))


if __name__ == "__main__":
    main_func()
