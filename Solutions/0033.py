"""
PROBLEM 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and
containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the
denominator.
"""

import functools
import math

# <8,100 combos is small enough that I say fuck it, iterate

fractions = []

for i in range(10,99):
    for j in range(i+1, 100):
        actual = i / j
        first_frac = str(i)
        second_frac = str(j)
        for index1, digit1 in enumerate(first_frac):
            for index2, digit2 in enumerate(second_frac):
                # I don't care if quadruple nested for loops are "evil"; I know my bounds and I
                # code within them (this joke makes sense if you've heard too many OLG radio ads)
                # Here the bounds are 90 * 90 * 2 * 2 / 2; hardly a real problem
                if digit1 != '0' and digit1 == digit2 and second_frac[index2 - 1] != '0':
                    reduced = int(first_frac[index1 - 1]) / int(second_frac[index2 - 1])
                    if reduced == actual:
                        fractions.append((i, j))

numerator = functools.reduce(lambda x, y: x * y, [el[0] for el in fractions])
denominator = functools.reduce(lambda x, y: x * y, [el[1] for el in fractions])


def get_divisors(num):
    divisors = [[int(num/can), can] for can in range(1, int(math.ceil(math.sqrt(num))))
                if not num % can]
    final_divisors = []
    for divisor_pair in divisors:
        final_divisors += divisor_pair

    return sorted(list(set(final_divisors)))


def reduce_fraction(num, denom):
    numerator_divisors = get_divisors(num)
    denominator_divisors = get_divisors(denom)
    common = [divisor for divisor in numerator_divisors if divisor in denominator_divisors]
    if len(common) <= 1:
        return num, denom
    else:
        return reduce_fraction(int(num/common[-1]), int(denom/common[-1]))


print(reduce_fraction(numerator, denominator))
