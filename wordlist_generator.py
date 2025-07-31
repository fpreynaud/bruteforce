#!/usr/bin/python

from argparse import ArgumentParser, RawTextHelpFormatter
from operations import *
import operations

if __name__ == '__main__':
	rules_help = """
Apply one or more transformations to the provided words. The basic transformations are the following:
- AppendYear : append numbers to the words (usually a year, but can actually be any number). One or more ranges can be specified with the --year-range option
- AppendSpecial : append special charaters to the words
- LowerCase : make the words lower case
- UpperCase : make the words upper case
- FirstUpper: make the first letter of the words uppercase, and leave the rest unchanged
- TitleCase : make the first letter of the words uppercase, and the rest lowercase
- BruteCase : apply all possible combination of cases to the words
- 1337 (or leet) : transform the words in l33t, in several manners
Those are case insensitive.
It is possible to combine these basic transformations to produce more complex ones. In the following examples, the base word will be "Word"
* Several keywords separated by a comma ',' defines a sequence of independent transformations
*     Example: AppendYear,UpperCase will produce Word2021, Word2022, WORD.
* Using a pipe '|' will compose the transformations, that is, transformations produced by an operation will be used as the input for the next operation
*     Example: BruteCase|AppendYear will produce word2021, word2022, Word2021, Word2022,..., WORD2021, WORD2022
"""
	parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
	parser.add_argument('word', nargs='*', help='Base words to use (typically customer name)')
	parser.add_argument('-o', '--output', help='Save wordlist in OUTPUT', default='-')
	parser.add_argument('--rules', default='lowercase', help=rules_help)
	parser.add_argument('--year-range', default='2020-2022', help='Years to use for AppendYear rule. Several range can be specified by separating them with a comma')
	args = parser.parse_args()
	wordlistFile = None
	if args.output != '-':
		wordlistFile = open(args.output, 'w')

	operations.year_range = args.year_range
	operations_map = {
		'appendyear':do_append_year,
		'appendspecial':do_append_special,
		'lowercase':do_lowercase,
		'uppercase':do_uppercase,
		'titlecase':do_titlecase,
		'firstupper':do_firstupper,
		'brutecase':do_brutecase,
		'1337':do_l33t,
		'leet':do_l33t,
		'identity':do_nothing
	}

	sequence = args.rules.split(',')

	for word in args.word:
		for pipeline in sequence:
			seq = (word, )
			composition = pipeline.split('|')
			for operation in composition:
				seq = operations_map.get(operation.lower(), operations_map['identity'])(seq)

			for result in seq:
				if wordlistFile:
					wordlistFile.write(result + '\n')
				else:
					print(result)
	if wordlistFile:
		wordlistFile.close()
