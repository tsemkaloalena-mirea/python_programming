def fast_mul_gen(y, need_to_print=False):
	x_list = [12, 16, 15, 29]
	new_y = y
	results = []
	for x in x_list:
		if need_to_print:
			print("f(" + str(x) + "):")
		new_y = y
		result = 0
		while x >= 1:
			if x % 2 == 1:
				if need_to_print:
					print("result = " + str(result) + " + " + str(new_y))
				result += new_y
			new_y *= 2
			x //= 2
		results.append(result)
	return results


def test_fast_mul_gen():
	for x in range(1, 101):
		results = fast_mul_gen(x)
		assert results == [12 * x, 16 * x, 15 * x, 29 * x], f"wrong answer for {x}: the result is {results}, but {[12, 16, 15, 29] * x} was expected"
	print("correct")


fast_mul_gen(5, True)
test_fast_mul_gen()
