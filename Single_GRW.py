import warnings
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as lg
from scipy import stats

n = 100
mu = 0
sigma = 0.2

X = np.array(np.random.normal(mu,sigma,size=n))

Y = np.cumsum(X)
Y[0] = 0
Z = np.exp(Y)
print(Z.shape)
sum_z = np.cumsum(Z)
print(sum_z)
mu_n = sum_z/n
print(mu_n)
plt.plot(range(0,100),mu_n)
plt.show()
