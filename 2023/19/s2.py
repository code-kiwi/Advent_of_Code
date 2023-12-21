import sys


def main_func():
    with open(sys.argv[1], "r") as file:
        block1, _ = file.read().split("\n\n")

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

        def count(ranges, name="in"):
            if name == "R":
                return 0
            if name == "A":
                res = 1
                for low, high in ranges.values():
                    res *= high - low + 1
                return res

            rules, fallback = workflow[name]
            total = 0
            for key, cmp, n, target in rules:
                low, high = ranges[key]
                if cmp == "<":
                    true_half = (low, min(high, n - 1))
                    false_half = (max(low, n), high)
                else:
                    true_half = (max(low, n + 1), high)
                    false_half = (low, min(high, n))
                # We only do a recursion if our new range is valid
                if true_half[0] <= true_half[1]:
                    copy = dict(ranges)
                    copy[key] = true_half
                    total += count(copy, target)
                if false_half[0] <= false_half[1]:
                    # We work on a copy in order to avoid mutating the original ranges tuple
                    ranges = dict(ranges)
                    ranges[key] = false_half
                else:
                    break
            else:
                # else block after for is only executed if the for has not been broken with break instruction
                total += count(ranges, fallback)
            return total

        print(count({key: (1, 4000) for key in "xmas"}))


if __name__ == "__main__":
    main_func()
