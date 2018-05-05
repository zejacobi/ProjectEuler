"""
PROBLEM 43: Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits
0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:

d_2d_3d_4=406 is divisible by 2
d_3d_4d_5=063 is divisible by 3
d_4d_5d_6=635 is divisible by 5
d_5d_6d_7=357 is divisible by 7
d_6d_7d_8=572 is divisible by 11
d_7d_8d_9=728 is divisible by 13
d_8d_9d_10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

# I'm going to assume that by "this property" they mean "divisible by these specific numbers", not
# THE MANY OTHER SEQUENCES THAT COULD ALSO FIT THAT RULE, LIKE, IDK, DIVISIBLE BY ASCENDING PRIMES?

# I'm going to do this backwards, then reverse. Because that should slow down our explosion of
# places to search

str_numbers = [str(i) for i in range(10)]


initial_list = []

for num in range(1000):
    if num % 17 == 0:
        num_str = str(num)
        while len(num_str) < 3:
            num_str = '0' + num_str
        for test_number in str_numbers:
            if num_str.count(test_number) > 1:
                break
        else:
            initial_list.append(num_str)

kept_list = []

for factor_num, factor in enumerate([13, 11, 7, 5, 3, 2]):
    for number in initial_list:
        for added_number in str_numbers:
            if added_number in number:
                continue
            new_str_num = added_number + number
            # my gosh it took me forever to get these indexes right
            test_num = int(new_str_num[-4 - factor_num:-1 - factor_num])
            if test_num % factor == 0:
                kept_list.append(new_str_num)
    initial_list = kept_list
    kept_list = []

final_list = []
for number in initial_list:
    for added_number in str_numbers:
        if added_number not in number:
            final_list.append(int(added_number + number))

print(sum(final_list))
