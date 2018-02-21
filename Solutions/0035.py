"""
# PROBLEM 35: Circular Primes
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from Lib.Helpers import all_rotations, list_primes

# First thing I notice: the numbers between 100 and 1,000,000 can't have 5, 0, 2, 4, 6, or 8 in
# them. Because those will rotate into last position and make it not prime.

candidates = [i for i in range(100, 1000001) if
              '0' not in str(i) and
              '2' not in str(i) and
              '4' not in str(i) and
              '5' not in str(i) and
              '6' not in str(i) and
              '8' not in str(i)]

# this leaves a relatively small number of numbers, just 5440. Hence we don't really need to
# worry about efficiency from this point onwards, because n will now be tiny.

# That said: we should add all re-arrangements not already in the list and then skip any numbers
# that have already shown up

circular_primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]

primes = list_primes(1000000)

for x in candidates:
    if x not in circular_primes:
        rotations = all_rotations(x)
        novel = []
        for option in rotations:
            if option not in primes:
                break
        else:
            circular_primes += rotations

circular_primes = list(set(circular_primes))

print(len(circular_primes))