# Exercise:
# Scan the likely candidate boxes and count the number that have an ID containing
# EXACTLY TWO OF ANY LETTER, and those containing EXACTLY THREE of any letter.
# Multiply those two to get a checksum

# ------------------------------------------------------------------------------
import csv
import os
path = 'your_path'
os.chdir(path)

# Read the data from the text file
results = []
i = 0
with open('input.txt', newline = '') as inputfile:
    data = inputfile.readlines()
    # Remove the '\n' from elements
    for ele in data:
        print(ele)
        data[i] = ele[:-1]
        i += 1

# example data
# data = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
total2 = 0
total3 = 0
for row in data:
    # Get a dictionary that counts the occurences of every character in the element (row)
    occurences = dict((letter, row.count(letter)) for letter in set(row))
    # Get the values only
    counting = list(occurences.values())
    # Count the EXACT number 2 and EXACT 3
    two_letters = sum([ele == 2 for ele in counting])
    three_letters = sum([ele == 3 for ele in counting])
    # Controlling for the specific conditions
    if two_letters >= 1 and three_letters >= 1:
        total2 += 1
        total3 += 1
    elif two_letters >= 1 and three_letters == 0:
        total2 += 1
        total3 += 0
    elif two_letters == 0 and three_letters >= 1:
        total2 += 0
        total3 += 1

# Results:
print(str(total2) + ' boxes contain a letter which appears exactly twice.')
print(str(total3) + ' boxes contain a letter which appears exactly three times.')
print('Out of ' + str(len(data)) + ' Box IDs.')
print('RESULT: ' + str(total2 * total3))
