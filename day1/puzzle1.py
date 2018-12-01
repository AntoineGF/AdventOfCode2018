# Starting with a frequency of zero, what is the resulting frequency after all
# of the changes in frequency have been applied?

## -----  PART ONE -----
import os
path = 'your_path'
os.chdir(path)

import csv
from itertools import chain
filename = "input1.txt"
results = []

with open(filename, newline = '') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row)

results = list(chain.from_iterable(results))

clean = []
for ele in results:
    if ele[0] == "+":
        clean.append( int(ele[1:]) )
    else:
        clean.append( int(ele[1:]) * -1 )

print(sum(clean))

## -----  PART TWO -----
import numpy as np
def has_duplicates(lst):
    # Find the first frequency
    uniques = np.unique(lst, return_index = True, return_counts = True)

    frequencies = uniques[0]
    # indexes = uniques[1]
    counts = uniques[2]

    position = np.array([c == 2 for c in counts])
    result = frequencies[position]

    if result.size == 0:
        print("No duplicates found !")
        return False

    else:
        return True


inpt = clean
result_frequency = np.cumsum(inpt)[1:]
i = 0
maxit = 300
while not has_duplicates(result_frequency):
    i += 1
    print("Iteration: " + str(i))
    # While no duplicate: iterate again
    new_inpt = np.append(result_frequency[len(result_frequency) - 1], inpt)
    result_bis = np.cumsum(new_inpt)[1:]
    result_frequency = np.append(result_frequency, result_bis)

    if i == maxit:
        break


# At this point, result_frequency has at least one duplicate element
# Find the first duplicate
uniques = np.unique(result_frequency, return_index = True, return_counts = True)

frequencies = uniques[0]
indexes = uniques[1]
counts = uniques[2]

position = np.array([c > 1 for c in counts])
result = frequencies[position]

# Careful for first occurence
if result.size > 1:
    # Find the position of the smaller index
    pos = [idx == min(indexes[position]) for idx in indexes]
    result = frequencies[pos]

print("The first frequency that has a duplicate is " + str(result[0]) + ".")


## ----- REDDIT SOLUTION -----

# Task 1
import itertools
data = [int(x) for x in open("input1.txt").readlines()]
print(sum(data))

# Task 2
freq = 0
seen = set([0])
for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq); break
    seen.add(freq)

seen = set([0])
freq = 0
for num in itertools.cycle(data):
    freq = freq + num
    if freq in seen:
        print(freq); break
    seen.add(freq)
