# Timestamps are written using year-month-day hour:minute format
# all asleep/awake times are during the midnight hour
# Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?

import os
path = '/Users/antoinegex-fabry/Desktop/AdventOfCode2018/day4'
os.chdir(path)

## ------ PART ONE -----

import datetime as dt
import re

input_file = 'input.txt'
results = []
i = 0
with open(input_file, newline = '') as f:
    data = f.readlines()

    for row in data:
        addition = [None]*3
        temp = row[1:].split('] ')
        # Get time
        date = dt.datetime.strptime(temp[0], '%Y-%m-%d %H:%M')
        # Get ID if possible
        try:
            ID = re.findall('\d+', temp[1])[0]
        except IndexError:
            ID = None
        # Get the "action"
        if temp[1].find('begins') != -1:
            action = 'begin'
        elif temp[1].find('wakes') != -1:
            action = 'wakeup'
        else:
            action = 'asleep'

        results.append([date, ID, action])

    # Sort the results by date (l[0]) and hour (l[2])
    results = sorted(results, key=lambda l: l[0])

# Finally,give ID to everyone
for i in range(1, len(results)):
    # If current line is None, take the ID of the previous element
    if results[i][1] is None:
        results[i][1] = results[i-1][1]

print(results)

import pandas as pd
df = pd.DataFrame()
df['date'] = [date for date, ID, action in results]
df['ID'] = [ID for date, ID, action in results]
df['action'] = [action for date, ID, action in results]

df['time_asleep'] = [0]*len(df)
for i in range(1, len(df)):
    if df.loc[i, 'action'] == 'wakeup' and df.loc[i-1, 'action'] == 'asleep':
        df.loc[i, 'time_asleep'] = int((df.date[i] - df.date[i-1]).seconds / 60)
        # df.loc[i, 'time_asleep'] = int(df.time_asleep[i].seconds / 60)

# Find the ID with the most minutes asleep
grouped = df.loc[:, ['ID', 'time_asleep']].groupby('ID').sum()
print( grouped.sort_values(by = 'time_asleep', ascending = False) )
print('ID 521 is the one who slept the most.')


import numpy as np
# Select the minutes where he/she slept
subdf = df.loc[df.ID == '521', :].reset_index()

times = []
for i in range(0, len(subdf) - 1):
    temp = subdf.iloc[i:i+2, :]
    if temp.action[i] == 'asleep':
        start = int(temp.date[i].minute)
        increment = int(temp.time_asleep[i+1])
        times.append([start, increment])

time_table = np.zeros((50, 60))
i = 0
for start, increment in times:
    time_table[i, start:start+increment] += 1
    i+=1

# Sum by column
total = np.sum(time_table, axis = 0)
final = total.argmax()
print('Minutes when he/she slept the most is the ' + str(int(final)) + 'th minute.')

# Result
final_result = final * int(subdf.ID[0])

## ----- PART TWO -----

# WIP
