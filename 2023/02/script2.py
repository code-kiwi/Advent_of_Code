def main_func():
    cubes = {"red": 12, "green": 13, "blue": 14}
    with open("./input2.txt", "r") as file:
        total = 0
        lines = file.readlines()
        # Each line is a game
        for line in lines:
            line_split = line.split("Game")[1].split(":")
            line = line_split[1].strip()
            index = int(line_split[0])
            possible = True
            rounds = line.split(";")
            # Testing every round of a game
            round_minimums = {"red": 0, "blue": 0, "green": 0}
            for round in rounds:
                # Extracting all the data from a round
                round_components = round.split(",")
                for round_component in round_components:
                    round_component = round_component.strip()
                    round_component_data = round_component.split()
                    if "red" in round_component_data[1]:
                        value = int(round_component_data[0])
                        if value > round_minimums["red"]:
                            round_minimums["red"] = value
                    elif "green" in round_component_data[1]:
                        value = int(round_component_data[0])
                        if value > round_minimums["green"]:
                            round_minimums["green"] = value
                    else:
                        value = int(round_component_data[0])
                        if value > round_minimums["blue"]:
                            round_minimums["blue"] = value
            # Getting game power and adding it to powers
            # print(index, ': ', round_minimums)
            total += (
                round_minimums["red"] * round_minimums["green"] * round_minimums["blue"]
            )
        print(total)


if __name__ == "__main__":
    main_func()
