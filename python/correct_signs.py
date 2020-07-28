"""
Create a function that returns true if a given inequality
expression is correct and false otherwise.

Examples:
correct_signs("3 < 7 < 11") ➞ True
correct_signs("13 > 44 > 33 > 1") ➞ False
correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
"""

import re

COMPARISONS_RE = re.compile(r'\d+|<|>')


def correct_signs(txt):
    """Evaluates the inequality expression in txt,
    and returns True or False,
    based on whether the inequality is correct."""
    txt = txt.replace(' ', '')
    terms = COMPARISONS_RE.findall(txt)
    t_0 = int(terms.pop(0))
    while terms:
        op = terms.pop(0)
        t_1 = int(terms.pop(0))
        if t_0 <= t_1 and op == '>':
            return False
        if t_0 >= t_1 and op == '<':
            return False
        t_0 = t_1
    return True


def main():
    print(f'correct_signs("3 < 7 < 11") ➞ True == {correct_signs("3 < 7 < 11")}')
    print(f'correct_signs("13 > 44 > 33 > 1") ➞ False == {correct_signs("13 > 44 > 33 > 1")}')
    print(f'correct_signs("1 < 2 < 6 < 9 > 3") ➞ True == {correct_signs("1 < 2 < 6 < 9 > 3")}')


if __name__ == "__main__":
    main()
