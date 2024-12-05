import sys


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

        left = []
        right = []
        for line in lines:
            split = line.split()
            left.append(int(split[0]))
            right.append(int(split[1]))

        left.sort()
        right.sort()
        print(sum(abs(a - b) for a, b in zip(left, right)))


if __name__ == "__main__":
    main_func()
