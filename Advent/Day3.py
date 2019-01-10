import pandas as pd


file = open("Day3.txt", "r")
input = []

for line in file:

    input.append(line)

file.close()
input

df = pd.read_csv("Day3.txt", delimiter="\n")

df.describe
