import sys
import numpy as np
import scipy
import matplotlib.pyplot as plt


def inv_cum(y):
    return 2*np.arccos(1-2*y)

def random_walk2(step, N):
    deltax = np.zeros(N+1)
    deltay = np.zeros(N+1)
    tmpx = 0
    tmpy = 0
    y = np.random.uniform(low = 0, high = 1, size = N)
    phi = inv_cum(y)
    for i in range(len(phi)):
        tmpx = tmpx+step*np.cos(phi[i])
        tmpy = tmpy+step*np.sin(phi[i])
        deltax[i+1] = tmpx
        deltay[i+1] = tmpy
    return deltax, deltay

for i in range(5):
    x, y = random_walk2(1,1000)
    plt.plot(x,y)
plt.xlabel('$\Delta x$')
plt.ylabel('$\Delta y$')
plt.show()

passi10x = np.zeros(1000)
passi100x = np.zeros(1000)
passi1000x = np.zeros(1000)

passi10y = np.zeros(1000)
passi100y = np.zeros(1000)
passi1000y = np.zeros(1000)


for i in range(1000):
     x, y = random_walk2(1,1000)
     passi10x[i] = x[10]
     passi10y[i] = y[100]
     passi100x[i] = x[100]
     passi100y[i] = y[1000]
     passi1000x[i] = x[1000]
     passi1000y[i] = y[1000]


plt.plot(passi1000x, passi1000y, 'o', markersize = 4, alpha = 0.5, color = 'royalblue', label = '1000 passi')     
plt.plot(passi100x, passi100y, 'o', markersize = 4, alpha = 0.5, color = 'slateblue', label = '100 passi')
plt.plot(passi10x, passi10y, 'o',markersize = 4, alpha = 0.5, color = 'mediumaquamarine', label = '10 passi')

plt.legend()
plt.show()



