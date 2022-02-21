def fast_mul_gen(y, need_to_print=False):
	x_list = [12, 16, 15, 29]
	results = []
	for x in x_list:
		if need_to_print:
			print("f(" + str(x) + "):")
			print("result = 0")
		new_y = y
		result = 0
		y_for_output = "y"
		while x >= 1:
			if x % 2 == 1:
				if need_to_print:
					# print("result = " + str(result) + " + " + str(new_y))
					print("\tresult = result + " + y_for_output)
				result += new_y
			new_y *= 2
			x //= 2
			y_for_output += " * 2"
		results.append(result)
	return results


def test_fast_mul_gen():
	for x in range(1, 101):
		results = fast_mul_gen(x)
		assert results == [12 * x, 16 * x, 15 * x,  29 * x], f"wrong answer for {x}: the result is {results}, but {[12, 16, 15, 29] * x} was expected"
	print("correct")


def fast_pow_gen(x, n, need_to_print=False):
	answer = x
	if need_to_print:
		print(f"f({n}):")
	for i in range(n - 1):
		new_x = x
		new_y = answer
		result = 0
		result_output = "0"
		new_y_output = f"x{i}"
		while new_x >= 1:
			if new_x % 2 == 1:
				result += new_y
				result_output += " + " + new_y_output
			new_y *= 2
			new_x //= 2
			new_y_output += " * 2"
		answer = result
		if need_to_print:
			print(f"\tx{i + 1} = {result_output}")
	return answer


def test_fast_pow_gen():
	for x in range(1, 101):
		for y in range(1, 101):
			result = fast_pow_gen(x, y)
			assert result == x ** y, f"wrong answer: {x} ^ {y} != {result}"
	print("correct")


fast_mul_gen(5, True)
test_fast_mul_gen()

fast_pow_gen(8, 3, True)
test_fast_pow_gen()
