# AoC 2021 Day 3

import numpy as np
from scipy import stats

gamma=int(0)
epsilon=int(0)
gammaDec=int(0)
epsilonDec=int(0)

data = np.genfromtxt('puzzleInput.txt', delimiter=1, dtype=int)
mode = stats.mode(data)
gamma = np.array2string(mode[0])
gamma = gamma.strip("[] ")
gamma = gamma.replace(" ","")
epsilon = gamma.replace("1","x")
epsilon = epsilon.replace("0","1")
epsilon = epsilon.replace("x","0")

for digit in gamma:
    gammaDec = int(gammaDec*2 + int(digit))

for digit in epsilon:
    epsilonDec = int(epsilonDec*2 + int(digit))

print(gammaDec)
print(epsilonDec)

print("Final Value: " + str(gammaDec * epsilonDec))