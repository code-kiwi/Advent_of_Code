import sys


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()[0].split(",")

        val_final = 0
        for line in lines:
            val = 0
            for char in line:
                val += ord(char)
                val *= 17
                val %= 256
            val_final += val
        print(val_final)


if __name__ == "__main__":
    main_func()
