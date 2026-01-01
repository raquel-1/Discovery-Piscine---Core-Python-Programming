#!/usr/bin/env python3
import sys

def shrink(word):
	print(f"{word[:8]}")
def enlarge(word):
	while len(word) < 8:
		word += "Z"
	print(word)

if len(sys.argv) < 2:
	print("none")
else:
	i = 1
	while i < len(sys.argv):
		if len(sys.argv[i]) > 8:
			shrink(sys.argv[i])
		elif len(sys.argv[i]) < 8:
			enlarge(sys.argv[i])
		else:
			print(f"{sys.argv[i]}")
		i += 1

