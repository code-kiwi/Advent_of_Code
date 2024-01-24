import sys


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
        for sr, sc in points_of_interest:
            stack = [(0, sr, sc)]
            seen = {(sr, sc)}
            while stack:
                n, r, c = stack.pop()
                if n != 0 and (r, c) in points_of_interest:
                    graph[(sr, sc)][(r, c)] = n
                    continue
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
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

        # Calculating longest path
        seen = set()

        def dfs(point):
            if point == end:
                return 0

            m = -float("inf")
            seen.add(point)
            for next_point in graph[point]:
                if next_point not in seen:
                    m = max(m, graph[point][next_point] + dfs(next_point))
            seen.remove(point)
            return m

        print(dfs(start))


if __name__ == "__main__":
    main_func()
