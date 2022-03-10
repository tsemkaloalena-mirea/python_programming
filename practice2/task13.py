import os, sys


def file_tree(start):
	graph = []
	for currentdir, dirs, files in os.walk(start):
		for file in files:
			file = file.split('.')[0]
			file = file.replace(" ", "_")
			if "\\" in currentdir:
				graph.append(currentdir.split("\\")[-1] + " -> " + file)
			else:
				graph.append(currentdir + " -> " + file)
		for directory in dirs:
			if "\\" in currentdir:
				graph.append(currentdir.split("\\")[-1] + " -> " + directory)
			else:
				graph.append(currentdir + " -> " + directory)
	print("digraph G {\n\t" + ";\n\t".join(graph) + ";\n}")


# file_tree("pack")
file_tree(sys.argv[1])
