def main_func():
    with open("./input1.txt", "r") as file:
        # with open("./testinput.txt", "r") as file:
        # Parsing and storing data
        galaxies = list(map(lambda x: x.strip(), file.readlines()))
        print(galaxies)

        # Empty lines are doubled
        empty_lines = []
        for index, line in enumerate(galaxies):
            is_empty = True
            for j in range(len(line)):
                if line[j] != ".":
                    is_empty = False
                    break
            if is_empty:
                empty_lines.append(index)
        i = 0
        while i < len(empty_lines):
            galaxies.insert(empty_lines[i], galaxies[empty_lines[i]])
            j = i + 1
            while j < len(empty_lines):
                empty_lines[j] += 1
                j += 1
            i += 1
        del empty_lines

        # Empty cols are doubled
        empty_cols = []
        for col_index in range(len(galaxies[0])):
            is_empty = True
            for line_index in range(len(galaxies)):
                if galaxies[line_index][col_index] != ".":
                    is_empty = False
                    break
            if is_empty:
                empty_cols.append(col_index)
        i = 0
        while i < len(empty_cols):
            for line_index in range(len(galaxies)):
                galaxies[line_index] = (
                    galaxies[line_index][: empty_cols[i]]
                    + "."
                    + galaxies[line_index][empty_cols[i] :]
                )
            j = i + 1
            while j < len(empty_cols):
                empty_cols[j] += 1
                j += 1
            i += 1
        del empty_cols
        print(galaxies)

        # Storing galaxy positions
        positions = []
        for i, line in enumerate(galaxies):
            for j in range(len(line)):
                if galaxies[i][j] == "#":
                    positions.append((i, j))
        print(positions)

        # Calculating final result
        res = 0
        for i, position in enumerate(positions):
            for j in range(i + 1, len(positions)):
                res += abs(position[0] - positions[j][0]) + abs(
                    position[1] - positions[j][1]
                )
        print(res)


if __name__ == "__main__":
    main_func()
