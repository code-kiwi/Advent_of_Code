import sys

def check_left(grid, i, j):
    if (j < 3):
        return 0
    if grid[i][j] == 'X' and grid[i][j - 1] == 'M' and grid[i][j - 2] == 'A' and grid[i][j - 3] == 'S':
        return 1
    return 0

def check_right(grid, i, j, width):
    if (j > width - 4):
        return 0
    if grid[i][j] == 'X' and grid[i][j + 1] == 'M' and grid[i][j + 2] == 'A' and grid[i][j + 3] == 'S':
        return 1
    return 0

def check_up(grid, i, j):
    if (i < 3):
        return 0
    if grid[i][j] == 'X' and grid[i - 1][j] == 'M' and grid[i - 2][j] == 'A' and grid[i - 3][j] == 'S':
        return 1
    return 0

def check_down(grid, i, j, height):
    if (i > height - 4):
        return 0
    if grid[i][j] == 'X' and grid[i + 1][j] == 'M' and grid[i + 2][j] == 'A' and grid[i + 3][j] == 'S':
        return 1
    return 0

def check_diag1(grid, i, j):
    if (i < 3 or j < 3):
        return 0
    if grid[i][j] == 'X' and grid[i - 1][j - 1] == 'M' and grid[i - 2][j - 2] == 'A' and grid[i - 3][j - 3] == 'S':
        return 1
    return 0

def check_diag2(grid, i, j, width):
    if (i < 3 or j > width - 4):
        return 0
    if grid[i][j] == 'X' and grid[i - 1][j + 1] == 'M' and grid[i - 2][j + 2] == 'A' and grid[i - 3][j + 3] == 'S':
        return 1
    return 0

def check_diag3(grid, i, j, width, height):
    if (i > height - 4 or j > width - 4):
        return 0
    if grid[i][j] == 'X' and grid[i + 1][j + 1] == 'M' and grid[i + 2][j + 2] == 'A' and grid[i + 3][j + 3] == 'S':
        return 1
    return 0

def check_diag4(grid, i, j, height):
    if (i > height - 4 or j < 3):
        return 0
    if grid[i][j] == 'X' and grid[i + 1][j - 1] == 'M' and grid[i + 2][j - 2] == 'A' and grid[i + 3][j - 3] == 'S':
        return 1
    return 0

def calc_xmas(grid, height, width):
    count = 0
    for i in range(height):
        print(grid[i])
        for j in range(width):
            if (grid[i][j] != 'X'):
                continue
            count += check_left(grid, i, j)
            count += check_right(grid, i, j, width)
            count += check_up(grid, i, j)
            count += check_down(grid, i, j, height)
            count += check_diag1(grid, i, j)
            count += check_diag2(grid, i, j, width)
            count += check_diag3(grid, i, j, width, height)
            count += check_diag4(grid, i, j, height)
    return (count);
    

def main_func():
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

        width = len(lines[0])
        height = len(lines)
        for i in range(len(lines)):
            print(lines[i])
        
        print(calc_xmas(lines, height, width))


if __name__ == "__main__":
    main_func()
