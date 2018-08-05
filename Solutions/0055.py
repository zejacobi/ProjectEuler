"""
# Problem 53: Lychrel numbers
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a
palindrome. A number that never forms a palindrome through the reverse and add process is called a
Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this
problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are
given that for every number below ten-thousand, it will either (i) become a palindrome in less
than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed
so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require
over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations,
28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of
Lychrel numbers.
"""

# This is actually pretty similar to my beloved problem 14; if we save all numbers that lead to
# palindromes and all that don't, then we should speed up the answer.

# Actually huh no I tried and they slow it down considerably. I've commended those blocks out, but
# you're welcome to prove it to yourself if you're interested.

# oh look, some kind soul gave us a function that tells us if a number is a palindrome. Isn't past
# me great?

from Lib.Helpers import is_palindrome
#
# dont_lead_to_palindrome = []
# do_lead_to_palindrome = []

n_lycherel = 0

for number in range(1, 10000):
    attempts = []
    #
    # if number in do_lead_to_palindrome:
    #     n_lycherel += 1
    #     continue
    # elif number in dont_lead_to_palindrome:
    #     continue

    for _ in range(50):
        new_number = number + int(str(number)[::-1])
        attempts.append(new_number)
        if is_palindrome(new_number):
            # do_lead_to_palindrome += attempts[0:-1]
            # ^ we don't know if the last one "leads" to palindrome, just that it is
            break
        number = new_number
    else:
        n_lycherel += 1
        # dont_lead_to_palindrome += attempts
print(n_lycherel)
