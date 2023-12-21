import sys


def main_func():
    with open(sys.argv[1], "r") as file:
        block1, block2 = file.read().split("\n\n")

        workflow = {}
        for line in block1.splitlines():
            name, rest = line[:-1].split("{")
            rules = rest.split(",")
            workflow[name] = ([], rules.pop())
            for rule in rules:
                comparison, target = rule.split(":")
                key, cmp, nb = comparison[0], comparison[1], int(comparison[2:])
                workflow[name][0].append((key, cmp, nb, target))

        # NB: int python those notations are equivalent:
        #       - a < b
        #       - a.__lt__(b)
        #       - type(a).__lt__(a, b)
        #       - int.__LT__(a, b)
        ops = {"<": int.__lt__, ">": int.__gt__}

        def accept(item, name="in"):
            if name == "A":
                return True
            if name == "R":
                return False
            rules = workflow[name]
            for key, cmp, nb, target in rules[0]:
                item_value = item[key]
                # if eval(f"{item_value} {cmp} {nb}"):
                if ops[cmp](item_value, nb):
                    return accept(item, target)
            return accept(item, rules[1])

        total = 0
        for line in block2.splitlines():
            item = {}
            for elt in line.strip("{}").split(","):
                item[elt[0]] = int(elt[2:])
            if accept(item):
                total += sum(item.values())
        print(total)


if __name__ == "__main__":
    main_func()
