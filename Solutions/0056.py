"""
# Problem 56: Powerful digit sum
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost
unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in
each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""

# Well, this is one of those actually pretty simple problems. 8910 possible options if we remove
# the obviously bad ones.

disallow_a_values = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a_values = [i for i in range(1, 100) if i not in disallow_a_values]
b_values = range(2, 100)

max_sum = 0

for a in a_values:
    for b in b_values:
        # THE ASSIGNMENT EQUAL OPERATOR CAN'T HAPPEN SOON ENOUGH
        digit_sum = sum([int(digit) for digit in str(a ** b)])
        if digit_sum > max_sum:
            max_sum = digit_sum

print(max_sum)
