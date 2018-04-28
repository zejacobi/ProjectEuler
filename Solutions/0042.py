"""
### PROBLEM 42: Coded triangle numbers

The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1); so the first ten
triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and
adding these values we form a word value. For example, the word value for SKY is
19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a
triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly
two-thousand common English words, how many are triangle words?
"""

# wait is it really this easy? I almost want to code in French or something to make this less
# trivial
from os import path
from string import ascii_uppercase

file_path = path.join('Files', 'p042_words.txt')


triangle_numbers = []

# let's pregenerate, IDK, 1k triangle numbers? Seems excessive, but probably quicker than iterating
# through all 2000 words twice and easier than doing some complicated memoization thing on the
# checking array.
for i in range(1, 1000):
    triangle_numbers.append(i*(i+1)/2)

letter_values = {letter: index + 1 for index, letter in enumerate(ascii_uppercase)}

with open(file_path, 'r') as words:
    # Ah, I love problems where most of the answer can be done in one absurd triple list
    # comprehension
    print(len([1 for num in
              [sum([letter_values[letter] for letter in word[1:-1]])
               for word in words.read().split(',') if word] if num in triangle_numbers]))
    # Some people love python for it's clarity. Me? I just like to abuse list comprehension
