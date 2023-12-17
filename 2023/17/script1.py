import sys


def main_func():
    with open(sys.argv[1], "r") as file:
        # Getting input data
        lines = list(
            map(
                lambda x: list(map(lambda y: int(y), list(x.strip()))), file.readlines()
            )
        )
        for line in lines:
            print(line)

        # Building our nodes
        paths = {}
        visited = []
        unvisited = []
        nb_lines = len(lines)
        nb_cols = len(lines[0])
        for i in range(nb_lines):
            for j in range(nb_cols):
                key = str(i) + "," + str(j)
                paths[key] = {"distance": -1, "previous": None}
                unvisited.append(key)
        print(unvisited)

        current_key = "0,0"
        current_distance = lines[0][0]
        paths[current_key]["distance"] = current_distance
        last_dirs = []
        while len(unvisited) > 0:
            unvisited.remove(current_key)
            visited.append(current_key)
            i, j = current_key.split(",")
            i, j = int(i), int(j)
            # print("CURRENT_KEY: ", current_key, " - ", i, j)
            # print(visited)
            # print(unvisited)
            # for key in paths:
            #     print(key, paths[key])
            # input()

            # Setting distances from current node to neighbors
            for dir in "udlr":
                if dir == "u":
                    i_next, j_next = i - 1, j
                elif dir == "d":
                    i_next, j_next = i + 1, j
                elif dir == "l":
                    i_next, j_next = i, j - 1
                elif dir == "r":
                    i_next, j_next = i, j + 1
                if i_next < 0 or i_next >= nb_lines or j_next < 0 or j_next >= nb_cols:
                    continue
                dist_next = lines[i_next][j_next]
                key_next = str(i_next) + "," + str(j_next)
                if (key_next) in visited:
                    continue
                if (
                    paths[key_next]["distance"] == -1
                    or paths[key_next]["distance"] > current_distance + dist_next
                ):
                    paths[key_next]["distance"] = current_distance + dist_next
                    paths[key_next]["previous"] = current_key

            # Finding the next node to reach
            min_dist = None
            for key in unvisited:
                if paths[key]["distance"] != -1 and (
                    min_dist == None or paths[key]["distance"] < min_dist
                ):
                    min_dist = paths[key]["distance"]
                    current_key = key
            current_distance = paths[current_key]["distance"]
            
            # Getting chosen direction
            i_new, j_new = current_key.split(",")
            i_new, j_new = int(i_new), int(j_new)
            if i_new == i - 1:
                chosen_dir = 'u'
            elif i_new == i + 1:
                chosen_dir = 'd'
            elif j_new == j - 1:
                chosen_dir = 'l'
            elif j_new == j + 1:
                chosen_dir = 'r'
            last_dirs.append(chosen_dir)

        for key in paths:
            print(key, paths[key])
        print()
        print(last_dirs)


if __name__ == "__main__":
    main_func()
