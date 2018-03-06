"""
# PROBLEM 32: Pandigital Products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly
once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a
1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your
sum.
"""

from math import log10

from Lib.Helpers import contains_all_numbers

valid_multipliers = []
valid_products = []
set_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# my range is too big here, but I don't know how to cleverly refine it
for i in range(1, 10000):
    str_i = str(i)
    if "0" in str(i):
        continue
    for j in range(1, 1 + 10 ** (5 - int(log10(len(str_i))))):
        # okay, let this count as "cleverly refining the range"
        # if my math is right, this should keep us from going too high above the range where
        # we have any chance of finding anything
        # wish I could figure out a sensible log for the starting point too; it shouldn't always
        # start at 1.
        str_j = str(j)
        if "0" in str_j:
            continue
        allowed = 9 - len(str_i) - len(str_j)

        if allowed <= 0:
            # we've overshot! There's not point in trying any more numbers with this i
            break
        product = i * j
        str_prod = str(product)

        if contains_all_numbers(str_prod + str_j + str_i, set_of_nums):
            valid_multipliers.append([i, j])
            valid_products.append(product)
        elif allowed - len(str_prod) < 0:
            # we've overshot, so there's no point in trying HIGHER numbers
            break
        else:
            # we've undershot, (or shot correctly but without the right combo) so we NEED to try
            # higher/more numbers
            continue

print(sum(set(valid_products)))