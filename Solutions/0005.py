"""
# PROBLEM 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# This is equivalent to "what is the smallest number that can be divided by each prime
# number between 1 and 20 without any remainder", right?

# Or is it slightly different? I guess more accurate is to say "divided by each number that
# isn't a divisor of another number in the set. So 20 is in even though it isn't prime,
# but 2, 4, 5, and 10 are out by virtue of being a divisor of 20.

all_numbers = [i+2 for i in range(19)]

numbers = [number for number in all_numbers
           if not any([i % number == 0 for i in all_numbers if number != i and number < i])]

# After I printed this out, I realized that the presence of 2 actually just reduces this to
# "all numbers > 10". But I'm leaving this here as a testament to how I figured it out.

# This number must be at least 2520, right?

candidate = 2520
while True:
    if all([candidate % i == 0 for i in numbers]):
        break
    else:
        candidate += 20  # our number has to be divisible by 20

print(candidate)

# Given how long this took to run, I'm guessing the answer was probably just the multiplication
# of 11-20.

print(11*12*13*14*15*16*17*18*19*20)

# Huh, nope, it's actually much lower. Nifty.
