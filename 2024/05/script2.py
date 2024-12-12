import sys

def get_elts(lines):
    dic_elts = []
    pages = []
    doing_dic = True
    for line in lines:
        if line == '':
            doing_dic = False
            continue

        if doing_dic:
            dic_elts.append(line)
        else:
            pages.append(line)
    return dic_elts, pages

def make_dict(dict_elts):
    dict = {}
    for elt in dict_elts:
        temp = [int(val) for val in elt.split('|')]
        if (temp[0]) not in dict:
            dict[temp[0]] = []
        dict[temp[0]].append(temp[1])
    return dict

def main_func():
    # Opening the file
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    # Getting data from lines
    dict_elts, pages_lines = get_elts(lines)
    dict = make_dict(dict_elts)
    pages = [list(map(int, item.split(','))) for item in pages_lines]

    # Saving valid lines
    res = 0
    for page in pages:
        valid = False
        for i in range(len(page) - 1):
            # print(page[i], end=': ')
            for j in range(i + 1, len(page)):
                # print(page[j], end = ' ')
                if (page[i] in dict and page[j] not in dict[page[i]]) or (page[j] in dict and page[i] in dict[page[j]]):
                    page[i], page[j] = page[j], page[i]
                    valid = True
            # print()
        # print()
        if valid:
            res += page[(len(page) - 1) // 2]
    
    print(res)


if __name__ == "__main__":
    main_func()
