#!/bin/python
#
# @author Martin Vician <info@vician.cz>
#

import sys
import itertools
import enchant
import numpy
import collections
from translate import Translator # https://github.com/terryyin/google-translate-python

# params
if len (sys.argv) != 3 :
	print "Wrong arguments (",len(sys.argv),")!"
	print "usage: "+sys.argv[0]+" chars length"
	exit(1)

# transalator
translator = Translator(from_lang="en",to_lang="cs")
# dictionary
d = enchant.Dict("en_US")

# get params
chars = sys.argv[1]
length = int(sys.argv[2])

words=[] # array for unique values
# all permutations
i = 0
for p in itertools.permutations(chars,length):
	i += 1
	print "\r",i,
	word = ''.join(p)
	if d.check(word):
		if word not in words: # already found
			words.append(word)
			print "\r",word,
			print "->",translator.translate(word),
			print "\n",

print "=> ",len(words)," exists words"
