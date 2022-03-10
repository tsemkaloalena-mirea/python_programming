import math


def f(n):
    if n == 0:
        return 0.67
    a = f(n - 1)
    return a ** 2 / 46 - math.atan(1 + a ** 3 + 87 * a) ** 3 - math.fabs(a)


def main(n):
    return f(n)
