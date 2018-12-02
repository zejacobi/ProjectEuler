"""
# Problem 92: Square digit chains

A number chain is created by continuously adding the square of the digits in a number to form a new
number until it has been seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most
amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

results = {
    44: 1,
    32: 1,
    23: 1,
    13: 1,
    31: 1,
    10: 1,
    1: 1,
    85: 89,
    89: 89,
    145: 89,
    42: 89,
    24: 89,
    20: 89,
    2: 89,
    4: 89,
    16: 89,
    61: 89,
    73: 89,
    37: 89,
    58: 89
}

# gonna cheat and take advantage of all the ones they give me.

count_89 = 13

# my first attempt used lists to keep track; that was bad, because this made the whole thing
# n ^ 2 (and our n is quite large here!). Using lookups and a counter makes this n.

upper_bound = 10000000

for num in range(1, upper_bound):
    temp_nums = [num]
    new_num = sum([int(i) ** 2 for i in str(num)])
    while True:
        final_result = results.get(new_num, None)
        if final_result == 1:
            for temp in temp_nums:
                results[temp] = final_result
            break
        elif final_result == 89:
            for temp in temp_nums:
                exists = results.get(temp, None)
                if not exists and temp < upper_bound:
                    count_89 += 1
                    results[temp] = final_result
            break
        temp_nums.append(new_num)
        new_num = sum([int(i) ** 2 for i in str(new_num)])

print(count_89)