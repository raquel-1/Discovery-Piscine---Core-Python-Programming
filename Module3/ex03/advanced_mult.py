#!/usr/bin/env python3
i = 0
while i < 11:
	print(f"Table of {i}: ", end=" ")
	j = 0
	while j < 11:
		print(f"{j * i} ", end=" ")
		j += 1
	print("")
	i += 1
