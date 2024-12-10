import sys
import re


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = file.read()
        save = []

        include = True
        i = 0
        while i < len(lines):
            if include:
                j = lines[i:].find("don't()")
                saved = lines[i:i+j] if j != -1 else lines[i:]
                save.append(saved)
                if j == -1:
                    break
                include = False
                i += j
            else:
                j = lines[i:].find("do()")
                if j == -1:
                    break
                include = True
                i += j + 4
        line = ''
        for s in save:
            line += s
        pattern = r"mul\((\d+),(\d+)\)"
        res = re.findall(pattern, line)

        ans = 0;
        for tup in res:
            ans += int(tup[0]) * int(tup[1])
        print(ans)



if __name__ == "__main__":
    main_func()
