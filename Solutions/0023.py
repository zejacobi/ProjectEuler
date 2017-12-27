"""
# PROBLEM 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as the sum of two abundant
numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from math import ceil, sqrt

# our earlier summing function (from 21) will come in handy with minor tweaks


def type_num(n):
    factors = [1]
    upper_bound = int(ceil(sqrt(n + 1)))  # huh, this +1 was important!
    for i in range(2, upper_bound):
        if not n % i:
            factors.append(i)
            factors.append(int(n / i))
    num_sum = sum(list(set(factors)))
    if num_sum == n:
        return 'p'
    elif num_sum > n:
        return 'a'
    else:
        return 'd'


abundant_numbers = [n for n in range(1, 28124) if type_num(n) == 'a']
numbers_from_abundant = []

for index, num in enumerate(abundant_numbers):
    for num2 in abundant_numbers[index:]:
        if (num2 + num) < 28124:
            numbers_from_abundant.append(num + num2)

numbers_from_abundant = list(set(numbers_from_abundant))

non_abundant_sum = 0
for i in range(1, 28124):
    if i not in numbers_from_abundant:
        non_abundant_sum += i

print(non_abundant_sum)
exit()

# OLD attempt, takes like 25 minutes to run (optimizations shave off ~8 minutes)
# ugh this double loop is gonna be ugly, but the optimizations should help
remainder = []
for i in range(1, 28124):
    if i % 250 == 0:
        print(i)
    for index, n in enumerate(abundant_numbers):
        if 2 * n > i:
            remainder.append(i)
            break
        elif (i - n) in abundant_numbers[index:]:
            break
    else:
        remainder.append(i)

print(len(remainder))
print(sum(remainder))
