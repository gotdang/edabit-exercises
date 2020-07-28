"""
Factorial of a Number

Create a function that receives a non-negative
integer and returns the factorial of that number.

Examples:
fact(0) ➞ 1
fact(1) ➞ 1
fact(3) ➞ 6
fact(6) ➞ 720

Notes:
Avoid using built-in functions to solve this challenge.
"""


def fact(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product