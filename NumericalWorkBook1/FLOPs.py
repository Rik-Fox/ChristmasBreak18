import numpy as np
import matplotlib.pyplot as plt
from Recursion1 import *
from scipy import linalg

##### Quad precision does not work as well as julia as it is a
##### padded float64 as opposed to a true complier implementation
##### Tried to use a bigfloat pkg that wouldnt install and mpmath which did
##### however could not make it work and gave up after 2 hours
##### (it somehow took the value negative???!?!?!)

n = 128

a = np.float32(np.zeros(n))
b = np.zeros(n)
c = np.float128(np.zeros(n))

a = Recursive_32(a,n)
b = Recursive_64(b,n)
c = Recursive_128(c,n)

plt.figure()

plt.semilogy(a,label = "recursive 32")
plt.semilogy(b,label = "recursive 64")
plt.semilogy(c,label = "recursive 128")
#plt.show()

k=128

#ϵ's of varying magnitude to show perturbation growth\n",
ϵ_1 = 1E-8   # ~Float32\n",
ϵ_2 = 1E-16  # ~Float64\n",
ϵ_3 = 1E-32  # ~BigFloat

#arrays holding the analytical solution solved with the varying ϵ values\n",
e_1=perturb(ϵ_1,k)
e_2=perturb(ϵ_2,k)
e_3=perturb(ϵ_3,k)

#plt.figure()
plt.semilogy(e_1,label = "perturbed exact 32")
plt.semilogy(e_2,label = "perturbed exact 64")
plt.semilogy(e_3,label = "perturbed exact 128")
plt.legend()
plt.show()
