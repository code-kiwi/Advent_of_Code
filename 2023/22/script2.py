import sys
from collections import deque


def overlaps(brick_a, brick_b):
    return max(brick_a[0], brick_b[0]) <= min(brick_a[3], brick_b[3]) and max(
        brick_a[1], brick_b[1]
    ) <= min(brick_a[4], brick_b[4])


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        bricks = [list(map(int, line.replace("~", ",").split(","))) for line in lines]
        bricks.sort(key=lambda brick: brick[2])

        for index, brick in enumerate(bricks):
            min_z = 1
            for brick_to_check in bricks[:index]:
                if overlaps(brick, brick_to_check):
                    # New z min needs to take multiple bricks on same z in account
                    min_z = max(min_z, brick_to_check[5] + 1)
            brick[5] = min_z + (brick[5] - brick[2])
            brick[2] = min_z
        bricks.sort(key=lambda brick: brick[2])

        lower_supports_upper = {i: set() for i in range(len(bricks))}
        upper_supported_by_lower = {i: set() for i in range(len(bricks))}
        for j, upper in enumerate(bricks):
            for i, lower in enumerate(bricks[:j]):
                if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                    lower_supports_upper[i].add(j)
                    upper_supported_by_lower[j].add(i)

        valid = set()
        for index in range(len(bricks)):
            if len(lower_supports_upper[index]) == 0:
                valid.add(index)
                continue
            if all(
                (len(upper_supported_by_lower[j]) > 1)
                for j in lower_supports_upper[index]
            ):
                valid.add(index)

        total = 0
        for i in range(len(bricks)):
            if i in valid:
                continue
            q = deque(
                j
                for j in lower_supports_upper[i]
                if len(upper_supported_by_lower[j]) == 1
            )
            fallen = set(q)
            while q:
                j = q.popleft()
                for k in lower_supports_upper[j]:
                    if k not in fallen and upper_supported_by_lower[k] <= fallen:
                        q.append(k)
                        fallen.add(k)
            total += len(fallen)
        print(total)


if __name__ == "__main__":
    main_func()
