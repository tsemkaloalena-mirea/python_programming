def fast_mul(x, y):
	result = 0
	while x >= 1:
		if x % 2 == 1:
			result += y
		y *= 2
		x //= 2
	return result


def test_fast_mul():
	for x in range(101):
		for y in range(101):
			result = fast_mul(x, y)
			assert result == x * y, f"wrong answer: {x} * {y} != {result}"
	print("correct")


def fast_pow(x, n):
	result = x
	for i in range(n - 1):
		result = fast_mul(result, x)
	return result


def test_fast_pow():
	for x in range(1, 101):
		for y in range(1, 101):
			result = fast_pow(x, y)
			assert result == x ** y, f"wrong answer: {x} ^ {y} != {result}"
	print("correct")


test_fast_mul()
# print(fast_mul(10, 15))
test_fast_pow()
# print(fast_pow(3, 2))
