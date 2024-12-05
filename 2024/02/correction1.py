import sys

def is_safe(levels):
    diffs = [x - y for x, y in zip(levels, levels[1:])]
    return 1 if (all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)) else 0

def main_func():
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    
    levels = [list(map(int, line.split())) for line in lines]
    # print(levels)

    res = 0
    for lvl in levels:
        res += is_safe(lvl)
    print(res)


if __name__ == "__main__":
    main_func()
