def extract_number(matrix, line, col, nb_cols):
    num = {'val': 0, 'line': line, 'col_start': -1, 'col_end': -1}
    while (col >= 0 and matrix[line][col] in '0123456789'):
        col -= 1
    col += 1
    num['col_start'] = col
    while (col < nb_cols and matrix[line][col] in '0123456789'):
        num['val'] = num['val'] * 10 + int(matrix[line][col])
        col += 1
    num['col_end'] = col - 1
    return num


def get_num1(matrix, line, col, nb_lines, nb_cols):
    if (line > 0 and col > 0 and matrix[line - 1][col - 1] in '0123456789'):
        return extract_number(matrix, line - 1, col - 1, nb_cols)
    if (line > 0 and matrix[line - 1][col] in '0123456789'):
        return extract_number(matrix, line - 1, col, nb_cols)
    if (line > 0 and col < nb_cols - 1 and matrix[line - 1][col + 1] in '0123456789'):
        return extract_number(matrix, line - 1, col + 1, nb_cols)
    if (col > 0 and matrix[line][col - 1] in '0123456789'):
        return extract_number(matrix, line, col - 1, nb_cols)
    if (col < nb_cols - 1 and matrix[line][col + 1] in '0123456789'):
        return extract_number(matrix, line, col + 1, nb_cols)
    if (line < nb_lines - 1 and col > 0 and matrix[line + 1][col - 1] in '0123456789'):
        return extract_number(matrix, line + 1, col - 1, nb_cols)
    if (line < nb_lines - 1 and matrix[line + 1][col] in '0123456789'):
        return extract_number(matrix, line + 1, col, nb_cols)
    if (line < nb_lines - 1 and col < nb_cols - 1 and matrix[line + 1][col + 1] in '0123456789'):
        return extract_number(matrix, line + 1, col + 1, nb_cols)
    return {'val': -1, 'line': -1, 'col_start': -1, 'col_end': -1}


def get_num2(matrix, line, col, nb_lines, nb_cols, num1):
    if (line > 0 and col > 0 and matrix[line - 1][col - 1] in '0123456789'):
        if (line - 1 != num1['line'] or col - 1 < num1['col_start'] or col - 1 > num1['col_end']):
            return extract_number(matrix, line - 1, col - 1, nb_cols)
    if (line > 0 and matrix[line - 1][col] in '0123456789'):
        if (line - 1 != num1['line'] or col < num1['col_start'] or col > num1['col_end']):
            return extract_number(matrix, line - 1, col, nb_cols)
    if (line > 0 and col < nb_cols - 1 and matrix[line - 1][col + 1] in '0123456789'):
        if (line - 1 != num1['line'] or col + 1 < num1['col_start'] or col + 1 > num1['col_end']):
            return extract_number(matrix, line - 1, col + 1, nb_cols)
    if (col > 0 and matrix[line][col - 1] in '0123456789'):
        if (line != num1['line'] or col - 1 < num1['col_start'] or col - 1 > num1['col_end']):
            return extract_number(matrix, line, col - 1, nb_cols)
    if (col < nb_cols - 1 and matrix[line][col + 1] in '0123456789'):
        if (line != num1['line'] or col + 1 < num1['col_start'] or col + 1 > num1['col_end']):
            return extract_number(matrix, line, col + 1, nb_cols)
    if (line < nb_lines - 1 and col > 0 and matrix[line + 1][col - 1] in '0123456789'):
        if (line + 1 != num1['line'] or col - 1 < num1['col_start'] or col - 1 > num1['col_end']):
            return extract_number(matrix, line + 1, col - 1, nb_cols)
    if (line < nb_lines - 1 and matrix[line + 1][col] in '0123456789'):
        if (line + 1 != num1['line'] or col < num1['col_start'] or col > num1['col_end']):
            return extract_number(matrix, line + 1, col, nb_cols)
    if (line < nb_lines - 1 and col < nb_cols - 1 and matrix[line + 1][col + 1] in '0123456789'):
        if (line + 1 != num1['line'] or col + 1 < num1['col_start'] or col + 1 > num1['col_end']):
            return extract_number(matrix, line + 1, col + 1, nb_cols)
    return {'val': -1, 'line': -1, 'col_start': -1, 'col_end': -1}


