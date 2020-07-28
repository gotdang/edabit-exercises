"""
Convert Year to Century

Write a function that takes a year and
returns its corresponding century.

Examples:
century_from_year(2005) ➞ 21
century_from_year(1950) ➞ 20
century_from_year(1900) ➞ 19
"""


def century_from_year(year):
    return 1 + (year - 1) // 100
