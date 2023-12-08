def main_func():
    with open("./01_temp1.txt", "r") as file:
        sum = 0
        lines = file.readlines()
        for line in lines:
            num = 0
            for char in line[::1]:
                if char in "0123456789":
                    num += 10 * int(char)
                    break
            for char in line[::-1]:
                if char in "0123456789":
                    num += int(char)
                    break
            sum += num
        print(sum)


if __name__ == "__main__":
    main_func()
