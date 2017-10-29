"""
# PROBLEM 3
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math

# I don't actually know an efficient algorithm for factoring or finding primes.
# Googling leads me to Pollard's rho algorithm, which seems cool, but also like overkill
# here. I think I'll just try exhaustive search, but this is a good one to come back
# to if I want to learn some things about primes and factorization


def factor(n):
    """Simple factorization function. Makes sure to only try each number once."""
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if i not in factors and not n % i:
            factors.append(i)
            factors.append(n / i)
    return factors


found_factors = factor(600851475143)

prime_factors = sorted([i for i in found_factors if not factor(i)])

print(prime_factors[-1])
