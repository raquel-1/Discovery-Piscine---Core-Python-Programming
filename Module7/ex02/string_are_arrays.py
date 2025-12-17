#!/usr/bin/env python3
import sys
import re

if len(sys.argv) < 2:
	print("none")
else:
	i = 0
	while i < len(sys.argv[1]) - 1:
		if sys.argv[1][i] == "z":
			print(sys.argv[1][i], end = "")
		i += 1
