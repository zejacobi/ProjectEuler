"""
# Problem 48: Self powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

# I'm lazy.

print(str(sum([i ** i for i in range(1, 1001)]))[-10:])

