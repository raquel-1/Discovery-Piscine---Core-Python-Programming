#!/usr/bin/env python3
n = [2, 8, 9, 48, 8, 22, -12, 2]
new = []

#Itero sobre array, creando un nuevo array
a = 0
while a < len(n):
	value = n[a] + 2
	new.append(value)
	a += 1

print(f"Original array: {n}")
print(f"New array: {new}")

