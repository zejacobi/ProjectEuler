"""
# Problem 58: Spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side
length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal,
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime;
that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9
will be formed. If this process is continued, what is the side length of the square spiral for
which the ratio of primes along both diagonals first falls below 10%?
"""

# Didn't I do something like this before?

# Yep, 28. And even though that spirals clockwise and this spirals anti-clockwise, the diagonals
# are the same, so I can totally re-use my code. (I'm copy pasting because properly re-using is
# hard when your modules have names that are numbers...

from Lib.Helpers import list_big_primes, efficient_is_prime


def get_perimeter(n):
    return 4 * (n - 1)  # simplified for of 4 * n - 4


# But what's best is if we can get the perimeter for arbitrary layer
def get_perimeter_for_layer(layer):
    layer_size = 2 * layer + 1
    return get_perimeter(layer_size), layer_size


primes_up_to = 1000000
prime_list = list_big_primes(primes_up_to)  # should be safe?

total_diagonal = 1
prime_diagonal = 0

layer = 0
place = 1

while prime_diagonal == 0 or (prime_diagonal / total_diagonal) > 0.1:
    layer += 1
    perimeter, layer_size = get_perimeter_for_layer(layer)
    diagonal_positions = [perimeter/4, perimeter/2, 3 * perimeter / 4, perimeter]
    diagonal_numbers = [place + pos for pos in diagonal_positions]
    for number in diagonal_numbers:
        total_diagonal += 1
        prime_diagonal += efficient_is_prime(number, primes_up_to, prime_list)

    # for position, number in enumerate(range(place + 1, place + 1 + perimeter)):
    #     if position + 1 in diagonal_positions:
    #         total_diagonal += 1
    #         prime_diagonal += efficient_is_prime(number, primes_up_to, prime_list)

    print('Layer', layer, 'Prime', prime_diagonal, 'Total', total_diagonal)
    place = number  # despite what my IDE thinks, number isn't scoped to the loop!

print(2 * layer + 1)
