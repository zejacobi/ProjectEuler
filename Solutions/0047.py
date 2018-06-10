"""
# Problem 47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
"""

# I distinctly recall hating factorization problems, although I can't remember why. Um. Let's
# go check through the other problems for other factorization problems?

# (At least python doesn't hate the unicode ² in the problem; it's previously thrown a fit about
# unicode characters and proper encodings)

# Well, I think the thing I hate is that they're slow. Now that I've realized I can just do trial
# division, this doesn't seem as bad. Although it was very slow before I hit on a memoization
# scheme to square root one of the n's inherent in trial division.

# The result is still inelegant, but it's better than trying to understand one of Wikipeida's
# "nicer" factorization algorithms, which are _dreadfully_ explained.

from math import sqrt

from Lib.Helpers import list_big_primes

primes = list_big_primes(100000)  # we can now search up to the square of the 100,000th prime

three_ago = False
two_ago = False
one_ago = False


past_factors = {}

for i in range(2 * 3 * 5, primes[-1] ** 2):
    if i in primes:
        one_ago = False
        two_ago = False
        three_ago = False
        continue

    factors = []
    for potential_factor in primes:
        if len(factors) > 4:
            break
        if potential_factor > sqrt(i):  # memoization makes the n sqrt'd, which is v. sweet.
            break
        if i % potential_factor == 0 and potential_factor not in factors:
            factors.append(potential_factor)
            other_factor = int(i / potential_factor)

            # at this point, the number is either prime, which means we can append it directly to
            # our factors and restrict our search to sqrt(i) and below, or it's composite, in which
            # case we already know all of its factors.
            if other_factor in primes and other_factor not in factors:
                factors.append(other_factor)

            elif past_factors.get(other_factor, None):
                for extra_factor in past_factors[other_factor]:
                    if extra_factor not in factors:
                        factors.append(extra_factor)

    past_factors[i] = factors

    if len(factors) == 4:
        if one_ago and two_ago and three_ago:
            print(three_ago)
            exit()
        else:
            three_ago = two_ago
            two_ago = one_ago
            one_ago = i
    else:
        one_ago = False
        two_ago = False
        three_ago = False
