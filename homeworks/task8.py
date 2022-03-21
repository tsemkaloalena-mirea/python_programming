def main(data):
    data = data.replace("\n", " ")
    data = data.lstrip("do do local array")
    data = data.strip('od end').strip().strip('.')
    data = data.split(". od do local array")
    dictionary = {}
    for line in data:
        values, key = line.split("=>")
        values = values.strip()
        values = values.lstrip("(")
        values = values.rstrip(")")
        values = values.split(";")
        values = list(map(lambda x: int(x.strip()), values))
        key = key.strip()
        dictionary[key] = values
    return dictionary
