"""
# PROBLEM 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although
it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# This is my favourite question so far. Because there's an obvious (and beautiful) optimization!

precomputed = {0: 0, 1: 1}  # initialize this with steps for 0 and 1

biggest = 1
biggest_steps = 1


def do_collatz(num, others):
    if precomputed.get(num, None):
        return precomputed[num]

    others.append(num)

    if num % 2:
        return do_collatz(num * 3 + 1, others) + 1
    else:
        return do_collatz(num / 2, others) + 1


for starting_num in range(2, 10**6):
    other_nums = []

    # Easy mode is just saving single numbers when you have their step number. Hard mode is saving
    # every single number you see. Obviously I'm going to do hard mode.

    steps = do_collatz(starting_num, other_nums)

    for count, other in enumerate(other_nums):
        precomputed[int(other)] = steps - count

    if steps > biggest_steps:
        biggest = starting_num
        biggest_steps = steps

print(biggest)

