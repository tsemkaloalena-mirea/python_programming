import math


def main(x):
    s = 0
    for i in range(len(x)):
        s += 35 * (63 * x[i] + 31 + x[i] ** 2) ** 3
    return 78 * s
