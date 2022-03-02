import re


def parse_subj(text):
	text = text.split()
	group_letter = 0
	variant_number = 0
	for word in text:
		if re.findall(r'И?БО-', word):
			group_letter = word[word.find("И") + 1]
		if "Вариант№" in word:
			variant_number = word[word.find("Вариант№") + len("Вариант№"):]
	return group_letter, variant_number


print(parse_subj("jefn ewojf Вариант№14 wq[k ДЛКЬ УОШАИ Икбо-01-20 ИВБО-05а 6"))
