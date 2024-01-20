import sys
from collections import deque


class Module:
    def __init__(self, name, type, destinations):
        self.name = name
        self.type = type
        self.destinations = destinations

        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}

    def __str__(self) -> str:
        return f"MODULE {self.name}: {self.type} - dest: [{', '.join(self.destinations)}] - mem: {str(self.memory)}]"


modules = {}
broadcast_targets = []


def main_func():
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()

        # Parsing input file in order to get all modules and the broadcast info
        for line in lines:
            left, right = list(map(lambda x: x.strip(), line.strip().split("->")))
            destinations = list(map(lambda x: x.strip(), right.split(",")))
            if left == "broadcaster":
                broadcast_targets = destinations
            else:
                type = left[0]
                name = left[1:]
                modules[name] = Module(name, type, destinations)

        # Parsing the modules in order to have all the memory for conjunction modules
        for name, module in modules.items():
            for dest in module.destinations:
                if dest in modules and modules[dest].type == "&":
                    modules[dest].memory[name] = "l"

        # Displaying the modules
        # for name, module in modules.items():
        # print(module)

        nb_l = 0
        nb_h = 0
        for _ in range(1000):
            nb_l += 1
            q = deque([("broadcast", dest, "l") for dest in broadcast_targets])
            while q:
                origin, dest, pulse = q.popleft()

                if pulse == "l":
                    nb_l += 1
                else:
                    nb_h += 1

                # Output is not taken in account
                if dest not in modules:
                    continue

                module = modules[dest]
                if module.type == "%" and pulse == "l":
                    module.memory = "on" if module.memory == "off" else "off"
                    outpulse = "l" if module.memory == "off" else "h"
                    for dest in module.destinations:
                        q.append((module.name, dest, outpulse))
                elif module.type == "&":
                    module.memory[origin] = pulse
                    outpulse = (
                        "l"
                        if all(mempulse == "h" for mempulse in module.memory.values())
                        else "h"
                    )
                    for dest in module.destinations:
                        q.append((module.name, dest, outpulse))

        print(nb_l * nb_h)


if __name__ == "__main__":
    main_func()
