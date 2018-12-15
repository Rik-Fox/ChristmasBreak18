
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
from MergeSort import *

m = 6
n = (2**m)

A = np.random.randint(1, 100, n)
B = np.random.randint(1, 100, n)
A

C = mergesort(A, B, n)
C
plt.figure()
plt.plot(A, '.')
plt.plot(B, '.')
plt.plot(C)
plt.show()

a = np.linspace(-50, 50, 100)
b = np.linspace(50, 150, 99)
b
E = mergepresorted(a, b)
E

plt.figure()
plt.plot(a)
plt.plot(b)
plt.plot(E)
plt.show()
# k = 13
#
# runtimes = np.zeros(k)
# th = np.zeros(k)
# number = np.zeros(k)
#
# for i in range(0, k):
#     m = i
#     n = (2**m)
#     A = np.random.randint(1, 100, n)
#     B = np.random.randint(1, 100, n)
#     C = mergesort(A, B, n)
#
#     runtimes[i] = C[2]
#     th[i] = n*np.log(n)
#     number[i] = n
