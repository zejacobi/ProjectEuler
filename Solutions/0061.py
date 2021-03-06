"""
# Problem 61: Cyclical figurate numbers
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate
(polygonal) numbers and are generated by the following formulae:


Triangle	P_(3,n) = n(n+1)/2		1, 3, 6, 10, 15, ...
Square		P_(4,n) = n^2			1, 4, 9, 16, 25, ...
Pentagonal	P_(5,n) = n(3n−1)/2		1, 5, 12, 22, 35, ...
Hexagonal	P_(6,n) = n(2n−1)		1, 6, 15, 28, 45, ...
Heptagonal	P_(7,n) = n(5n−3)/2		1, 7, 18, 34, 55, ...
Octagonal	P_(8,n) = n(3n−2)		1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

    1. The set is cyclic, in that the last two digits of each number is the first two digits of the
       next number (including the last number with the first).
    2. Each polygonal type: triangle (P_(3,127)=8128), square (P_(4,91)=8281),
       and pentagonal (P_(5,44)=2882), is represented by a different number in the set.
    3. This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type:
triangle, square, pentagonal, hexagonal, heptagonal, and octagonal,
is represented by a different number in the set.
"""


formula_types = ['triangle', 'square', 'pentagonal', 'hexagonal', 'heptagonal', 'octagonal']


def triangle(x):
    return x * (x + 1) / 2


def square(x):
    return x ** 2


def pentagonal(x):
    return x * (3 * x - 1) / 2


def hexagonal(x):
    return x * (2 * x - 1)


def heptagonal(x):
    return x * (5 * x - 3) / 2


def octagonal(x):
    return x * (3 * x - 2)


# what, how is this legal?
formulas = {formula_name: globals()[formula_name] for formula_name in formula_types}
four_digit_numbers = {}


for formula_type in formula_types:
    four_digit_numbers[formula_type] = []
    n = 1
    value = int(formulas[formula_type](n))
    val_len = len(str(value))
    while val_len <= 4:
        if val_len == 4:
            four_digit_numbers[formula_type].append(value)
        n += 1
        value = int(formulas[formula_type](n))
        val_len = len(str(value))

first_parts = []
back_parts = []

for formula_type in formula_types:
    for number in four_digit_numbers[formula_type]:
        str_num = str(number)
        first_parts.append(str_num[0:2])
        back_parts.append(str_num[2:])

first_parts = list(set(first_parts))
back_parts = list(set(back_parts))

useful_numbers = {}

for formula_type in formula_types:
    useful_numbers[formula_type] = []
    for number in four_digit_numbers[formula_type]:
        str_num = str(number)
        first_part = str_num[0:2]
        back_part = str_num[2:]
        if first_part in back_parts and back_part in first_parts:
            useful_numbers[formula_type].append(str_num)
            # str version of number is easier to work with


potential_sequences = useful_numbers[formula_types[0]]

for formula_type in formula_types[1:]:
    surviving_sequences = []
    for str_num in useful_numbers[formula_type]:
        for seq in potential_sequences:
            if str_num[0:2] == seq[-2:]:
                surviving_sequences.append(seq + str_num)
            if str_num[2:] == seq[0:2]:
                surviving_sequences.append(str_num + seq)
    potential_sequences = surviving_sequences


only_seq = [seq for seq in potential_sequences if seq[0:2] == seq[-2:]][0]

seq_numbers = []
for i in range(0, len(only_seq), 4):
    seq_numbers.append(int(only_seq[i:i+4]))

print(sum(seq_numbers))