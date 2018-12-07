#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:07:10 2018

@author: antoinegex-fabry
"""

import numpy as np
import sys
import os
os.chdir('/Users/antoinegex-fabry/PythonProjects/AdventOfCode2018/day6')

# Import data
coordinates = []
with open("input.txt") as f:
    for line in f:
        x, y = line.strip('\n').split(', ')
        coordinates.append((int(x), int(y)))

## ----- FUNCTIONS -----
# Manhattan distance 
def calculateManhattan(coord1, coord2): 
    result = abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])
    return result

def grid_bounds(coordinates, margin):
    x_min = min(coordinates)[0] - margin
    x_max = max(coordinates)[0] + 1 + margin
    y_min = min(coordinates, key=lambda x: x[1])[1] - margin
    y_max = max(coordinates, key=lambda x: x[1])[1] + 1 + margin
    return x_min, x_max, y_min, y_max


def get_grid(coordinates, margin):
    x_min, x_max, y_min, y_max = grid_bounds(coordinates, margin)
    
    # Store the closest coordinates
    grid = np.zeros( (500,500))
    
    for x in range(x_min,x_max):
        for y in range(y_min, y_max):
            # Create the set of point that we will use to compute the distances 
            # from all coordinates
            point = (x, y)
            min_dist = (-1, sys.maxsize)
            for i, ele in enumerate(coordinates):
                dist = calculateManhattan(point, ele)
                
                if dist < min_dist[1]:
                    min_dist = (i, dist)
                
                elif dist == min_dist[1]:
                    min_dist = (-1, dist)
                
            # Closest coordinate to that point (x,y)
            grid[x,y] = min_dist[0]
            
    return grid


## ---- PART ONE -----

# We add a margin because if the area is finite, then changin the x_min, x_max etc
# values must not change their areas. 
# However, if the area changes btw grid1 and grid2, then the area is NOT finite
# and must not be counted as a possible candidate
grid1 = get_grid(coordinates, 0)
grid2 = get_grid(coordinates, 10)

# Count for each grid
unique, counts = np.unique(grid1, return_counts=True)
countDict1 = dict(zip(unique, counts))
unique, counts = np.unique(grid2, return_counts=True)
countDict2 = dict(zip(unique, counts))

# Candidates 
candidates = []
keys = countDict1.keys()
for k in keys: 
    if countDict1[k] == countDict2[k]:
        candidates.append(countDict1[k])

result = max(candidates)
print('PART ONE: ' + str(result))



## ----- PART TWO ----- 

# Add up the distances top all the coordinates 
def get_grid_distances(coordinates, margin):
    x_min, x_max, y_min, y_max = grid_bounds(coordinates, margin)
    
    # Store the closest coordinates
    grid = np.zeros( (500,500))
    
    for x in range(x_min,x_max):
        for y in range(y_min, y_max):
            # Create the set of point that we will use to compute the distances 
            # from all coordinates
            point = (x, y)
            dist = []
            for i, ele in enumerate(coordinates):
                dist.append(calculateManhattan(point, ele))
            
            # Total distance of all coordinates to that point (x,y)
            dist = sum(dist)
            
            # Condition
            if dist < 10000:
                grid[x,y] = 1
            else:
                grid[x,y] = 0
            
    return grid

grid_distances = get_grid_distances(coordinates, 0)
result = int(np.sum(grid_distances))

print('PART TWO: ' + str(result))


