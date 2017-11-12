"""
#PROBLEM 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the
square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and
 the square of the sum.
"""

# The first question is: can Python calculate the square of the sum of the first 100 natural
# numbers?

print('Testing: ', sum(range(1, 101))**2)

# Okay, I feel kind of silly now. I should have remembered that the sum was 5050 and obviously
# the square of this isn't going to overflow Python's int class (which further research shows
# is actually of arbitrary precision).
# See: http://mortada.net/can-integer-operations-overflow-in-python.html

# At this point, answering is trivial:
print('Answer: ', sum(range(1, 101))**2 - sum((i ** 2 for i in range(1, 101))))


# But what if I couldn't have done this all at once? Is there a clever way I could have
# done it inline? (a + b)^2 - a^2 - b^2 = a^2 - a^2 + 2ab - b^2 + b^2

# (a + b + c) ^ 2 - a^2 - b^2 - c^2 = 2ab + 2ab + 2bc

# And it actually generalizes, I think. Namely (\sigma(i, 1, N)(i))^2 - \sigma(i, 1, N)(i^2)
# should equal \sigma(i, 1, N)(2 * i * j for all j > i)

print('Alertnative Calculation:',
      sum((sum((2 * i * j for j in range(i+1, 101))) for i in range(1, 101))))
