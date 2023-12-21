import sys


class Node:
    def __init__(self, id) -> None:
        self.id = id
        self.links = []

    def add_link(self, dest, condition) -> None:
        self.links.append(Link(dest, condition))


class Link:
    def __init__(self, dest, condition) -> None:
        self.detination = dest
        self.condition = condition


def format_rules(rules_input):
    rules = {}
    for rule in rules_input.split("\n"):
        key, info = rule.split("{")
        info = info.strip("}").split(",")
        default = info[-1]
        info = info[0:-1]

        formatted_info = []
        for elt in info:
            elt_rule, elt_dest = elt.split(":")
            formatted_info.append({"rule": elt_rule, "dest": elt_dest})
        rules[key] = {"info": formatted_info, "default": default}
    return rules


def set_status(workflows, part):
    status = "0"
    rule_key = "in"
    while status not in "AR":
        rule = workflows[rule_key]
        rule_new_key = None
        for rule_curr in rule["info"]:
            r, d = rule_curr["rule"], rule_curr["dest"]
            rating, op, rating_val = r[0], r[1], int(r[2:])
            rating_part = part[rating]
            if (op == "<" and rating_part < rating_val) or (
                op == ">" and rating_part > rating_val
            ):
                rule_new_key = rule_curr["dest"]
                break
        if rule_new_key == None:
            rule_new_key = rule["default"]
        if rule_new_key in "AR":
            status = rule_new_key
            break
        rule_key = rule_new_key
    part["status"] = status


def main_func():
    with open(sys.argv[1], "r") as file:
        rules_input, parts_input = file.read().split("\n\n")

        # Formatting rules
        rules = format_rules(rules_input)
        for key in rules.keys():
            print(key, rules[key])

        # # Formatting parts
        # parts = []
        # for part in parts_input.split("\n"):
        #     x, m, a, s = map(
        #         lambda x: int(x.split("=")[1]),
        #         (res for res in part.strip("{}").split(",")),
        #     )
        #     parts.append({"x": x, "m": m, "a": a, "s": s, "status": None})

        # res = 0
        # for part in parts:
        #     set_status(rules, part)
        #     if part["status"] == "A":
        #         for key in "xmas":
        #             res += part[key]
        # print(res)


if __name__ == "__main__":
    main_func()
