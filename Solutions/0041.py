"""
# Problem 41: Pandigital Prime
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly
once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

# from Lib.Helpers import list_big_primes, list_primes


# Well, this is reasonably easy! We just need to use our list_primes helper function to find
# all primes below 987654321.

# HAHAHAHA that was a funny joke! Turns out that we were loading basically 1,000,000,000 integers
# into memory, so, uh, that was bad (you might notice that if each integer was 1 byte, that would
# be 1GB. But of course, 1 byte only goes up to 255. Hmmm, can I write a generator version of that?

# list_primes(987654321)

# well, I'm back, after having read wikipedia until I could implement a partitioned prime sieve.
# It's approximately 31,426 times less memory intensive... (in this application)

# list_big_primes(987654321)

# Well, it may not write 10GB to swap, but it's still prohibitively slow.

# I think my best bet is actually to try all pandigital numbers that start with 9 and end with
# something that isn't 2, 4, 5, 6, 8, or 0. If none of these are prime, I can move on to 8 digit
# numbers with the same constraint, etc., etc.

# I'll need a quick way of checking if things are prime, maybe based off an adapted version of
# my new list_big_primes function

from Lib.Helpers import efficient_is_prime, list_primes
from math import ceil, sqrt

upper_limit = 987654321
prime_list_limit = int(ceil(sqrt(upper_limit)) + 1)
pregen_primes = list_primes(prime_list_limit)

# Adapting code from problem 38, focusing our search as high as possible, we can search like this.
# Note that if this comes up again, this should go in a friggen helper.

for size in range(9, 0, -1):

    def recursively_find_allowable_bases(current):
        if len(current) < size:
            for i in range(1, size):
                str_i = str(i)
                if str_i not in current and (len(current) != size - 1 or str_i not in ['0', '2', '4', '6', '8', '5']):
                    recursively_find_allowable_bases(current + str_i)
        elif current not in numbers:
            numbers.append(int(current))

    for start in range(size, 0, -1):
        numbers = []
        recursively_find_allowable_bases(str(start))

        primes = [number for number in numbers if efficient_is_prime(number, prime_list_limit, pregen_primes)]

        if len(primes):
            print(sorted(primes)[-1])
            exit()
