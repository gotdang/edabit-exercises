"""
Return the Factorial

Create a function that takes an integer and returns
the factorial of that integer. That is, the integer
multiplied by all positive lower integers.

Examples:
factorial(3) ➞ 6
factorial(5) ➞ 120
factorial(13) ➞ 6227020800

Notes:
Assume all inputs are greater than or equal to 0.
"""


def factorial(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact
