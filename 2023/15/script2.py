import sys


def hash_str(str):
    val = 0
    for char in str:
        val += ord(char)
        val *= 17
        val %= 256
    return val


def print_boxes(boxes):
    for key in boxes.keys():
        if len(boxes[key]) > 0:
            print("Box ", key, ": ", boxes[key])


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()[0].split(",")

        # Creating and filling boxes
        boxes = {}
        for i in range(256):
            boxes[i] = []
        for line in lines:
            label = line[: len(line) - 1] if "-" in line else line[: len(line) - 2]
            box = hash_str(label)
            focal = line[-1]
            lens_str = "" + label + " " + focal
            if focal != "-":
                found = False
                for i, lens in enumerate(boxes[box]):
                    if lens.startswith(label):
                        found = True
                        boxes[box][i] = lens_str
                        break
                if not found:
                    boxes[box].append(lens_str)
            else:
                for i, lens in enumerate(boxes[box]):
                    if lens.startswith(label):
                        found = True
                        del boxes[box][i]
                        break

        # Calculating final value
        val_final = 0
        for key in boxes.keys():
            val = 0
            for i, lens in enumerate(boxes[key]):
                val = (key + 1) * (i + 1) * int(lens[-1])
                val_final += val
        print(val_final)


if __name__ == "__main__":
    main_func()
