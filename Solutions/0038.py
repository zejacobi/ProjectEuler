"""
# Problem #38: Pandigital Multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the
concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the
pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product
of an integer with (1,2, ..., n) where n > 1?
"""

from Lib.Helpers import contains_all_numbers

# One key thing to note is that we actually only care about numbers that start with 9...
# Anything else, and it _MUST_ be smaller than the example 918273645, which I know for a fact
# isn't the answer (I guessed it)

# This cuts down our solution space by a factor of 10. We also know it can't contain zero
# (because the multplication by one, which cuts things down even further. Also, it cannot contain
# more than one nine, or actually, more than any number once. This further cuts things down.

# There's something like 80 possible numbers below 987 and 800 below 9876

# There's one last thing; as our main number gets bigger, the amount of factors we can try
# gets smaller. There's no way we'll succeed with a number greater than 4 digits, given that
# n MUST be greater than 1

numbers = []


def recursively_find_allowable_bases(current):
    if current not in numbers:
        numbers.append(int(current))
        if len(current) < 4:
            for i in range(1, 9):
                str_i = str(i)
                if str_i not in current:
                    recursively_find_allowable_bases(current + str_i)


recursively_find_allowable_bases('9')

# 401 numbers at this point; that's very reasonable.

factors = [1, 2]

highest = 918273645


# I honestly don't see much point in being clever here. We're doing 8 * 401 operations.
while len(factors) < 9:
    for n in numbers:
        pan = ''.join([str(n * f) for f in factors])
        if contains_all_numbers(pan, [1, 2, 3, 4, 5, 6, 7, 8, 9]) and int(pan) > highest:
            highest = int(pan)

    factors.append(factors[-1] + 1)

print(highest)
# yeah that took basically no time
