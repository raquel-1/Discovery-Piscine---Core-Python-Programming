#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
	print("none")
else:
	# sys.argv[0] es "./count_it.py"
	# sys.argv[1:] son ["Game", "of", "Thrones"]
	parameters = sys.argv[1:]
	print(f"parameters: {len(parameters)}")
	for p in parameters:
		print(f"{p}: {len(p)}")
