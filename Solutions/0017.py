"""
# PROBLEM 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23
letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out
numbers is in compliance with British usage.
"""

letters = {
    0: 4,
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
}


def recursive_count(number):
    if number == 0:
        return 0
    elif number > 99:
        first_number = int(str(number)[0])
        return letters[first_number] + recursive_count(number - first_number * 100) + (
            10 if number % 100 else 7)
    elif number > 20:
        first_number = int(str(number)[0])
        return letters[first_number * 10] + recursive_count(number - first_number * 10)
    else:
        return letters[number]


count = 11  # start with one thousand, which is outside our range
for i in range(1, 1000):
    count += recursive_count(i)

print(count)
