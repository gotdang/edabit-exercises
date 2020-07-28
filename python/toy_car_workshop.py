"""
Toy Car Workshop

You work in a toy car workshop, and your job is
to build toy cars from a collection of parts.
Each toy car needs 4 wheels, 1 car body, and 2
figures of people to be placed inside.
Given the total number of wheels, car bodies and
figures available, how many complete toy cars
can you make?

Examples:
cars(2, 48, 76) ➞ 0
# 2 wheels, 48 car bodies, 76 figures
cars(43, 15, 87) ➞ 10
cars(88, 37, 17) ➞ 8
"""

WHEELS = 4
BODY = 1
FIGURES = 2

def cars2(w, b, f):
    num_cars = 0
    while w >= WHEELS and b >= BODY and f >= FIGURES:
        num_cars += 1
        w -= WHEELS
        b -= BODY
        f -= FIGURES
    return num_cars


def cars(w, b, f):
    return min(w // WHEELS, b // BODY, f // FIGURES)
