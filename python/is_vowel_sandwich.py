"""
Vowel Sandwich

Create a function which validates whether a 3-character
string is a vowel sandwich. In order to have a valid
sandwich, the string must satisfy the following rules:

    The first and last characters must be a consonant.
    The character in the middle must be a vowel.

Examples:
isVowelSandwich("cat") ➞ true
isVowelSandwich("ear") ➞ false
isVowelSandwich("bake") ➞ false
isVowelSandwich("try") ➞ false

Notes
    Return false if the word is not 3 characters in length.
    All words will be given in lowercase.
    y is not considered a vowel.
"""

import string

VOWELS = ['a', 'e', 'i', 'o', 'u']
CONSONANTS = [c for c in string.ascii_lowercase if c not in VOWELS]

def is_vowel_sandwich(s3):
    return (s3 and len(s3) == 3
        and s3[0] in CONSONANTS
        and s3[1] in VOWELS and s3[2] in CONSONANTS)
