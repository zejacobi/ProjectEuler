"""
# PROBLEM 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial

# Eh, I'm sure there's some smart mathy way to figure out the bounds on this problem, but I can't
# see it, so instead of elegant bounds checking (a la problem 25), I'm just going to use
# the trademark Zach Jacobi combination of inelegant heuristics, brute force, and ignorance!


threshold = 100000

valid = []

last = 2
current = 2

while (current - last) < threshold:
    current += 1
    if current == sum([factorial(int(i)) for i in str(current)]):  # I regret nothing
        # you know, if I knew the bounds, I could do this whole thing in one horrible line
        # it would be a double nested list comprehension.
        print(current)
        last = current
        valid.append(current)


print(sum(valid))

# ONE LINE SOLUTION!
print(sum([i for i in range(3, 50000) if i == sum([factorial(int(j)) for j in str(i)])]))