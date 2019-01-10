import numpy as np
import matplotlib.pyplot as plt


def pred(X, w):

    P = np.dot(X, w)

    return P


def weightgrad(X, n, P, T):

    Δ = P-T
    C_grad = (1/n)*np.dot(X.T, Δ)

    return C_grad


def cost(P, T, n):

    S = (P-T)**2
    cost1 = (1/(2*n))*np.sum(S)

    return cost1


n = 10
t = (2 * np.linspace(0, 1, n)) + 1 + np.random.normal(0, 0.02, n)
X = np.vstack([t, np.ones(n)]).T
T = np.copy(t)
w = [0, 0]
P = pred(X, w)

α = 0.01
itr = 1000


def myfit(w, X, P, T, n):

    for i in range(itr):

        cost1 = cost(P, T, n)
        plt.plot(cost1)

        P = pred(X, w)
        weight_grad = weightgrad(X, n, P, T)
        w -= α*weight_grad

    return w


w = myfit(w, X, P, T, n)
x = np.linspace(0, 1, n)

linfit = (w[0]*x) + w[1]
linfit
print(t)
plt.figure()
plt.scatter(x, t)
plt.plot(x, linfit)
plt.show()
