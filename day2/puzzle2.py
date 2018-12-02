# Exercise:
# Scan the likely candidate boxes and count the number that have an ID containing
# EXACTLY TWO OF ANY LETTER, and those containing EXACTLY THREE of any letter.
# Multiply those two to get a checksum

# ----- PART ONE -----
import os
path = '/Users/antoinegex-fabry/Desktop/AdventOfCode2018/day2'
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

## ----- PART TWO -----

# Ex: What letters are common between the two correct box IDs?
# data = ['abcde', 'fghij', 'vweyo', 'fguij']

foundID = False
i = 0
check = [None]*len(data[0]) # 26 is length of a row in input.txt
for row in data:
    print("Checking the " + str(i) +"th row.")
    letters_initial = [letter for letter in data[i]]
    # Index to compare the rest of the data (could probably be more efficient)
    for j in range(i + 1, len(data)):
        letters_compare = [letter for letter in data[j]]
        for pos in range(0, len(letters_initial)):
            check[pos] = ( letters_initial[pos] == letters_compare[pos] )

        # If (len(letters) - 1) elements in common, it means that only one letter is different.
        if sum(check) == len(letters_initial) - 1:
            # print(letters_initial)
            # print(letters_compare)
            print(data[i])
            print(data[j])
            # If found, do not iterate over the remaining obsverations
            foundID = True
            break
    # Break if found the two desired IDs. 
    if foundID:
        break
    # Use the next row and compare it with rest of data input
    i += 1
