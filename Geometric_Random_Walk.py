import warnings
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as lg
from scipy import stats


M = 500
n = 100
mu = 0
sigma = 0.2

def GRWalk(n,M,mu,sigma):

    X = np.array(np.random.normal(mu,sigma,size=(n,M)))

    Y = np.zeros(shape=(n,M))
    X[:,0] = 0

    for j in range(0,M):
        Y[:,j] = np.cumsum(X[:,j])

    return Y

Y = GRWalk(n,M,mu,sigma)

Z = np.exp(Y)

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.plot(Y)

plt.subplot(1,2,2)
plt.plot(Z)

#plt.show()

sum_z = np.cumsum(Z,axis = 1)

mu_n = (1/M)*sum_z[:,M-1]
sigma_n = np.std(Z,axis=1)

plt.figure(figsize=(12,6))
plt.errorbar(range(0,n),mu_n,yerr=sigma_n)
#plt.show()


plt.figure(figsize=(12,6))
plt.boxplot(Z[9,:])
plt.show()

print(sum_z)
