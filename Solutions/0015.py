"""
# PROBLEM 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

__      _       _
  |      |_      |      |__     |_      |
  |        |     |_        |      |_    |__
How many such routes are there through a 20×20 grid?
"""

# Okay, so is this, or isn't this isomorphic to "how many ways can we arrange n horizontal and
# n vertical one unit lines, constrained such that they start in the top left, end in the top right
# and each segment leads to another?

# And is, or isn't the answer to that n choose 2? 4 choose 2 = 4!/(2 * (4 - 2)!) = 4 * 3 / 2 = 6

# Ah, n choose 2 seems to be a red herring.

# It also isn't (n-1)(n-2)

# The probability space is probably too big to do a random search.

# 400 choose 40 isn't feasible

# AHH. We're actually looking for the number of unique strings we can make out of twenty instances
# of the letter R and twenty of the letter D

# By analogy to the 2x2 grid, we want to find the number of ways to arrange two strings D and two
# strings R
# RRDD RDRD RDDR DRRD DRDR DDRR

# For 3x3 (6 characters) it is:
# 12 of the case XY____ (because there are exactly 6 ways ____ can be written)
# 8 of the case XX____ (because there are only 4 spots the last X can go)

# For 4x4 (8 characters) it is:
# 20 of the case RD______
# 20 of the case DR______
# 6 of the case DD____RR
# 6 of the case RR____DD
# 4 of the case DD____DR
# 4 of the case DD____RD
# 4 of the case RR____RD
# 4 of the case RR____DR
# 1 of the case RRDDDDRR
# 1 of the case DDRRRRDD

# ARGGHH, the formula I want is (2 * n)! / (n!)^2

import math

print(math.factorial(40)/(math.factorial(20)**2))
