"""
# PROBLEM 22

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

from os import path
import string


# handle wherever you might run this thing from
try:
    file_path = path.join('..', 'Files', 'p022_names.txt')
    with open(file_path) as r_file:
        line = r_file.readline()

except IOError:
    file_path = path.join('Files', 'p022_names.txt')
    with open(file_path) as r_file:
        line = r_file.readline()

# strip off the opening and closing quotes, then break by quotes
line = line[1:-1]
names = line.split('","')

names = sorted(names)

# we can use the ascii_uppercase string to get our letter ranks and the enumerate index to get
# our name ranks. We just need to adjust both by 1 each time.
print(sum([sum([string.ascii_uppercase.index(letter) + 1 for letter in name]) * (index + 1)
           for index, name in enumerate(names)]))
