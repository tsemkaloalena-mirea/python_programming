def transpose(table):
    new_table = []
    for i in range(len(table[0])):
        line = []
        for j in range(len(table)):
            line.append(table[j][i])
        new_table.append(line)
    return new_table


def remove_repeating_rows(table):
    new_table = []
    for i in range(len(table)):
        if table[i] not in new_table and table[i] != [None] * len(table[i]):
            new_table.append(table[i])
    return new_table


def remove_empty_rows(table):
    new_table = []
    for i in range(len(table)):
        if table[i] != [None] * len(table[i]):
            new_table.append(table[i])
    return new_table


def divide_column_by_symbol(table):
    for i in range(len(table)):
        x, y = table[i][-1].split("&")
        table[i][-1] = y
        table[i].insert(1, x)
    return table


def edit_mail(table):
    for i in range(len(table)):
        table[i][0] = table[i][0].split("[at]")[-1]
    return table


def edit_numbers(table):
    for i in range(len(table)):
        numbers = table[i][-2]
        table[i][-2] = "(" + numbers[:3] + ") "\
                       + numbers[3:6] + "-" + numbers[6:]
        table[i][-1] = str(int(round(float(table[i][-1]), 2) * 100)) + "%"
    return table


def main(table):
    table = transpose(remove_repeating_rows(transpose(table)))
    table = remove_empty_rows(table)
    table = divide_column_by_symbol(table)
    table = edit_mail(table)
    table = edit_numbers(table)
    table = transpose(table)
    return table


print(main([['odissej13[at]yahoo.com', 'odissej13[at]yahoo.com', '1573517278&0.385'],
            ['vladislav42[at]yandex.ru', 'vladislav42[at]yandex.ru', '6442266742&0.228'],
            [None, None, None],
            ['kusman13[at]yahoo.com', 'kusman13[at]yahoo.com', '0042746813&0.339'],
            [None, None, None],
            ['evgenij88[at]mail.ru', 'evgenij88[at]mail.ru', '5059643119&0.990']]))
