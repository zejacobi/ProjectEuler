"""
# Problem 62
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3).

In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which
are also cube.

Find the smallest cube for which exactly five permutations of its digits are a cube.
"""


# Okay so obviously checking each permutation is a TERRIBLE idea.

# Instead we:
# 1) Find all cubes of a give number of digits
# 2) As we're finding them, split them up into sorted lists of digits
# 3) Compare these with a dictionary to keep track
# 4) Break when we hit 5, printing smallest number

n_digits = 0
number = 1

while True:
    n_digits += 1
    numbers_this_size = []
    canonical_representations = {}

    cubed_number = str(number ** 3)

    while len(cubed_number) <= n_digits:
        canonical_representation = ''.join(sorted([i for i in cubed_number]))
        list_of_others = canonical_representations.get(canonical_representation, [])
        list_of_others.append(cubed_number)

        if len(list_of_others) == 5:
            print(sorted(int(i) for i in list_of_others)[0])
            exit(0)

        canonical_representations[canonical_representation] = list_of_others

        number += 1
        cubed_number = str(number ** 3)

