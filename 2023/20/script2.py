import sys
from collections import deque
from math import lcm


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

        (feed,) = (
            module.name for module in modules.values() if "rx" in module.destinations
        )
        (i1, i2, i3, i4) = (
            module.name for module in modules.values() if "lv" in module.destinations
        )
        inputs_to_check = {
            i1: {"name": i1, "found": False, "res": 0},
            i2: {"name": i2, "found": False, "res": 0},
            i3: {"name": i3, "found": False, "res": 0},
            i4: {"name": i4, "found": False, "res": 0},
        }

        b_pressed = 0
        while not all(
            input_to_check["found"] for input_to_check in inputs_to_check.values()
        ):
            b_pressed += 1
            q = deque([("broadcast", dest, "l") for dest in broadcast_targets])
            while q:
                origin, dest, pulse = q.popleft()

                # Output is not taken in account
                if dest not in modules:
                    continue

                module = modules[dest]
                if module.type == "%" and pulse == "l":
                    module.memory = "on" if module.memory == "off" else "off"
                    outpulse = "l" if module.memory == "off" else "h"
                    for i in inputs_to_check.keys():
                        if (
                            dest == i
                            and outpulse == "h"
                            and not (inputs_to_check[i]["found"])
                        ):
                            inputs_to_check[i]["found"] = True
                            inputs_to_check[i]["res"] = b_pressed
                    for dest in module.destinations:
                        q.append((module.name, dest, outpulse))
                elif module.type == "&":
                    module.memory[origin] = pulse
                    outpulse = (
                        "l"
                        if all(mempulse == "h" for mempulse in module.memory.values())
                        else "h"
                    )
                    for i in inputs_to_check.keys():
                        if (
                            dest == i
                            and outpulse == "h"
                            and not (inputs_to_check[i]["found"])
                        ):
                            inputs_to_check[i]["found"] = True
                            inputs_to_check[i]["res"] = b_pressed
                    for dest in module.destinations:
                        if dest == "rx" and outpulse == "l":
                            print(b_pressed)
                            return
                        q.append((module.name, dest, outpulse))
        print(lcm(inputs_to_check[i1]["res"], inputs_to_check[i2]["res"], inputs_to_check[i3]["res"], inputs_to_check[i4]["res"]))

if __name__ == "__main__":
    main_func()
