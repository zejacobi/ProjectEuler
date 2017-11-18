"""
# PROBLEM 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import ceil

# Okay, so obviously a, b, and c must be constrained to be below 997.

# And a and b both need to be below 332 and 499 respectively. Which implies the lowest
# possible value for c is 334. But there has to be an upper bound to c as well that is actually
# lower than 997. Because 1 ^ 2 + 2 ^ 2 != 997 ^ 2.

# There's the ~ n ^ 2 complexity solution, which requires us to iterate a and b between
# The bounds we've established. Is there are smart way to work from both ends and iteratively
# Squeeze the values towards a solution, maybe in linear time?

# I can't think of what this might be, so I may as well just settle for a mildly smart
# brute-ish force solution

for a in range(1, 333):
    for b in range(a + 1, int(500 - ceil(a/2) + 1)):
        c = 1000 - b - a
        # Note that when a is even, we need to remove the case where b == c
        if c > b and (a ** 2 + b ** 2) == c ** 2:
            print(a, b, c, a * b * c)
            exit(0)
            # we've been assured there's only one possible number, so exit with no error here

exit(1)  # something obviously has gone wrong.
