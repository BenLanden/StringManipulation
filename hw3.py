s = "BEEKEEPER"
binarydict = {
	"B": "1 ",
	"E": "0 ",
	"K": "01 ",
	"P": "00 ",
	"R": "10 "
}

def binary_replace(string, dictionary):
	for letter in string:
		if letter in dictionary.keys():
			string = string.replace(letter, dictionary[letter])

	return string

print(binary_replace(s, binarydict))
