#!/usr/bin/python
import re

words = open('/usr/share/dict/words','r')
length = raw_input('enter word len : ')
pattern = str(raw_input('enter pattern : '))
pattern = pattern.replace('?','\w')
print ''
for word in words:
	if len(word)== int(length)+1 and re.search(pattern,word):
		print word.strip()

