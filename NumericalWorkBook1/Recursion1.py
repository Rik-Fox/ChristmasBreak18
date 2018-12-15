import numpy as np


def Recursive_128(x, n):

    x = np.float128(np.zeros(n))
    x[0] = np.float128(1)
    x[1] = np.float128(2)/np.float128(3)

    for i in range(2, n):
        x[i] = np.float128(2)*x[i-1] - ((np.float128(8)/np.float128(9))*(x[i-2]))

    return x


def Recursive_64(x, n):

    x[0] = 1
    x[1] = 2/3

    for i in range(2, n):
        x[i] = 2*x[i-1] - (8/9)*(x[i-2])

    return x


def Recursive_32(x, n):

    x[0] = np.float32(1)
    x[1] = np.float32(2)/np.float32(3)

    for i in range(2, n):
        x[i] = np.float32(2)*x[i-1] - ((np.float32(8)/np.float32(9))*(x[i-2]))

    return x


def perturb(p, n):

    s = np.zeros(n)

    for i in range(0, n):
        s[i] = (1-(3/2)*p)*((2/3)**(i-1)) + (3/2)*p*((4/3)**(i-1))  # perturbed solution

    return s
