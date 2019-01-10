from itertools import accumulate, cycle
import numpy as np
import matplotlib.pyplot as plt

file = open("Day1.txt", "r")
input = []

for line in file:

    input.append(int(line))

file.close()

num = np.array(input)

print("Part 1", "     ", sum(num))

seen = {0}
print("Part 2", "     ", next(f for f in accumulate(cycle(input)) if f in seen or seen.add(f)))
