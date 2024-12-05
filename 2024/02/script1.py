import sys

def is_safe(lvl):
    # Tests if lvl is sorted
    is_sorted = \
        all(lvl[i] < lvl[i + 1] for i in range(len(lvl) - 1)) \
        or all(lvl[i] > lvl[i + 1] for i in range(len(lvl) - 1))
    if not(is_sorted):
        return 0
    
    # Tests if the differences are correct
    diff_ok = all(abs(lvl[i] - lvl[i + 1]) >= 1 and abs(lvl[i] - lvl[i + 1]) <= 3 for i in range(len(lvl) - 1))

    return 1 if diff_ok else 0

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
