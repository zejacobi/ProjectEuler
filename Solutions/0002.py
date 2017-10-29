"""
# PROBLEM 2
Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, f
ind the sum of the even-valued terms.
"""

# Hmmm. It looks like Fibonacci goes odd, odd, even, ood, ood, even, etc.

final_sum = 0
current = 1
past = 1
index = 2  # If I index from 0, the math won't work as elegantly

while current < 4000000:
    index += 1
    temp = current
    current += past
    past = temp

    if not index % 3:  # We've set things up so that every third item is even.
        final_sum += current

print(final_sum)