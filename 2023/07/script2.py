from functools import cmp_to_key


def get_hand_val(hand):
    hand_component = {}
    for card in hand:
        if card in hand_component:
            hand_component[card] += 1
        else:
            hand_component[card] = 1

    # Dealing with J as Jocker
    keys = hand_component.keys()
    if "J" in keys and hand_component["J"] != 5:
        nb_J = hand_component["J"]
        del hand_component["J"]
        max_key = ""
        max_val = 0
        for key in keys:
            if hand_component[key] > max_val:
                max_key = key
                max_val = hand_component[key]
        hand_component[max_key] += nb_J

    nb_diff_cards = len(hand_component.keys())
    if nb_diff_cards == 1:
        return 6
    if nb_diff_cards == 2:
        for value in hand_component.values():
            if value == 4:
                return 5
        return 4
    if nb_diff_cards == 3:
        for value in hand_component.values():
            if value == 3:
                return 3
        return 2
    if nb_diff_cards == 4:
        return 1
    return 0


def get_card_val(card):
    if card.isdigit():
        return int(card)
    if card == "T":
        return 10
    if card == "J":
        return 1
    if card == "Q":
        return 12
    if card == "K":
        return 13
    return 14


def compare_card_by_card(hand1, hand2):
    for i in range(len(hand1)):
        card1_val = get_card_val(hand1[i])
        card2_val = get_card_val(hand2[i])
        if card1_val != card2_val:
            break
    return card1_val - card2_val


def hands_sort(hand1, hand2):
    hand1_val = get_hand_val(hand1["hand"])
    hand2_val = get_hand_val(hand2["hand"])
    if hand1_val != hand2_val:
        return hand1_val - hand2_val
    return compare_card_by_card(hand1["hand"], hand2["hand"])


def main_func():
    with open("./input1.txt", "r") as file:
        # with open("./testinput.txt", "r") as file:
        lines = file.readlines()

        # Storing hands
        hands = []
        for line in lines:
            line_content = line.strip().split()
            hands.append({"hand": line_content[0], "bid": int(line_content[1])})

        # Sorting the hands according to their values
        hands = sorted(hands, key=cmp_to_key(hands_sort))

        # Culculating and printing the result
        res = 0
        for index, hand in enumerate(hands):
            res += (index + 1) * hand["bid"]
        print(res)


if __name__ == "__main__":
    main_func()
