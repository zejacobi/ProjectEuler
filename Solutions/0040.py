"""
# Problem 40: Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...
             |
It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""

# quick guessing has confirmed that the answer here is neither 1 nor zero, so that's unfortunate

# okay, so obviously there's a quick answer. It just requires concatenating 10s-100s of thousands of
# strings, then indexing it. I don't like that solution.

product = 1

breakpoints = []
breakpoint_values = []
current = 1
num_digs = [1]
max_num = 1000000

while current <= max_num*10:
    breakpoint_values.append(current)
    current += 9 * num_digs[-1] * (10 ** len(breakpoints))
    breakpoints.append(10 ** len(breakpoints))
    num_digs.append(num_digs[-1] + 1)

positions_of_interest = [1, 10, 100, 1000, 10000, 100000, 1000000]

for num in positions_of_interest:
    for ix, value in enumerate(breakpoint_values):
        if value > num:
            last_num = breakpoints[ix-1]  # the last number we know in the sequence
            last_pos = breakpoint_values[ix-1]  # the position in the sequence that number was at
            number_digits = num_digs[ix-1]  # the number of digits of every number after that one
            to_traverse = num - last_pos  # the difference between the last known number in
                                          # the sequence and the one we care about
            position_in_number = to_traverse % number_digits  # which digit in the next number to take
            sequence_number = to_traverse//number_digits + last_num  # the number in the sequence
                                                                     # at the position we care about
            product *= int(str(sequence_number)[position_in_number])  # multiply the right digit
            break

print(product)