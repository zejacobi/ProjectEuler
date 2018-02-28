"""
# PROBLEM 36: Double Based Palindromes

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from Lib.Helpers import is_palindrome

# I'm not sure if 1-9 will count, so I'm going to do them separately.

ambiguous = sum([i for i in range(1, 10) if is_palindrome(str(bin(i)).split('b')[-1])])

palindromes = [i for i in range(10, 1000001) if is_palindrome(i)]

palindromes = [i for i in palindromes if is_palindrome(str(bin(i)).split('b')[-1])]

palindromes_sum = sum(palindromes)

print('Sum without ambiguous numbers:', palindromes_sum)
print('Sum with ambiguous numbers:', palindromes_sum + ambiguous)

# Turned out numbers below ten do count!
