"""
# PROBLEM 27

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40, 40^2+40+41=40(40+1)+41n=40, is divisible by 41, and certainly when n=41,
41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive
values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the
maximum number of primes for consecutive values of n, starting with n=0.
"""

# This search space is much smaller than I initially thought, because we're starting with n=0,
# which means that b must always be prime.


def sieve(limit):
    bits = [0] + [1 for _ in range(limit)]  # we filter out 0
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

    return primes


# gives values for b
primes_up_to_1000 = sieve(1001)

# quick check for n=1 case
first_pass_primes = sieve(primes_up_to_1000[-1] + 2 + 1000)

# quick-ish check for the n <= 10 case
under_10_primes = sieve(primes_up_to_1000[-1] + 1000 * 10 + 10 * 10 + 1)

# our true list of primes; we'll recalculate this if we ever over-run it
all_relevant_primes = sieve(primes_up_to_1000[-1] + 1000 * 1000 + 1000 * 1000 + 1)


# splitting these up like this should really speed up my list access, especially if it's rare to go
# above 1, above 10, or above my max.

max_count = 0
best = [None, None]
for a in range(-1000,1000):
    for b in primes_up_to_1000:
        count = 0
        if (1 + a + b) in first_pass_primes:
            n = 1
            while True:
                n += 1
                product = n * n + n * a + b
                if n < 10:
                    if product not in under_10_primes:
                        break
                    else:
                        count += 1
                else:
                    if product > all_relevant_primes[-1]:
                        all_relevant_primes = sieve(product * 10)
                    if product not in all_relevant_primes:
                        break
                    else:
                        count += 1
        if count > max_count:
            print(count)
            max_count = count
            best = [a, b]

print(best[0] * best[1])
