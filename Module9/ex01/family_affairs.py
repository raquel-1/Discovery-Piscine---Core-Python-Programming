#!/usr/bin/env python3
import sys

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

def find_the_redheads(data):
	return list(filter(lambda name: data[name] == "red", dupont_family))


print(find_the_redheads(dupont_family))
