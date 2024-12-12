import sys


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        grid = [list(line.strip()) for line in lines]
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
        gr_init = gr
        gc_init = gc
        
        # Moving the guard
        obsr, obsc = 0, 0
        count = 0
        for obsr in range(rows):
            for obsc in range(cols):
                if grid[obsr][obsc] == '#' or grid[obsr][obsc] == '^':
                    continue
                grid[obsr][obsc] = '#'
                gr, gc = gr_init, gc_init
                dr, dc = -1, 0
                loop = True
                while True:
                    new_gr = gr + dr
                    new_gc = gc + dc
                    if new_gr < 0 or new_gr >= rows or new_gc < 0 or new_gc >= cols:
                        loop = False
                        break
                    elif (new_gr, new_gc) == (gr_init, gc_init):
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
                    gr, gc = new_gr, new_gc
                if loop:
                    count += 1
                grid[obsr][obsc] = '.'
        print(count)


        


if __name__ == "__main__":
    main_func()
