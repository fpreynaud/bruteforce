from functools import reduce
year_range = '2021-2022'

def do_append_year(seq):
	def years(ranges):
		rangeList = ranges.split(',')
		for yearRange in rangeList:
			yearList = yearRange.split('-')
			n = len(yearList)
			if n > 2:
				raise ValueError(f'Invalid year range {yearRange}')
			elif n == 0:
				continue
			elif n == 1:
				yield yearList[0]
			else:
				start, end = yearList
				start = int(start)
				end = int(end)

				if start > end:
					raise ValueError(f'Invalid year range {yearRange}')
				for year in range(start, end+1):
					yield year

	for word in seq:
		for year in years(year_range):
			yield f'{word}{year}'

def do_lowercase(seq):
	for word in seq:
		yield f'{word.lower()}'

def do_append_special(seq):
	specials = ['!', '$', '*']
	for word in seq:
		for special in specials:
			yield f'{word}{special}'

def do_uppercase(seq):
	for word in seq:
		yield f'{word.upper()}'

def do_firstupper(seq):
	for word in seq:
		if word == "":
			yield word
		else:
			yield word[0].upper() + word[1:]

def do_titlecase(seq):
	for word in seq:
		yield f'{word.title()}'

def do_brutecase(seq):
	for elt in seq:
		word = elt.lower()
		while word != elt.upper():
			yield word
			index = 0
			while index < len(word) and (word[index].isupper() or not word[index].isalpha()):
				index += 1
			word = word[:index].lower() + word[index].upper() + word[index+1:]
		yield word

def do_l33t(seq):
	substitutions = {
		'e':('3',),
		'i':('!',),
		'o':('0',),
		't':('7',),
		'k':('|<',),
		'p':('|*',),
		'q':('*|',),
		'r':('|2',),
		'u':('|_|',),
		'a':('4', '@'),
		'c':('(', '<'),
		's':('5', '$'),
		'b':('8', '|3'),
		'l':('1', '|_'),
		'h':('#', '|-|'),
		'm':('|V|', '|\\/|',)
	}

	for word in seq:
		if len(word) == 1:
			yield word
			for replacement in substitutions.get(word, word):
				yield replacement
		else:
			for s in do_l33t((word[1:],)):
				yield word[0] + s
			if word[0].lower() in substitutions:
				for replacement in substitutions[word[0]]:
					for s in do_l33t((word[1:],)):
						yield replacement + s

def do_nothing(seq):
	for word in seq:
		yield word

