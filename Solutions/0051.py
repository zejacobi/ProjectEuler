"""
# Problem 51
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the
first example having seven primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
with the same digit, is part of an eight prime value family.
"""

from Lib.Helpers import list_big_primes, list_primes

# Huh.

# I feel like the quickest way of doing this is to go primes and write down all the families
# they could be in. Or, hmm, this means that our algorithm looks like:

# 1) Get a prime number. See how many of each number it has.
# 2) Add each family to a dictionary with appropriate stars. E.g. 9973 gives dictionary entries
#    **73, 99*3, 997*
# 3) Keep track! Break when we get to 8.

goal = 8

prime_families = {}


def generate_families(n):
    families = []
    n = str(n)
    observed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in str(n):
        observed[int(i)] += 1

    for digit, existed in enumerate(observed):
        if existed == 1:
            families.append(n.replace(str(digit), '*'))
        elif existed > 1:
            # ugh this isn't elegant, but at least n is small
            we_care_about = str(digit)
            combinations = [n]
            for index, original in enumerate(n):
                if original == we_care_about:
                    for combo in combinations[:]:
                        combinations.append(combo[:index] + '*' + combo[index + 1:])
            families += [combo for combo in combinations if '*' in combo]

    return families


def find_prime_families(starting_number, ending_number):
    # I'm doing this recursively because I have _no_ clue how big the winner will be
    if ending_number > 10000:
        primes = list_big_primes(ending_number)
    else:
        primes = list_primes(ending_number)

    for start_value, prime in enumerate(primes):
        if prime > starting_number:
            break
    else:
        start_value = 0

    prime = 2  # in case we mess up our first iteration and make stuff too small, this makes the
    # recursive section able to do work for us.
    for prime in primes[start_value:]:
        families = generate_families(prime)

        for instance in families:
            list_of_primes_in_family = prime_families.get(instance, list())
            list_of_primes_in_family.append(prime)
            prime_families[instance] = list_of_primes_in_family

            # check for exit conditions
            size_of_this_family = len(list_of_primes_in_family)
            if size_of_this_family == goal:
                print(instance, list_of_primes_in_family[0])
                exit()

    find_prime_families(prime, 10 * ending_number)


find_prime_families(0, 100000)
# nice, that wasn't too slow!
