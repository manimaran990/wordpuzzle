#!/usr/bin/python
import re
import sys

if len(sys.argv[:]) != 2:
	print "usage: ./puzzle.py 'pattern'"
	exit(0)

pattern = sys.argv[1]
length = len(pattern)
pattern = pattern.replace('?','\w')
words = open('/usr/share/dict/words','r')
print ''
for word in words:
	if len(word)== int(length)+1 and re.search(pattern,word):
		print word.strip()

