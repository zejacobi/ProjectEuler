"""
# PROBLEM 37: Truncatable Primes
The number 3797 has an interesting property. Being prime itself, it is possible to continuously
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to
left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from Lib.Helpers import list_primes

list_truncatable = []
curr_index = 4
curr_limit = 100000

while len(list_truncatable) < 11:
    all_primes = list_primes(curr_limit)

    for prime in all_primes[curr_index:]:
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if int(str_prime[i:]) in all_primes and int(str_prime[:-i]) in all_primes:
                continue
            else:
                break
        else:
            list_truncatable.append(prime)

    curr_index = len(all_primes)
    curr_limit += 100000


print(sum(list_truncatable))
