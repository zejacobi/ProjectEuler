"""
# Problem 40: Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...
             |
It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""

# quick guessing has confirmed that the answer here is neither 1 nor zero, so that's unfortunate

# okay, so obviously there's a quick answer. It just requires concatenating 10s-100s of thousands of
# strings, then indexing it. I don't like that solution.

