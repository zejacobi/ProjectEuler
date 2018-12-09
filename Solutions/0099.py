"""
# Problem 99

Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator
would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult,
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one
thousand lines with a base/exponent pair on each line, determine which line number has the greatest
numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""

from math import log

# we're going to try doing this with exponentials. If that's slow, we'll take logs first, to make
# the numbers smaller

with open('./Files/p099_base_exp.txt', 'r') as exp_file:
    lines = [[int(i) for i in l.strip().split(',')] for l in exp_file.readlines()]

# yep, it was too slow

numbers = [b_e[1] * log(b_e[0]) for b_e in lines]

best = 0
line = None

for i, n in enumerate(numbers):
    print(n)
    if n > best:
        best = n
        line = i

print(line + 1)