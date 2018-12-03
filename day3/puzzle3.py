# Large square: 1'000 inches
# A claim contains:
#    - Number of inches btw left edge fabric and left edge rectangle
#    - "" btw top fabric and top rectangle
#    - Width of rectangle
#    - Height of rectangle

import os
path = 'your_path'
os.chdir(path)

## ----- PART ONE -----

import numpy as np
import re

# Read the input file
with open('input.txt') as f:
    inp = []
    for row in f.readlines():
        # Keep only the digits (+ matches 1 or more occurrence of preceding expression)
        row = re.split('[^0-9]+', row[1:].strip())
        inp.append([int(d) for d in row])

# Create an empty grid space
fabric = np.zeros((1000,1000))

# Fill up the grid
for n, x, y, dx, dy in inp:
    fabric[x:x+dx, y:y+dy] += 1

# Count the number of overlapping square inches
print(str(np.sum(fabric > 1)) + ' square inches of fabric are within two or more claims.')


## ----- PART TWO -----

# Iterate over the grid for each ID
for id, x, y, dx, dy in inp:
    # If for a given ID all the elements of the grid (sub-area) == 1
    # Then return the claim ID
    if np.all(fabric[x:x + dx, y:y+dy] == 1):
        print(id)
        break;

print('ID ' + str(id) + ' does not overlap with any other claims.')
