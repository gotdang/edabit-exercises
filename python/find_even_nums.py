"""
Even Number Generator

Using list comprehensions, create a function that
finds all even numbers from 1 to the given number.

Examples:
find_even_nums(8) ➞ [2, 4, 6, 8]
find_even_nums(4) ➞ [2, 4
find_even_nums(2) ➞ [2]

Try to use list comprehensions in your solution. Here's an example:

vals = [expression
  for value in collection
    if condition]

This is equivalent to:

vals = []
for value in collection:
  if condition:
    vals.append(expression)

Notes
    Try to use list comprehensions instead of logic.
    If there are no even numbers, return an empty list.
"""


def find_even_nums(top):
    return [i for i in range(2, 1 + top) if not i % 2]
