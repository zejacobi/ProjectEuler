"""
### Problem 45: Triangle, pentagonal, and hexagonal  numbers

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle		T_n=n(n+1)/2	1, 3, 6, 10, 15, ...
Pentagonal		P_n=n(3n−1)/2	1, 5, 12, 22, 35, ...
Hexagonal		H_n=n(2n−1)		1, 6, 15, 28, 45, ...
It can be verified that T_285 = P_165 = H_143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""


def generate_triangular(n):
    return n * (n + 1) / 2


def generate_pentagonal(n):
    return n * (3 * n - 1) / 2


def generate_hexagonal(n):
    return n * (2 * n - 1)


triangular_n = 286
triangular_number = generate_triangular(triangular_n)

pentagonal_n = 166
pentagonal_numbers = [generate_pentagonal(pentagonal_n)]

hexagonal_n = 144
hexagonal_numbers = [generate_hexagonal(hexagonal_n)]

while triangular_number not in pentagonal_numbers or triangular_number not in hexagonal_numbers:
    triangular_n += 1
    triangular_number = generate_triangular(triangular_n)

    while hexagonal_numbers[-1] < triangular_number:
        hexagonal_n += 1
        hexagonal_numbers.append(generate_hexagonal(hexagonal_n))

    while pentagonal_numbers[-1] < triangular_number:
        pentagonal_n += 1
        pentagonal_numbers.append(generate_pentagonal(pentagonal_n))


print(triangular_number)