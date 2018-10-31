"""
# Problem 63 Powerful digit counts
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9,
is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

from math import log10

# Well, we know that 10^(n-1) <= x^n < 10^n
# n-1 <= log(x^n) < n
# n-1 <= n * log(x) < n
# (n-1)/n <= log(x) < 1

# So we only care about bases between 1 and 9 inclusive.
# Also, there should be a point where we get to too high of n.

fit_this_pattern = []

for base in range(1, 10):
    n = 1
    while ((n - 1) / n) <= log10(base):
        test = base ** n
        if len(str(test)) == n:
            fit_this_pattern.append(test)
        n += 1

print(len(set(fit_this_pattern)))

# NOW YOU'RE THINKING WITH LOGARITHMS

# Ok but seriously I love this problem.