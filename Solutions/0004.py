"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# I had a feeling that palindromic numbers needed at least one palindromic factor
# But that isn't true. 26 * 26 gives 676, but 26 is not a palindrome.
# Given that, all I see to do here is search exhaustively.
# Although I can slightly speed this up by avoiding duplicates


palindromes = []
for i in range(100, 1000):
    for j in range(i, 1000):
        num = i * j
        str_num = str(num)
        for idx in range(len(str_num) // 2 + 1):
            if not str_num[idx] == str_num[-idx - 1]:
                break
        else:
            palindromes.append(num)

print(sorted(palindromes)[-1])


# Although actually, it would probably be quicker if we went the other way and broke once
# we found one. Does this give the same answer?

palindrome = None
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        num = i * j
        str_num = str(num)
        for idx in range(len(str_num) // 2 + 1):
            if not str_num[idx] == str_num[-idx - 1]:
                break
        else:
            palindrome = num
            break
    if palindrome:
        break

print(palindrome)

# No, it doesn't because we end up with a pretty high first number, but a fairly low second.
# Maybe instead we try things in 100 number tranches?


def find_palindrome(highest, lowest):
    palindrome = None
    for i in range(highest, lowest, -1):
        for j in range(i, lowest, -1):
            num = i * j
            str_num = str(num)
            for idx in range(len(str_num) // 2 + 1):
                if not str_num[idx] == str_num[-idx - 1]:
                    break
            else:
                palindrome = num
                break
        if palindrome:
            break
    else:
        return find_palindrome(highest - 100, lowest - 100)
    return palindrome


print(find_palindrome(999, 899))

# This works, but I'm not sure I can prove that it will always work.
# In fact, it isn't exhaustive at all! It will miss much of the solution space.
