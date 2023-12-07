def main_func():
    cubes = {'red': 12, 'green': 13, 'blue': 14}
    with open('./input1.txt', 'r') as file:
        total = 0
        lines = file.readlines()
        # Each line is a game
        for line in lines:
            line_split = line.split('Game')[1].split(':')
            line = line_split[1].strip()
            index = int(line_split[0])
            possible = True
            rounds = line.split(';')
            print(index, ': ', end='')
            # Testing every round of a game
            for round in rounds:
                round_results = {'red': 0, 'blue': 0, 'green': 0}
                # Extracting all the data from a round
                round_components = round.split(',')
                for round_component in round_components:
                    round_component = round_component.strip()
                    round_component_data = round_component.split()
                    if ('red' in round_component_data[1]):
                        round_results['red'] = int(round_component_data[0])
                    elif ('green' in round_component_data[1]):
                        round_results['green'] = int(round_component_data[0])
                    else:
                        round_results['blue'] = int(round_component_data[0])
                # Verifying if the round is possible
                if (round_results['red'] > cubes['red'] or round_results['green'] > cubes['green'] or round_results['blue'] > cubes['blue']):
                    possible = False
                    break
            if possible == True:
                total += index
                print('OK')
            else:
                print('NOT OK')
        print(total)


if __name__ == '__main__':
    main_func()
