#!/usr/bin/env python3
import sys

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def get_date(person):
	return person["date_of_birth"]

def famous_births(data):
	sort_data = sorted(data.values(), key = get_date ) #key=lambda person: person["date_of_birth"]
	
	for person in sort_data:
        	print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

famous_births(women_scientists)
