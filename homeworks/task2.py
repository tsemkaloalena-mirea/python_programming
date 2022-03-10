import math


def main(x):
    if x < 109:
        return x ** 4
    if 109 <= x < 143:
        return 18 * (12 * x) ** 3 - x ** 6
    a = (math.sin(74 * x ** 2 + 25 * x)) ** 7
    return a / 9 + (math.cos(x)) ** 2 / 34 + math.log(x, 2)
