#!/usr/bin/env python3
import sys

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

def array_of_names(persons):
    names = []
    for first, last in persons.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        names.append(full_name)
    return names

print(array_of_names(persons))
