"""
# PROBLEM 18

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

# SPOILERS FOR PROBLEM 67!!!
# Note for future problem like this: there will be many sums that will be identical except for the
# first number. E.g. 17 + 18 + 20 + 19 + 88 + 99 + 41 + 41 + 53 + 70 + 91 + 63 + 04, v.s.
# 47 + 18 + 20 + 19 + 88 + 99 + 41 + 41 + 53 + 70 + 91 + 63 + 04. A smarter algorithm would prune
# all of the suboptimal equivalent sums and only look for the greatest of them. Basically, at each
# step, check you neighbour. If it's greater, then don't go down that path

# If you were doing this line by line and not recursively, you'd want to find the highest score
# at each point on the triangle and prune everything else for the next step.

# For this one, I already had the recursive solution done by the time I realized this, so I'll let
# it be.

triangle = [[int(num) for num in line.split() if num] for line in
            """75
               95 64
               17 47 82
               18 35 87 10
               20 04 82 47 65
               19 01 23 75 03 34
               88 02 77 73 07 63 67
               99 65 04 28 06 16 70 92
               41 41 26 56 83 40 80 70 33
               41 48 72 33 47 32 37 16 94 29
               53 71 44 65 25 43 91 52 97 51 14
               70 11 33 28 77 73 17 78 39 68 17 57
               91 71 52 38 17 14 91 43 58 50 27 29 48
               63 66 04 68 89 53 67 30 73 16 69 87 40 31
               04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split('\n')]

sums = []


def calculate_sum(line, position, current_sum):
    this = triangle[line][position]
    current_sum += this
    if len(triangle) > line + 1 and len(triangle[line + 1]) > position + 1:
        calculate_sum(line + 1, position + 1, current_sum)

    if len(triangle) > line + 1:
        calculate_sum(line + 1, position, current_sum)
    else:
        sums.append(current_sum)


calculate_sum(0, 0, 0)
best = 0
for option in sums:
    if option > best:
        best = option

print(best)
