"""
# PROBLEM 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime
is 13.

What is the 10,001st prime number?
"""

# Well, the Wikipedia article on the segmented Sieve of Eratosthenes is pretty unclear,
# so I guess I just have to take my best shot at it...

primes = [2]
bits = [0, 0, 1]
max_val = 2
first_new_prime = 2

while len(primes) < 10001:
    start_val = max_val + 1
    max_val = primes[-1] ** 2
    bits += [1 for _ in range(start_val, max_val + 1)]
    for prime in primes:
        if first_new_prime < prime:  # necessary for all primes after the first new prime
            index = prime ** 2
        else:  # most efficient for all primes *before* the first prime we found last time
            index = prime * first_new_prime
        while index <= max_val:
            bits[index] = 0
            index += prime
    new_primes = [index + start_val for index, bit in enumerate(bits[start_val:]) if bit]
    first_new_prime = new_primes[0]
    primes += new_primes

print(primes[10000])

# So this seems to work pretty well. It's a bit on the slow side, probably because it ends
# up finding may more primes than necessary. I don't quite know how to stop that, because
# it's not like we know ahead of time how big the 10001th prime number is (although knowing
# math, maybe there's a formula that puts an upper bound on it?).

# The whole point of this code is to slowly build the sieve up, without ever having to
# iterate over the same bits twice. I think I've accomplished that, so I'm happy with this.
