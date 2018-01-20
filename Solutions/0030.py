"""
# PROBLEM 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their
digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


# Okay, so this is a very mathy problem. But presumable the sums blow up so quickly that it
# becomes okay; that is to say, there's a point (a number of digits) where it becomes clear
# that you're just always going to overshoot (or, if you're just doing 1s and 2s, undershoot).


# Now watch as I try something simple
results = []


def check_numbers(current_number, current_sum, remaining_calls):
    if remaining_calls:
        for i in range(10):
            additional = i ** 5
            new_number = current_number + str(i)
            new_sum = current_sum + additional
            if int(new_number) == new_sum:
                results.append(new_number)
            check_numbers(new_number, new_sum, remaining_calls - 1)


check_numbers('', 0, 7)  # empirically, 7 gives no more results than 6, so let's count this as good?

results = list(set([int(i) for i in results if int(i) > 1]))

print(sum(results))


# I think there's a much smart solution to this problem involving heuristics (e.g. you're currently
# at a certain number of digits in both your sum and your products, which numbers can you add that
# will even give you the same order of magnitude) but this seems very complicated and my intuition
# was that we were only really going to be a few orders of magnitude higher than the ^4 case, which
# is very brute forceable on modern hardware
