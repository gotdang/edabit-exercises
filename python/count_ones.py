"""
Count Ones in Binary Representation of Integer

Count the amount of ones in the binary representation
of an integer. So for example, since 12 is '1100' in
binary, the return value should be 2.

Examples:
count_ones(0) ➞ 0
count_ones(100) ➞ 3
count_ones(999) ➞ 8

Notes:
The input will always be a valid integer (number).
"""

def count_ones(n):
    num_ones = 0
    while n > 0:
        num_ones += n % 2
        n >>= 1
    return num_ones
