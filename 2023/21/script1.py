import sys


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        print(lines)


if __name__ == "__main__":
    main_func()
