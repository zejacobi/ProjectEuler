"""
# PROBLEM 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""
from copy import deepcopy

# print(factorial(10))

# 3,628,800 permutations and 3.3 GHz chip suggests brute force isn't too bad
# Also, this seems like a task for recursion!

# Wait also my RAM should be fine? Yes, because 36,288,000 characters isn't bad vs. 16 GB

all_permutations = []


def generate_arrangement(current, remaining):
    if len(remaining) == 0:
        all_permutations.append(current)
    else:
        for index, item in enumerate(remaining):
            new_remaining = deepcopy(remaining)
            del new_remaining[index]
            generate_arrangement(current + item, new_remaining)


digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

generate_arrangement('', digits)
print(sorted(all_permutations)[999999])

exit()

# This is kind of a stupid solution, because it does 2,628,800 more calculations than it needs to
# A smarter solution would look very similar, but I'd just do the first few starting numbers (e.g.
# 0, 1, 2), then stop.

# Honestly, you could do that with this code, like this:

generate_arrangement('0', ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
generate_arrangement('1', ['0', '2', '3', '4', '5', '6', '7', '8', '9'])
generate_arrangement('2', ['0', '1', '3', '4', '5', '6', '7', '8', '9'])
print(sorted(all_permutations)[999999])

# And I'm sure a bit of cleverness would let me skip the sort step.

