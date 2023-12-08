def clean_numbers(numbers):
    res = []
    for number in numbers:
        if number.isdigit():
            res.append(int(number))
    return res


def main_func():
    with open("./input1.txt", "r") as file:
        # with open('./testinput.txt', 'r') as file:
        lines = file.readlines()
        nb_lines = len(lines)

        # Initializing our result structure
        result_structure = []
        for i in range(nb_lines):
            result_structure.append(1)

        # Getting every line of the file
        for index, line in enumerate(lines):
            card_info = line.split(":")[1].split("|")
            winning_numbers_dirty = card_info[0].strip().split(" ")
            chosen_numbers_dirty = card_info[1].strip().split(" ")
            winning_numbers = clean_numbers(winning_numbers_dirty)
            chosen_numbers = clean_numbers(chosen_numbers_dirty)
            current_score = 0
            for number in chosen_numbers:
                if number in winning_numbers:
                    current_score += 1
            i = index + 1
            while i < nb_lines and current_score > 0:
                result_structure[i] += result_structure[index]
                i += 1
                current_score -= 1
        print(result_structure)
        print(sum(result_structure))


if __name__ == "__main__":
    main_func()
