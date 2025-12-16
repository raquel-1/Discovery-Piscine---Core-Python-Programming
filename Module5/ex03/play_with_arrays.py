#!/usr/bin/env python3
ori = [2, 8, 9, 48, 8, 22, -12, 2]
new = []

#Itero sobre array, creando un nuevo array
i = 0
while i < len(ori):
	if ori[i] > 5:
		value = ori[i] + 2
		new.append(value)
	i += 1
s = set(new)
print(f"Original array: {ori}")
print(f"New array: {s}")
