import re


def parse_subj(text):
	groups = []
	variants = []
	text = text.split()
	for word in text:
		if "Вариант№" in word:
			variants.append(word)
		elif word[:5] == "Вар№" and word[5:].isdigit() or word[:5] == "Вар-" and word[5:].isdigit() or word[:4] == "Вар" and word[4:].isdigit():
			variants.append(word)
		elif (word[0] == "в" or word[0] == "В" or word[0] == "v" or word[0] == "V") and word[1:].isdigit():
			variants.append(word)
		elif (word[:2] == "в№" or word[:2] == "В№" or word[:2] == "v№" or word[:2] == "V№") and word[2:].isdigit():
			variants.append(word)
		elif (word[:2] == "в-" or word[:2] == "В-" or word[:2] == "v-" or word[:2] == "V-") and word[2:].isdigit():
			variants.append(word)
		elif re.findall(r'и?бо-', word.lower()) or word[0].isalpha() and word[1:].isdigit() or word[0].isalpha() and word[2:].isdigit():
			groups.append(word)
	return groups, variants


print(parse_subj("jefn и7 в19 щ а-6 ewojf j7 Вариант№14 wq[k ДЛКЬ УОШАИ Икбо-01-20 ИВБО-05а 6"))
