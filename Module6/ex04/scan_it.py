#!/usr/bin/env python3
import sys
import re

if len(sys.argv) < 3:
	print("none")
else:
	needle = sys.argv[1]
	haystack = sys.argv[2]
	matches =  re.findall(needle, haystack)
	print(len(matches))
