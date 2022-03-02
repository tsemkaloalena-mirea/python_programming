from random import choice, randrange


def generate_name(sex):
	female_names = ["Татьяна", "Мария", "Авдотья", "Елизавета"]
	male_names = ["Иван", "Андрей", "Яков", "Юрий"]
	female_endings = ["ина", "ая", "ская", "ко", "о", "як", "ич", "ова"]
	male_endings = ["ин", "ий", "ский", "ко", "о", "як", "ич", "ов"]
	vowels = ["у", "е", "ы", "а", "о", "э", "я", "и", "ю"]
	consonants = ["й", "ц", "к", "н", "г", "ш", "щ", "з", "х", "ф", "в", "п", "р", "л", "д", "ж", "э", "ч", "м", "т",
				  "б"]

	surname_start = ""
	for i in range(randrange(3, 8)):
		if i % 2 == 0:
			surname_start += choice(consonants)
		else:
			surname_start += choice(vowels)

	name = ""
	if sex == "female":
		name = choice(female_names)
		# name += " " + choice(male_names)[0] + ". "
		name += " " + chr(choice(range(ord('А'), ord('А') + 31))) + ". "
		name += surname_start[0].upper() + surname_start[1:] + choice(female_endings)
	elif sex == "male":
		name = choice(male_names)
		# name += " " + choice(male_names)[0] + ". "
		name += " " + chr(choice(range(ord('А'), ord('А') + 31))) + ". "
		name += surname_start[0].upper() + surname_start[1:] + choice(male_endings)
	return name


for _ in range(5):
	print(generate_name("female"))

for _ in range(5):
	print(generate_name("male"))
