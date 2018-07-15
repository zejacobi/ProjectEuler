"""
# Problem 53:

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, ^5C_3 = 10.

In general,

^nC_r = n!/(r!(n−r)!),where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: ^23C_10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
"""

# In my head, I hear the voice of my statistical thermodynamics professor yelling about how I
# could probably solve this with logs.

# It is generally known that log(n!) ~= nlog(n) - n, especially for large n.
# (Striling's approximation)

# Luckily, all those last terms cancel out. If we use Stirling's approximation here, we find that
# nlog(n) - rlog(r) - (n - r)log(n - r) . 6. This makes use of log rules and Stirling's
# approximation and only uses base 10 logs. With the additional constraint of r < n (well, it
# technically could be greater, but if r = n, then the expression is unity), this would be
# relatively simple to solve graphically for a good estimate. But I don't see any benefit to that
# here, so I may as well just solve it with brute force and ignorance? Like we have 100 values
# of n, 99 values of r. 9900 at most. It's just going to be really fast.

# Now using logs would give us a good approximation and probably be faster, because e.g. 33!
# requires 33 calculations and there's probably a good log lookup table somewhere on my computer
# for small integers. But still, I'd probably be off by like 5 and then Euler wouldn't be happy.

from math import factorial, log10


def number_combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


count = 0
for i in range(2, 101):
    for j in range(1, i):
        count += (number_combinations(i, j) > 1000000)

print("The solution is:", count)


# Okay, for my curiousity, did I Stirling right with my equation above?

def log_number_combinations(n, r):
    return n * log10(n) - r * log10(r) - (n - r) * log10(n - r)


log_count = 0
for i in range(2, 101):
    for j in range(1, i):
        log_count += (log_number_combinations(i, j) > 6)

print("This can also be approximately solved with a Stirling's Approximation, which gives:",
      log_count)

# Yep, it gives 4189, which is accurate to 2.8%, but obviously not going to work for Project Euler.
# I am glad I remembered how to do it.
