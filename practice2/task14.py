table = [["a11", "a102", "a1333", "a14"], ["a21", "a*/22", "a23", "a20004"]]


def count_horizontal_border_len():
    border_len = 0
    for i in range(len(table)):
        new_border_len = (sum(list(map(lambda x: len(x) + 2, table[i]))) + len(table[i]))
        if border_len < new_border_len:
            border_len = new_border_len
    return border_len


def count_vertical_border_len():
    border_len = [0] * len(table[0])
    for j in range(len(table[0])):
        new_border_len = max(list(map(lambda x: len(x[j]), table)))
        if border_len[j] < new_border_len:
            border_len[j] = new_border_len
    return border_len


horizontal_border_len = count_horizontal_border_len()
vertical_border_len = count_vertical_border_len()
print("+" + horizontal_border_len * "-" + "-+")
for i in range(len(table)):
    line = "| "
    for j in range(len(table[i])):
        line += table[i][j]
        line += " " * (vertical_border_len[j] - len(table[i][j]))
        line += " | "
    print(line)
    print("+" + horizontal_border_len * "-" + "-+")
