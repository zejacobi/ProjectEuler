"""
# Problem 46: Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of
a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from math import sqrt, ceil

from Lib.Helpers import list_big_primes

primes = list_big_primes(200000)  # I don't know how big this number is and will adjust this as
# needed.


def check_conjecture(odd_number):
    """Gives true if the conjecture is fulfilled for the number, false otherwise."""
    squares_limit = int(ceil(sqrt(odd_number / 2)))

    for square in range(1, squares_limit):
        if (odd_number - 2 * square ** 2) in primes:
            break
    else:
        return False
    return True


for i in range(3, 200000, 2):
    if i not in primes:
        if not check_conjecture(i):
            print(i)
            exit()
