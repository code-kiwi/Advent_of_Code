def main_func():
    with open("./input1.txt", "r") as file:
    #with open("./testinput.txt", "r") as file:
        expansion_size = 999999

        # Parsing and storing data
        galaxies = list(map(lambda x: x.strip(), file.readlines()))

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

        # Storing galaxy positions
        positions = []
        for i, line in enumerate(galaxies):
            for j in range(len(line)):
                if galaxies[i][j] == "#":
                    positions.append((i, j))

        # Calculating final result
        res = 0
        for i, position1 in enumerate(positions):
            for j in range(i + 1, len(positions)):
                distance = 0
                position2 = positions[j]
                line = position1[0]
                while line != position2[0]:
                    if line in empty_lines:
                        distance += 1 + expansion_size
                    else:
                        distance += 1
                    if position1[0] < position2[0]:
                        line += 1
                    else:
                        line -= 1
                col = position1[1]
                while col != position2[1]:
                    if col in empty_cols:
                        distance += 1 + expansion_size
                    else:
                        distance += 1
                    if position1[1] < position2[1]:
                        col += 1
                    else:
                        col -= 1
                res += distance
        print(res)


if __name__ == "__main__":
    main_func()
