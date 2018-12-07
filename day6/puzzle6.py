#############
# Common Code
#############

# @nbonfils

import sys

INPUT_FILE = "input.txt"

coords = []
with open(INPUT_FILE) as f:
    for line in f:
        x, y = line.strip('\n').split(', ')
        coords.append((int(x), int(y)))

def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def grid_bounds(coords, margin):
    x_min = min(coords)[0] - margin
    x_max = max(coords)[0] + 1 + margin
    y_min = min(coords, key=lambda x: x[1])[1] - margin
    y_max = max(coords, key=lambda x: x[1])[1] + 1 + margin
    return x_min, x_max, y_min, y_max

##########
# Part One
##########

def gen_region_grid(coords, margin=0):
    x_min, x_max, y_min, y_max = grid_bounds(coords, margin)

    grid = []
    for y in range(y_min, y_max):
        for x in range(x_min, x_max):
            min_dist = (-1, sys.maxsize)

            for i, coord in enumerate(coords):
                dist = manhattan_distance(coord, (x, y))
                
                if dist < min_dist[1]:
                    min_dist = (i, dist)
                elif dist == min_dist[1]:
                    min_dist = ('.', dist)

            grid.append(min_dist[0])
    return grid


grid_no_margin = gen_region_grid(coords)
grid_margin = gen_region_grid(coords, 10)

count = []
for i in range(len(coords)):
    no_margin = grid_no_margin.count(i)
    margin = grid_margin.count(i)

    if margin == no_margin:
        count.append((margin, i))

print("Part One:", max(count)[0])

##########
# Part Two
##########

def count_safe(coords, thresh):
    x_min, x_max, y_min, y_max = grid_bounds(coords, 0)

    count = 0
    for y in range(y_min, y_max):
        for x in range(x_min, x_max):
            total_dist = 0

            for i, coord in enumerate(coords):
                dist = manhattan_distance(coord, (x, y))
                
                total_dist += dist

            if total_dist < thresh:
                count += 1

    return count

print("Part Two:", count_safe(coords, 10000))