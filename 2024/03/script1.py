import sys
import re


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = file.read()
        # print(lines)

        pattern = r"mul\((\d+),(\d+)\)"
        res = re.findall(pattern, lines)
        # print(res)

        ans = 0;
        for tup in res:
            ans += int(tup[0]) * int(tup[1])
        print(ans)


if __name__ == "__main__":
    main_func()
