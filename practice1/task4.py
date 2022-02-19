def f_12_4(x):
	x = x + x
	x = x + x
	x = x + x + x
	return x


def f_16_4(x):
	x = x + x
	x = x + x
	x = x + x
	x = x + x
	return x


def f_15_3_2(x):
	z = x
	x = x + x  # 2
	x = x + x  # 4
	x = x + x  # 8
	z = z - x
	x = x - z
	return x


def task4(x):
	x2 = x + x
	x4 = x2 + x2
	x8 = x4 + x4
	x7 = x8 - x
	x14 = x7 + x7
	x28 = x14 + x14
	return x28 + x
