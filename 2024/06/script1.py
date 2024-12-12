import sys


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        grid = [line.strip() for line in lines]

        rows = len(grid)
        cols = len(grid[0])

        # Finding the guard position
        gr, gc = -1, -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '^':
                    gr, gc = r, c
                    break
            if (gr, gc) != (-1, -1):
                break
        
        # Moving the guard
        dr, dc = -1, 0
        visited = set()
        while True:
            new_gr = gr + dr
            new_gc = gc + dc
            if new_gr < 0 or new_gr >= rows or new_gc < 0 or new_gc >= cols:
                visited.add((gr,gc))
                break
            if grid[new_gr][new_gc] == '#':
                if (dr, dc) == (-1, 0):
                    dr, dc = 0, 1
                elif (dr, dc) == (0, 1):
                    dr, dc = 1, 0
                elif (dr, dc) == (1, 0):
                    dr, dc = 0, -1
                elif (dr, dc) == (0, -1):
                    dr, dc = -1, 0
                continue
            visited.add((gr,gc))
            gr, gc = new_gr, new_gc
        print(len(visited))

        


if __name__ == "__main__":
    main_func()
