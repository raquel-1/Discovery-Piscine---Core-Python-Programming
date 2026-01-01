#!/usr/bin/env python3
def greetings(word=None):
	if word is None:
		print(f"Hello, noble stranger.")
	elif isinstance(word, str) == True:
		print(f"Hello, {word}.")
	else:
		print("Error! It was not a name.")
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
