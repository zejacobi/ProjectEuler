"""
# Problem 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
from math import log10

# Okay, so the Fibonacci sequence converges to the golden ratio. Can I take advantage of this fact
# and use logs to troll this? Like F^N >= 10 ^ 1000, which implies that N * log_10 (F) >= 1000
# At the very least, this will let me know the neighbourhood, right?

# Rearranging tells me that N >= 1000 / log_10(F)

# Let's quickly calculate F and the bound on N

old = 1
new = 1

while new < 100000:
    temp = new
    new = old + new
    old = temp

print(1000 / log10(new / old))

# That's not the answer, but it does tell me that things shouldn't be prohibitively large

# (I could probably get the answer by guessing around that number, but that feels outside the
# spirit of project Euler)