import sys

dirs = ["u", "d", "l", "r"]


class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def add_neighbor(self, neighbor, weight):
        for i, node in enumerate(self.neighbors):
            if node[0].id == neighbor.id:
                self.neighbors[i][1] = min(self.neighbors[i][1], weight)
                return
        self.neighbors.append([neighbor, weight])

    def display(self):
        print("NODE: (", self.id, ")")
        print("[", end="")
        for node in self.neighbors:
            print("(", node[0].id, ") -> ", node[1], " ", end="")
        print("]")


def main_func():
    with open(sys.argv[1], "r") as file:
        grid = list(map(lambda x: list(x.strip()), file.readlines()))
        for line in grid:
            for i, char in enumerate(line):
                line[i] = int(line[i])
        nb_lines = len(grid)
        nb_cols = len(grid[0])

        nodes = {}
        start_node = Node("init")
        nodes["init"] = start_node
        node_A = None
        for i in range(nb_lines):
            for j in range(nb_cols):
                node_key = str(i) + "," + str(j)
                if node_key in nodes.keys():
                    node = nodes[node_key]
                else:
                    node = Node(node_key)
                    nodes[node_key] = node
                if i == 0 and j == 0:
                    node_A = node
                for dir_str in dirs:
                    weight = 0
                    curr_line = i
                    curr_col = j
                    valid = True
                    for dir in dir_str:
                        if dir == "u":
                            curr_line -= 1
                        elif dir == "d":
                            curr_line += 1
                        elif dir == "l":
                            curr_col -= 1
                        else:
                            curr_col += 1
                        if (
                            curr_line < 0
                            or curr_line >= nb_lines
                            or curr_col < 0
                            or curr_col >= nb_cols
                        ):
                            valid = False
                            break
                        weight += grid[curr_line][curr_col]
                    if not valid:
                        continue
                    curr_node_key = str(curr_line) + "," + str(curr_col)
                    if curr_node_key in nodes.keys():
                        curr_node = nodes[curr_node_key]
                    else:
                        curr_node = Node(curr_node_key)
                        nodes[curr_node_key] = curr_node
                    node.add_neighbor(curr_node, weight)
        start_node.add_neighbor(node_A, grid[0][0])

        """
        for node in nodes.values():
            node.display()
            input()
        """

        path = {}
        unvisited = []
        visited = []
        for key in nodes.keys():
            if key == "init":
                path[key] = {"weight": 0, "previous": None}
                visited.append(key)
            else:
                path[key] = {"weight": -1, "previous": None}
                unvisited.append(key)
        current_node = nodes["init"]
        current_weight = 0
        while True:
            for neighbor in current_node.neighbors:
                id = neighbor[0].id
                if id in visited:
                    continue
                if path[id]["weight"] == -1 or neighbor[1] < path[id]["weight"]:
                    path[id]["weight"] = current_weight + neighbor[1]
                    path[id]["previous"] = id
            min = None
            if (len(unvisited) == 0):
                break
            for key in unvisited:
                if min == None or min > path[key]["weight"]:
                    current_key = key
            current_node = nodes[key]
            current_weight += path[key]["weight"]
            visited.append(key)
            unvisited.remove(key)
        
        for key in path.keys():
            print(key, path[key])
        for key in nodes.keys():
            nodes[key].display()



if __name__ == "__main__":
    main_func()
