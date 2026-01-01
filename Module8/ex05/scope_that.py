#!/usr/bin/env python3
def add_one(par):
	par += 1

#En Python, los enteros son inmutables
#par es una copia del valor de number
#Cambiar par no cambia number

number = 5
print(number)
add_one(number)
print(number)

