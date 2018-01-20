"""
# PROBLEM 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is
formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""

# There's a predictable pattern in the perimeter


def get_perimeter(n):
    return 4 * (n - 1)  # simplified for of 4 * n - 4


# But what's best is if we can get the perimeter for arbitrary layer
def get_perimeter_for_layer(layer):
    layer_size = 2 * layer + 1
    return get_perimeter(layer_size), layer_size


# I feel like the problem isn't hard, it's just begging for 1001 compounded off by one errors :'(
# Let's make sure I can get the right answer in a trivial case? (i.e. one I already know the
# answer to)

def calculate_diagonal_sum(max_layer_size):
    layer = 0
    _, layer_size = get_perimeter_for_layer(layer)
    place = 1
    diagonals = [place]
    while layer_size < max_layer_size:
        layer += 1
        perimeter, layer_size = get_perimeter_for_layer(layer)
        diagonal_positions = [perimeter/4, perimeter/2, 3 * perimeter / 4, perimeter]
        for position, number in enumerate(range(place + 1, place + 1 + perimeter)):
            if position + 1 in diagonal_positions:
                diagonals.append(number)
        place = number  # despite what my IDE thinks, number isn't scoped to the loop!

    return sum(diagonals)


print(calculate_diagonal_sum(3))  # 25
print(calculate_diagonal_sum(5))  # 101!
print('Final:', calculate_diagonal_sum(1001))