def get_num3(matrix, line, col, nb_lines, nb_cols, num1, num2):
    if (line > 0 and col > 0 and matrix[line - 1][col - 1] in '0123456789'):
        if (line - 1 != num1['line'] or col - 1 < num1['col_start'] or col - 1 > num1['col_end']):
            if (line - 1 != num2['line'] or col - 1 < num2['col_start'] or col - 1 > num2['col_end']):
                return extract_number(matrix, line - 1, col - 1, nb_cols)
    if (line > 0 and matrix[line - 1][col] in '0123456789'):
        if (line - 1 != num1['line'] or col < num1['col_start'] or col > num1['col_end']):
            if (line - 1 != num2['line'] or col < num2['col_start'] or col > num2['col_end']):
                return extract_number(matrix, line - 1, col, nb_cols)
    if (line > 0 and col < nb_cols - 1 and matrix[line - 1][col + 1] in '0123456789'):
        if (line - 1 != num1['line'] or col + 1 < num1['col_start'] or col + 1 > num1['col_end']):
            if (line - 1 != num2['line'] or col + 1 < num2['col_start'] or col + 1 > num2['col_end']):
                return extract_number(matrix, line - 1, col + 1, nb_cols)
    if (col > 0 and matrix[line][col - 1] in '0123456789'):
        if (line != num1['line'] or col - 1 < num1['col_start'] or col - 1 > num1['col_end']):
            if (line != num2['line'] or col - 1 < num2['col_start'] or col - 1 > num2['col_end']):
                return extract_number(matrix, line, col - 1, nb_cols)
    if (col < nb_cols - 1 and matrix[line][col + 1] in '0123456789'):
        if (line != num1['line'] or col + 1 < num1['col_start'] or col + 1 > num1['col_end']):
            if (line != num2['line'] or col + 1 < num2['col_start'] or col + 1 > num2['col_end']):
                return extract_number(matrix, line, col + 1, nb_cols)
    if (line < nb_lines - 1 and col > 0 and matrix[line + 1][col - 1] in '0123456789'):
        if (line + 1 != num1['line'] or col - 1 < num1['col_start'] or col - 1 > num1['col_end']):
            if (line + 1 != num2['line'] or col - 1 < num2['col_start'] or col - 1 > num2['col_end']):
                return extract_number(matrix, line + 1, col - 1, nb_cols)
    if (line < nb_lines - 1 and matrix[line + 1][col] in '0123456789'):
        if (line + 1 != num1['line'] or col < num1['col_start'] or col > num1['col_end']):
            if (line + 1 != num2['line'] or col < num2['col_start'] or col > num2['col_end']):
                return extract_number(matrix, line + 1, col, nb_cols)
    if (line < nb_lines - 1 and col < nb_cols - 1 and matrix[line + 1][col + 1] in '0123456789'):
        if (line + 1 != num1['line'] or col + 1 < num1['col_start'] or col + 1 > num1['col_end']):
            if (line + 1 != num2['line'] or col + 1 < num2['col_start'] or col + 1 > num2['col_end']):
                return extract_number(matrix, line + 1, col + 1, nb_cols)
    return {'val': -1, 'line': -1, 'col_start': -1, 'col_end': -1}


def main_func():
    with open('./input2.txt', 'r') as file:
    #with open('./testinput.txt', 'r') as file:
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
                if (matrix[i][j] != '*'):
                    j += 1
                    continue
                num1 = get_num1(matrix, i, j, nb_lines, nb_cols)
                print('1: ', num1)
                if (num1['val'] == -1):
                    j += 1
                    continue
                num2 = get_num2(matrix, i, j, nb_lines, nb_cols, num1)
                print('2: ', num2)
                if (num2['val'] == -1):
                    j += 1
                    continue
                num3 = get_num3(matrix, i, j, nb_lines, nb_cols, num1, num2)
                print('3: ', num3)
                if (num3['val'] != -1):
                    j += 1
                    continue
                total += num1['val'] * num2['val']
                j += 1
            i += 1
        print(total)


if __name__ == '__main__':
    main_func()
