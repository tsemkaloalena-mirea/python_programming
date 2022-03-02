from itertools import groupby


def rle_encode(data):
	return [(k, len(list(g))) for k, g in groupby(data)]


def direct_conversion(text):
	transpositions = []
	new_text = ""
	for i in range(len(text)):
		transpositions.append(text)
		text = text[-1] + text[:-1]
	transpositions.sort()
	for elem in transpositions:
		new_text += elem[-1]
	return new_text


def reverse_conversion(text):
	table = [""] * len(text)
	for i in range(len(text)):
		for j in range(len(table)):
			table[j] = text[j] + table[j]
		table.sort()
	return "\n".join(table)


text = "SIX MIXED PIXIES SIFT SIXTY PIXIE DUST BOXES"
# text = ".BANANA."
print(direct_conversion(text))
print(reverse_conversion(direct_conversion(text)))
print(rle_encode(text))
