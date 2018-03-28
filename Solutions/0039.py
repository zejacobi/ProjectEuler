"""
# Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are
exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from math import sqrt

# The naive solution is to try every value of p<=1000 and look for right angles
# The clever solution is to try every two combo between 1 and 1000, continuing whenever the last
# angle is too big, and then add them together add the end.

perimeters = {}
max_amount = 3
val_at_max = 120

for i in range(1, 333):
    for j in range(i, 1000 - 2 * i):
        result = sqrt(i**2 + j ** 2)
        if i + j + result > 1000:
            break
        if result == round(result):
            perimeter = int(i + j + result)
            perimeters[perimeter] = perimeters.get(perimeter, 0) + 1

            if perimeters[perimeter] > max_amount:
                val_at_max = perimeter
                max_amount = perimeters[perimeter]

# yep, that works, and takes basically no time. Testing tells me it tries only 76,934 combinations,
# saving a bunch of time compared to something less bounded. This lets us skip 93% of the
# combinations we'd do if we did 1 to 1000 nested.

print(val_at_max)