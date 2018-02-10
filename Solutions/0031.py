"""
# PROBLEM 31

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

# So I checked and in Python, [1, 2, 3] == [1, 2, 3], [1, 2, 3] in [[1, 2, 3]] == True, etc.

# It's also true that sorted([1, 2, 3]) == sorted([3, 2, 1]), but I figure I'll save sorting
# overhead if I instead use an 8 element array (e.g. [1, 0, 0, 0, 0, 0, 0, 0] is one pence)

goal = 200

values_to_index = {
    1: 0,
    2: 1,
    5: 2,
    10: 3,
    20: 4,
    50: 5,
    100: 6,
    200: 7
}

coin_values = sorted(list(values_to_index.keys()))  # the fact that keys is its own thing probably
# was fine, but I don't want any nasty surprises!

index_to_value = {values_to_index[value]: value for value in coin_values}

# Okay so the first thing we'll realize is that there is a certain allowable set of values for each
# coin; there are twenty one for one pence pieces and one for two pound pieces.

# (therefore I'm ignoring two pound pieces entirely and adding one the final result and I'll deal
# with single pence right at the start, allowing me to ignore them)

coin_values = coin_values[1:-1]  # okay, so making this a list did come in useful
# (I promise I wrote the above comment 1st)

starting_arrays = [[[pence, 0, 0, 0, 0, 0, 0, 0], pence, 0] for pence in range(0, goal, 1)]
# packing these together lets me unpack them later

# the two easy cases, namely 1 200p coin and 200 1p coins, should be handled separately
final_arrays = [[0, 0, 0, 0, 0, 0, 0, 1], [goal, 0, 0, 0, 0, 0, 0, 0]]


def build_arrays(current, value, position):
    if position > len(coin_values):
        return
    for current_position, pence in enumerate(coin_values[position:]):
        max_pieces = int((goal - value) / pence) + 1
        for n in range(1, max_pieces):
            if (value + pence * n) < goal:
                new_array = current[:]
                new_array[values_to_index[pence]] += n
                build_arrays(new_array, value + pence * n, position + 1 + current_position)
                # the +current_position turned out to be really key in making this run quickly
                # seriously, it cuts down the run time 100-fold
            elif (value + pence * n) == goal:
                final = current[:]
                final[values_to_index[pence]] += n
                if final not in final_arrays:
                    final_arrays.append(final)


for array in starting_arrays[:]:
    build_arrays(*array)

print(len(final_arrays))
