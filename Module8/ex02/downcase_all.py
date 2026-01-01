#!/usr/bin/env python3
import sys

def upcase_it(word):
	return word.lower()

if len(sys.argv) < 2:
	print("none")
else:
	i = 1
	while i < len(sys.argv):
		print(upcase_it(sys.argv[i]))
		i += 1

