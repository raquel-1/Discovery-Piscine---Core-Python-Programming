#!/usr/bin/env python3
import sys
import re

if len(sys.argv) < 2:
	print("none")
else:
	i = 1
	while i < len(sys.argv):
		final_position = len(sys.argv[i]) - 3
		if sys.argv[i].find("ism", final_position) == -1:
			new = sys.argv[i] + "ism"
			print(new)
		i += 1
