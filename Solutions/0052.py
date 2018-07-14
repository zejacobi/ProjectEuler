"""
Problem 52: Permuted Multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

# I hate unbounded problems. This one doesn't even let me do a cool estimate like in 25.

# Let's assume that we can only use each digit 1:1. So this saves us some effort, because at each
# order of magnitude, we only want to look at things that are 1/6 of the next order of magnitude.

# So we check 1, find it doesn't work, then check 10-16, find none of them work, then check 100-166,
# etc.

# This cuts down our work by 6-fold.

# As usual, I wonder what the optimal way to figure out if a thing has the same digits as another
# in Python. Comparing 3 dictionaries is (3)N. Comparing two sorted lists is 2Nlog(N). I guess if
# log(N) is expected to be greater than 1.5, the dictionaries might be faster? But then again, sort
# is probably heavily optimized and anything I do probably won't be. Let's sort.

from math import ceil

def return_true_if_same_digits(a, b):
    a = sorted([int(digit) for digit in str(a)])
    b = sorted([int(digit) for digit in str(b)])
    return a == b


order = 10

while True:
    order *= 10
    max_num = int(ceil(order * 10 / 6))

    for i in range(order, max_num):
        for multiple in range(2, 7):
            if not return_true_if_same_digits(i, i * multiple):
                break
        else:
            print(i)
            exit()

# Oh lol it's awkward that I actually could have thought about this for two seconds and given the
# answer off the top of my head. Sigh.
