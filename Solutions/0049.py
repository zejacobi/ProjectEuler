"""
# Problem 49: Prime Permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways:
    (i) each of the three terms are prime, and,
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this
property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

# OOOOH I REALLY LIKE THIS. I think I will decompose primes into component numbers and see which
# ones have three+.

from Lib.Helpers import list_primes

primes = [prime for prime in list_primes(10000) if prime >= 1000]


prime_mapping = {}

for prime in primes:
    numbers = ''.join(sorted(i for i in str(prime)))

    if prime_mapping.get(numbers, None):
        prime_mapping[numbers].append(prime)
    else:
        prime_mapping[numbers] = [prime]


# need to check all numbers in the mapping against all others. Luckily at this point, n << 9000
def check_all_members(prime_array):
    differences = {}
    for pointer, first_prime in enumerate(prime_array):
        for second_prime in prime_array[(pointer + 1):]:
            diff = second_prime - first_prime
            list_diffs = differences.get(diff, [first_prime, second_prime])
            if first_prime not in list_diffs:
                list_diffs.append(first_prime)
            if second_prime not in list_diffs:
                list_diffs.append(second_prime)
            differences[diff] = list_diffs

    return [differences[diff] for diff in differences.keys() if len(differences[diff]) == 3]


# only run the check_all_numbers function when there's at least 3 primes with a set of numbers
# otherwise it's just a waste of cycles
candidates = [check_all_members(prime_mapping[candidate]) for candidate in prime_mapping.keys()
              if len(prime_mapping[candidate]) >= 3]

# 3 nested joins in triple nested list comprehension is readable, right?
print(', '.join([', '.join([''.join([str(s) for s in seq]) for seq in final])
                 for final in candidates if len(final)]))
# I wouldn't do this in production code, but it was too fun to pass up.
