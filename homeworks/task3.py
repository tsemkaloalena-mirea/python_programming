import math


def main(b, m, a):
    s = 0
    for c in range(1, a + 1):
        for j in range(1, m + 1):
            for k in range(1, b + 1):
                s += 34 * (math.tan(j)) ** 3 - 92 * (c ** 2 - k ** 3 - 1)
    return s
