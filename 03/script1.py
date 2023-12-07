def surrounded_by_symbol(matrix, line, col, nb_lines, nb_cols):
    if (line > 0 and col > 0 and matrix[line - 1][col - 1] not in '0123456789.'):
        return True
    if (line > 0 and matrix[line - 1][col] not in '0123456789.'):
        return True
    if (line > 0 and col < nb_cols - 1 and matrix[line - 1][col + 1] not in '0123456789.'):
        return True
    if (col > 0 and matrix[line][col - 1] not in '0123456789.'):
        return True
    if (col < nb_cols - 1 and matrix[line][col + 1] not in '0123456789.'):
        return True
    if (line < nb_lines - 1 and col > 0 and matrix[line + 1][col - 1] not in '0123456789.'):
        return True
    if (line < nb_lines - 1 and matrix[line + 1][col] not in '0123456789.'):
        return True
    if (line < nb_lines - 1 and col < nb_cols - 1 and matrix[line + 1][col + 1] not in '0123456789.'):
        return True
    return False


def main_func():
    with open('./input1.txt', 'r') as file:
        # with open('./testinput.txt', 'r') as file:
        matrix = []
        total = 0

        # Extracting the chars from the file into our matrix
        for line in file:
            matrix.append(list(line.strip()))
        nb_lines = len(matrix)
        nb_cols = len(matrix[0])

        i = 0
        while (i < nb_lines):
            j = 0
            while (j < nb_cols):
                if (matrix[i][j] not in '0123456789'):
                    j += 1
                    continue
                k = j
                num = 0
                is_valid = False
                while (k < nb_cols and matrix[i][k] in '0123456789'):
                    if surrounded_by_symbol(matrix, i, k, nb_lines, nb_cols) == True:
                        is_valid = True
                    num = num * 10 + int(matrix[i][k])
                    k += 1
                # print(num)
                if (is_valid == True):
                    # print(num)
                    total += num
                j = k + 1
            i += 1
        print(total)


if __name__ == '__main__':
    main_func()
