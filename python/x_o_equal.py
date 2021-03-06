"""
Xs and Os, Nobody Knows

Create a function that takes a string, checks if
it has the same number of "x"s and "o"s and
returns either True or False.

Return a boolean value (True or False).
The string can contain any character.
When no x and no o are in the string, return True.

Examples:
XO("ooxx") ➞ True
XO("xooxx") ➞ False
XO("ooxXm") ➞ True
# Case insensitive.
XO("zpzpzpp") ➞ True
# Returns True if no x and o.
XO("zzoo") ➞ False

Notes:
Remember to return True if there aren't any x's or o's.
Must be case insensitive.
"""

def XO(s):
    s = s.lower()
    return sum(1 for x in s if x == 'x') == sum(1 for o in s if o == 'o')
