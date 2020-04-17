import re

def split_tokens(word):
	return tuple([r for r in re.split(r"([A-Z][a-z]?)", word) if len(r) > 0 and r != '\n'])


def read_input(filename):
	conversions = {}
	data = ""

	with open(filename) as f:
		for line in f:
			if "=>" in line:
				before, after = line.split(" => ")
				if before == 'e':
					conversions[split_tokens(after)] = (before,)
				else:
					conversions[split_tokens(after)] = split_tokens(before)
			else:
				data = line

	return conversions, data

# def substitute_token(t, i, token):
# 	return t[0:i] + (token,) + t[i+1:]


def magnify_conversions(conversions):
	#Take a dict of conversions and return a dict with each key containing the before/after part of the conversion
	new_conversions = {}
	for c in conversions.keys():
		for i in range(len(c)):
			before = c[0:i]
			after = c[i+1:]
			new_key = (before, after)
			new_conversions[new_key] = conversions[c]
	return new_conversions


def indices_of_subsequence(molecule, sequence):
	indices = []
	for i, m in enumerate(molecule):
		if len(molecule[i:]) < len(sequence):
			break
		if m == sequence[0]:
			#Matched the start of the sequence
			l = len(sequence)
			if molecule[i:i+l] == sequence:
				indices.append(i)
	return indices



def find_precursors(full_molecule, conversions):
	pass



if __name__ == "__main__":
	conversions, data = read_input("input.txt")
	# new_conversions = magnify_conversions(conversions)
	mol = split_tokens(data)

	print([indices_of_subsequence(mol, key) for key in conversions.keys()])
	#print(conversions.keys())

