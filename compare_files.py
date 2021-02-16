import os
import numpy as np

def levenshtein(seq1, seq2):
	size_x = len(seq1) + 1
	size_y = len(seq2) + 1
	matrix = np.zeros ((size_x, size_y))
	for x in range(size_x):
		matrix [x, 0] = x
	for y in range(size_y):
		matrix [0, y] = y

	for x in range(1, size_x):
		for y in range(1, size_y):
			if seq1[x-1] == seq2[y-1]:
				matrix [x,y] = min(
					matrix[x-1, y] + 1,
					matrix[x-1, y-1],
					matrix[x, y-1] + 1
				)
			else:
				matrix [x,y] = min(
					matrix[x-1,y] + 1,
					matrix[x-1,y-1] + 1,
					matrix[x,y-1] + 1
				)
	#print (matrix)
	return (matrix[size_x - 1, size_y - 1])

# read files
files = []
file_names = []
file_name_lengths = []
for file_name in os.listdir("files"):
	with open("files/"+file_name, 'r') as reader:
		files.append(reader.read())
	file_names.append(file_name)
	file_name_lengths.append(len(file_name))

print("".rjust(max(file_name_lengths), ' '), end=" ")
for x in range(0, len(file_names)):
	print(file_names[x], end=" ")
print("", end="\n")

for y in range(0, len(files)):
	print(file_names[y], end=" ")
	for x in range(0, len(files)):
		similarity = 100 - (levenshtein(files[y], files[x]) / len(files[y]) * 100)
		print("{:.0f}%".format(similarity).rjust(len(file_names[x]), ' '), end=" ")
	print("", end="\n")
