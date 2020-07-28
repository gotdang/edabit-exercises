"""
Shuffle the Name

Create a function that takes a string (will be
a person's first and last name) and returns a
string with the first and last name swapped.

Examples:
name_shuffle("Donald Trump") ➞ "Trump Donald"
name_shuffle("Rosie O'Donnell") ➞ "O'Donnell Rosie"
name_shuffle("Seymour Butts") ➞ "Butts Seymour"
"""

def name_shuffle(name):
    parts = name.split(' ')
    return ' '.join(parts[::-1])

