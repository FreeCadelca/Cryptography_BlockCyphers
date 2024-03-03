import pprint
import sys
from AlphabetConfig import *

print('Enter the text for analysis of blocks of letters in dictionary ALPHABET')
text = []
line = input().lower()
while line != '':
    if len(line) % 2 != 0:
        line += '%'
    text.append(line)
    line = input().lower()

number_of_blocks = {i: {j: 0 for j in ALPHABET} for i in ALPHABET}

total_blocks = 0
for i in text:
    for k in range(0, len(i), 2):
        block = i[k:k + 2]
        number_of_blocks[block[0]][block[1]] += 1
        total_blocks += 1

top_of_blocks = []
for i in number_of_blocks.keys():
    for j in number_of_blocks[i].keys():
        top_of_blocks.append((i + j, number_of_blocks[i][j]))
top_of_blocks.sort(key=lambda x: -x[1])
print(top_of_blocks[:5])
# for ciphertext: [('9i', 186), ('%r', 151), ('wc', 149), ('ku', 141), ('2!', 140)]
# for plaintext:  [('e ', 186), (' t', 151), ('th', 149), (' a', 141), ('s ', 140)]
