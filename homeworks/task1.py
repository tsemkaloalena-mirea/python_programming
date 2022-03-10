import math


def main(x, y, z):
    a = 34 * (math.sin(92 * y - 14 * z ** 3 - 28 * y ** 2)) ** 7
    b = 50 * ((66 * x ** 3 + 0.01 + z) ** 2)
    c = x ** 6 + 69 * math.tan(y ** 2 - 1 - 92 * z ** 3)
    d = 57 * (1 + 25 * y ** 3) ** 3
    e = math.log(43 * x ** 2 - z / 32 - z ** 3, 2) ** 4
    return a - b - c / (d - e)
