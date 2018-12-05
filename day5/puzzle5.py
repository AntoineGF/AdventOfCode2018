# Polymer is formed by smaller units which, when triggered, react with each other
# such that two adjacent units of the same type and opposite polarity are destroyed.
# -> Units' types are represented by letters;
# -> units' polarity is represented by capitalization. For instance, r and R are
# -> units with the same type but opposite polarity, whereas r and s are entirely
# -> different types and do not react.

# EXAMPLE
# aA -> reaction -> nothing left behind
# abBA -> reaction bB -> leaves aA -> reaction -> nothing is left behind
# abAB -> nothing happens
# aabAAB -> aa are identical (same type) -> same polarity, nothing happens

# ----- COMMON CODE -----

import os
os.chdir('/Users/antoinegex-fabry/Desktop/AdventOfCode2018/day5')

# Get the input
with open('input.txt', newline = '') as f:
    polymer = f.readlines()[0].strip('\n')

# ----- PART ONE -----

# Strings are immutable, so change it first into a list to apply particular methods
polymer = list(polymer)

# A naive solution would be to compare recursiverly element by element
def reacting(polymer):
    i = 1
    while i < len(polymer):

        # If two consecutive are exactly the same, go on (same polarity)
        if polymer[i] != polymer[i-1] and polymer[i].lower() == polymer[i-1].lower():

            del(polymer[i], polymer[i-1])
            # If we removed two units, we must go back one units before
            i -= 1

        else:
            i += 1

        # Reinitialise the index if it becomes negative (otherwise it will compare
        # the last element in the list, and this may result in uncontrolled patterns)
        if i < 0:
            i = 0

    return polymer

polymer = reacting(polymer)
result = ''.join(polymer)
# print('Final string is: ' + result)
print('PART ONE:')
print('The length of reacted polymer is of ' + str(len(result)) + '\n')

## ----- PART TWO -----

# Get the input
with open('input.txt', newline = '') as f:
    polymer = f.readlines()[0].strip('\n')

result = []
for i in range(0,26):
    # Removing letters step by step
    temp = polymer.replace(chr(ord('a') + i), '')
    temp = temp.replace(chr(ord('A') + i), '')
    # Function needs a list
    temp = list(temp)
    # Store the value of interest
    result.append( len(reacting(temp)) )

alphabet = [chr(ord('a') + i) + "/" + chr(ord('A') + i) for i in range(0,26)]
final = alphabet[ result.index(min(result)) ]
print('PART TWO:')
print('The smallest polymer is obtained by removing the pair: ' + final)
print('Whose length is of ' + str(min(result)))
