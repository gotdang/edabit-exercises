"""
Find the Largest Even Number

Write a function that finds the largest even
number in a list. Return -1 if not found.
The use of built-in function max() is prohibited.

Examples:
largest_even([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10
largest_even([1, 3, 5, 7]) ➞ -1
largest_even([0, 19, 18973623]) ➞ 0

Notes:
Consider using the modulo operator % or the bitwise and operator &.
"""


def largest_even(lst):
    lst = sorted(i for i in lst if i % 2 == 0)
    return lst[-1] if len(lst) else - 1
