"""
# PROBLEM 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
denominators 2 to 10 are given:

1/2  = 0.5
1/3  = 0.(3)
1/4  = 0.25
1/5  = 0.2
1/6  = 0.1(6)
1/7  = 0.(142857)
1/8  = 0.125
1/9  = 0.(1)
1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a
6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal
fraction part.
"""

# Oh my

# I could do a terrible string comparison thing using the decimal library, but that seems slow
# and also liable to break.

# Reading Wikipedia, it seems like you can find repeating decimals using long division
# https://en.wikipedia.org/wiki/Repeating_decimal#Decimal_expansion_and_recurrence_sequence

# Time to implement long division!

# (but first to screen for numbers that obviously suck)


def size_of_cycle(number):
    """Crude function that counts cycles in long division of 1 by various numbers"""
    cycles = 1

    def make_big_enough(n):
        while n < number:
            n *= 10
        return n

    start = make_big_enough(10)

    remainder = start % number
    figures = [start, start - remainder]

    if remainder == 0:
        return cycles
    else:
        current_num = make_big_enough(remainder)
        while current_num not in figures[:-1]:
            cycles += 1
            current_num = make_big_enough(current_num % number)
            figures.append(current_num)

        return cycles


min_len = len(str(1/3)) # make sure it is decently large (e.g. not like 1/4)

most_digits = 6  # this is the highest on the range [1, 10], so lets start with it and ignore them
d = 7

potential_numbers = [i for i in range(10, 1000) if len(str(1/i)) >= min_len]

# testing tells me that this eliminates only 23 numbers, so it isn't quite as good as I hoped

# man, sure wish I'd ever paid attention to long division in school.

for num in potential_numbers:
    repeating = size_of_cycle(num)
    if repeating > most_digits:
        most_digits = repeating
        d = num

print(d, most_digits)
