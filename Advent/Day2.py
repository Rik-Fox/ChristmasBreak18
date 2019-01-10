from itertools import accumulate, cycle
import numpy as np
import matplotlib.pyplot as plt

file = open("Day2.txt", "r")
input = []

for line in file:

    input.append(line)

file.close()

twos = 0
lf2 = True
threes = 0
lf3 = True
count = 0
itr = 0

for k in range(len(input)):
    lf2 = True
    lf3 = True
    for i in range(len(input[k])):
        count = 0
        itr = i
        for j in range(len(input[k])):

            if input[k][itr] == input[k][j]:
                # print('hi')
                count += 1

        if count == 2 and lf2 == True:
            twos += 1
            lf2 = False
        if count == 3 and lf3 == True:
            threes += 1
            lf3 = False

    # print(twos, threes)

checksum = twos*threes
print(checksum)

simchar = []
find = []
newfind = []

for k in range(len(input)-1):
    find = []
    for i in range(k+1, len(input)-1):
        for j in range(len(input[k])):

            if input[k][j] == input[i][j]:
                newfind.append(input[k][j])

        if len(newfind) > len(find):
            find = newfind
        newfind = []
    simchar.append(find)

for d in range(len(input)-1):
    if len(simchar[d]) == len(input[0])-1:
        print(d)
        print(simchar[d])
