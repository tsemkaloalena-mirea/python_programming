import sys


def change_quotes(file_name):
	file = open(file_name)
	output_file = open("markdown_output_file.html", 'w')
	text = file.read()
	code = False
	left_quote_found = False
	for i in range(len(text)):
		if text[i] == "<":
			code = True
		elif text[i] == ">":
			code = False
		if text[i] == '"' and not code:
			if not left_quote_found:
				left_quote_found = True
				text = text[:i] + '«' + text[i + 1:]
			else:
				left_quote_found = False
				text = text[:i] + '»' + text[i + 1:]

	output_file.write(text)
	file.close()
	output_file.close()
	return text


# print(change_quotes("markdown_file.html"))
change_quotes(sys.argv[1])
