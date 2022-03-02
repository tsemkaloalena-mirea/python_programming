s = ["1", "5", "9", "7", "1", "585", "3", "67", "7", "4", "9", "5", "4", "3", "6", "4", "1"]

x1 = list(map(lambda x: int(x), s))
x2 = len(set(s))
x3 = [s[i] for i in range(len(s) - 1, -1, -1)]
x4 = [i for i in range(len(s)) if s[i] == "1"]
x5 = sum([int(s[i]) for i in range(0, len(s), 2)])
x6 = sorted(s, key=lambda x: len(x))[-1]

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
