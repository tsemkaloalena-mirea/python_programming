import sys


def print(*text, sep=" ", end="\n"):
	def get_str(sp):
		if isinstance(sp, str) or isinstance(sp, int) or isinstance(sp, bool):
			return str(sp)
		start = "["
		finish = "]"
		if isinstance(sp, tuple):
			start = "("
			finish = ")"
		elif isinstance(sp, set):
			start = "{"
			finish = "}"
		sp = list(sp)
		return start + ", ".join(list(map(lambda x: get_str(x), sp))) + finish

	text = list(text)
	if len(text) == 1:
		text = get_str(text[0])
	else:
		text = [get_str(elem) for elem in text]
		text = sep.join(text)
	sys.stdout.write(text + end)


print(4)
print({"hjdj", "a", "b"})
print(1, 5, 6, 9, sep=" ^ ")
print([[1, 6], 5], [6, 9])
print(True)
