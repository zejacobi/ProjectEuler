"""
# PROBLEM 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math
limit = 2000000
# You know what's great? We already know how to create a sieve of Eratosthenes!

highest = math.floor(math.sqrt(limit))
# We only have to try numbers up to the square root of our target, if I remember correctly from my
# reading.

bits = [0] + [1 for i in range(limit)]  # we filter out 0
bits[1] = 0  # and also one.
primes = []

for num, prime in enumerate(bits):
    if not prime:
        continue
    primes.append(num)
    index = num ** 2
    while index <= limit:
        bits[index] = 0
        index += num

print(sum(primes))
