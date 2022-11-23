import numpy as np
import scipy
import matplotlib.pyplot as plt

def inv_cum(y):
    return 2*np.arccos(1-2*y)

yc = np.arange(0,1,0.001)
xc = inv_cum(yc)
plt.plot(yc, xc)
plt.grid()
plt.xlabel('y')
plt.ylabel('$c^{-1}(y)$')
plt.show()


# valri y distribuiti uniformemnte in (0, 1)
yrndq = np.random.uniform(low = 0, high = 1, size = 1000)

# valori x da cumulativa inversa
xrndq = inv_cum(yrndq)


fig, ax = plt.subplots(1,2, figsize=(11,5))
ax[0].hist(yrndq, bins=100, range=(0,1), color='cyan',   ec='darkcyan')
ax[0].set_title('Distribuzione y Cumulativa')
ax[0].set_xlabel('y cumulativa')

ax[1].hist(xrndq, bins=100, range=(0,2*np.pi), color='orange', ec='darkorange')
ax[1].set_xlabel('x')
plt.show()

