def remove_extra_rows(table):
    new_table = []
    for i in range(len(table)):
        if table[i] not in new_table and table[i] != [None] * len(table[i]):
            new_table.append(table[i])
    return new_table


def divide_first_column(table):
    for i in range(len(table)):
        x, y = table[i][0].split("|")
        table[i][0] = x
        table[i].insert(1, y)
    return table


def transpose(table):
    new_table = []
    for i in range(len(table[0])):
        line = []
        for j in range(len(table)):
            line.append(table[j][i])
        new_table.append(line)
    return new_table


def transform_view(table):
    for i in range(len(table)):
        date = table[i][0].split(".")
        date = [date[-1][2:], date[1], date[0]]
        table[i][0] = "-".join(date)
        table[i][1] = table[i][1].split()[-1]
        table[i][2] = "%.4f" % float(table[i][2])
    return table


def main(table):
    table = transpose(table)
    table = remove_extra_rows(table)
    table = transpose(table)
    table = remove_extra_rows(table)
    table = divide_first_column(table)
    table = transform_view(table)
    table = sorted(table, key=lambda x: x[1])
    return table


print(main([[None, "10.07.2003|Р.О. Цонберг", None, "0.59", "0.59"],
            [None, "10.07.2003|Р.О. Цонберг", None, "0.59", "0.59"],
            [None, None, None, None, None],
            [None, "21.06.2003|З.Ш. Руфий", None, "0.33", "0.33"],
            [None, "19.11.2001|Т.З. Зочко", None, "0.49", "0.49"],
            [None, "10.07.2003|Р.О. Цонберг", None, "0.59", "0.59"],
            [None, "16.10.2000|Д.А. Возабин", None, "0.14", "0.14"]]))
