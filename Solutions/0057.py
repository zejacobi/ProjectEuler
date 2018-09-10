"""
# Problem 57: Square root convergents

It is possible to show that the square root of two can be expressed as an infinite continued
fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
is the first example where the number of digits in the numerator exceeds the number of digits
in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than
denominator?
"""

# Python is a bro
from fractions import Fraction

# Fractions was the only thing that gave enough precision to make this workable
# I know this is basically cheating, but I spent more than an hour fruitlessly trying to make this
# work, so, meh.

bigger = 0

for n in range(1000):
    counter = n
    divisor = Fraction(2)

    while counter > 0:
        counter -= 1
        divisor = Fraction(2) + Fraction(1) / divisor

    value = Fraction(1) + Fraction(1) / divisor
    frac = str(value).split('/')
    if len(frac[0]) > len(frac[1]):
        bigger += 1

print(bigger)