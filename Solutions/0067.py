"""
# Problem 67: Maximum Path Sum II
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a
triangle with one-hundred rows.
"""

with open('./Files/p067_triangle.txt', 'r') as tri_file:
    triangle = [[int(num.strip()) for num in line.split() if num] for line in tri_file.readlines()]

sums = triangle[0]
new_sums = []


# Like I mentioned back in #18, we have to prune at each layer, otherwise we get buried in
# computational complexity. There's probably a way to eliminate a few of the operations here,
# but we only have to do them like 5050 times, so it's nbd
for row in triangle[1:]:
    for sum_index, sum_value in enumerate(sums):
        new_sums.append([sum_value + row[sum_index], sum_value + row[sum_index + 1]])

    # okay so what we've done is figure out the two new sums each old sum can create. There is
    # overlap between all adjacent elements. The 1st element of 0 competes with the 0th element 1,
    # the 1st element of 1 competes with the 0th element of 2, etc, etc.

    sums = [new_sums[0][0]] # 0,0 has no competition
    for sum_pair_index, sum_pair in enumerate(new_sums[:-1]):
        a = sum_pair[1]
        b = new_sums[sum_pair_index + 1][0]

        # we write out all our competitions explicitly here, then figure out which one takes the
        # slot in each row

        if a > b:
            sums.append(a)
        else:
            sums.append(b)

    sums.append(new_sums[-1][-1]) # -1, -1 also has no competition, but we shouldn't forget it!
    new_sums = []


print(max(sums))