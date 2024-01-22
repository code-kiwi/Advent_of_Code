import sys


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


if __name__ == "__main__":
    main_func()
