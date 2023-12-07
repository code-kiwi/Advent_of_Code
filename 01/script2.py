def main_func():
    digits = ['zero', 'one', 'two', 'three', 'four',
              'five', 'six', 'seven', 'eight', 'nine']
    with open('./01_temp2.txt', 'r') as file:
        sum = 0
        lines = file.readlines()
        for line in lines:
            found = False
            num = 0
            line_len = len(line)

            # Getting first digit
            for i in range(line_len):
                subline = line[i:line_len]
                if subline[0] in '0123456789':
                    num += 10 * int(subline[0])
                    break
                for index, digit in enumerate(digits):
                    if subline.startswith(digit):
                        num += 10 * int(index)
                        found = True
                        break
                if found:
                    break

            found = False
            # Getting last digit
            for i in range(line_len - 1, -1, -1):
                subline = line[i:line_len]
                if subline[0] in '0123456789':
                    num += int(subline[0])
                    break
                for index, digit in enumerate(digits):
                    if subline.startswith(digit):
                        num += int(index)
                        found = True
                        break
                if found:
                    break
            print(num)
            sum += num
        print(sum)


if __name__ == "__main__":
    main_func()
