"""
# PROBLEM 21
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are
called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt, ceil

amicable_numbers = []


def d(n):
    factors = []
    upper_bound = int(ceil(sqrt(n)))
    for i in range(2, upper_bound):
        if not n % i:
            factors.append(i)
            factors.append(n / i)
    return sum(factors) + 1


for number in range(1, 10000):
    if number not in amicable_numbers:
        potential_friend = d(number)
        if potential_friend != number and d(potential_friend) == number:
            # remember: we don't want to count a number if its divisor sum is itself
            amicable_numbers.append(number)
            if potential_friend < 10000: # we also don't want to count it if it's too big
                amicable_numbers.append(potential_friend)


print(sum(amicable_numbers))
