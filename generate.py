"""
Bruteforce generators
"""
import requests
from bruteforce.alphabets import *

def bf(alphabet='01', length=4):
	"""
	Bruteforce words of a specific length
	"""
	word = length * alphabet[0]
	index = -1
	while word != length * alphabet[-1]:
		yield word
		index = -1
		while word[index] == alphabet[-1] and index > -length:
			index -= 1
		word = word[:index] + alphabet[alphabet.index(word[index]) + 1] + alphabet[0] * (length - (len(word[:index]) + 1) )

	yield word

def bruteforce(alphabet='01', minlen=1, maxlen=5):
	"""
	Bruteforce words of length between minlen and maxlen
	"""
	for length in range(minlen, maxlen+1):
		for word in bf(alphabet,length):
			yield word
