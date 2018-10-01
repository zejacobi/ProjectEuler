"""
# Problem 59: XOR Decryption

Each character on a computer is assigned a unique code and the preferred standard is ASCII
(American Standard Code for Information Interchange). For example, uppercase A = 65,
asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte
with a given value, taken from a secret key. The advantage with the XOR function is that using the
same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is
made up of random bytes. The user would keep the encrypted message and the encryption key in
different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a
password as a key. If the password is shorter than the message, which is likely, the key is
repeated cyclically throughout the message. The balance for this method is using a sufficiently
long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted
ASCII codes, and the knowledge that the plain text must contain common English words, decrypt
the message and find the sum of the ASCII values in the original text.
"""

# Thank you, Code Book

from os.path import join as path_join
from operator import itemgetter

with open(path_join('Files', 'p059_cipher.txt'), 'r') as byte_file:
    byte_string = byte_file.readline()  # just has one line
    encrypted_bytes = [chr(int(char)) for char in byte_string.split(',')]

# break up the characters into three separate ciphers for frequency analysis
freq_1 = [char for index, char in enumerate(encrypted_bytes) if index % 3 == 0]
freq_2 = [char for index, char in enumerate(encrypted_bytes) if index % 3 == 1]
freq_3 = [char for index, char in enumerate(encrypted_bytes) if index % 3 == 2]


def create_frequency_list(character_list):
    frequency_key = {}
    for item in character_list:
        frequency_key[item] = frequency_key.get(item, 0) + 1

    sortable_list = []
    for item in frequency_key.keys():
        sortable_list.append([item, frequency_key[item]])

    return sorted(sortable_list, key=itemgetter(1), reverse=True)


frequency_table_1 = create_frequency_list(freq_1)
frequency_table_2 = create_frequency_list(freq_2)
frequency_table_3 = create_frequency_list(freq_3)

# I checked and both have a strong (~2x next highest) candidate for most common letter
# so let's assume that this is a space

space_1 = ord(frequency_table_1[0][0])
space_2 = ord(frequency_table_2[0][0])
space_3 = ord(frequency_table_3[0][0])


key = chr(ord(' ') ^ space_1) + chr(space_2 ^ ord(' ')) + chr(space_3 ^ ord(' '))

print(sum([ord(key[index % 3]) ^ ord(letter) for index, letter in enumerate(encrypted_bytes)]))