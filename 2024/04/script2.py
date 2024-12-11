import sys

def check_c1(grid, i, j, width, height):
    if (i - 1 < 0 or i + 1 >= height or j - 1 < 0 or j + 1 >= width):
        return False
    if grid[i][j] == 'A' and grid[i - 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'S' and grid[i + 1][j - 1] == 'M' and grid[i - 1][j + 1] == 'S':
        return True
    return False

def check_c2(grid, i, j, width, height):
    if (i - 1 < 0 or i + 1 >= height or j - 1 < 0 or j + 1 >= width):
        return False
    if grid[i][j] == 'A' and grid[i - 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'S' and grid[i + 1][j - 1] == 'S' and grid[i - 1][j + 1] == 'M':
        return True
    return False

def check_c3(grid, i, j, width, height):
    if (i - 1 < 0 or i + 1 >= height or j - 1 < 0 or j + 1 >= width):
        return False
    if grid[i][j] == 'A' and grid[i - 1][j - 1] == 'S' and grid[i + 1][j + 1] == 'M' and grid[i + 1][j - 1] == 'S' and grid[i - 1][j + 1] == 'M':
        return True
    return False

def check_c4(grid, i, j, width, height):
    if (i - 1 < 0 or i + 1 >= height or j - 1 < 0 or j + 1 >= width):
        return False
    if grid[i][j] == 'A' and grid[i - 1][j - 1] == 'S' and grid[i + 1][j + 1] == 'M' and grid[i + 1][j - 1] == 'M' and grid[i - 1][j + 1] == 'S':
        return True
    return False

def calc_xmas(grid, height, width):
    count = 0
    for i in range(height):
        print(grid[i])
        for j in range(width):
            if check_c1(grid, i, j, width, height) or check_c2(grid, i, j, width, height) or check_c3(grid, i, j, width, height) or check_c4(grid, i, j, width, height):
                count += 1
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
