import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def v(x, k):
    return k*x**6

def f(x0, x, k):
    y = 1/np.power(v(x0, k)-v(x, k), 0.5)
    return y

def periodo(x0, m, k):
    x = np.arange(0, x0, 0.1)
    y = f(x0, x, k)
    T = np.sqrt(8*m)*integrate.simpson(y, x)
    return T

m = 0.5
k = 2
x0 = 50

T = periodo(x0, m, k)
print(T)

xx = np.arange(0,50,1)

T = np.zeros(len(xx))
for i in range(1, len(xx)):
    x0 = xx[i]
    T[i-1] = periodo (x0, m, k)
print(T)

plt.plot(xx, T)
plt.show()




"""
xx = np.arange(-5,5.05, 0.1)
xx2 = np.arange(0, 5.05, 0.1)

m = 0.5
k = 2

plt.plot(xx, v(xx, k), color='slategray')
plt.axvline(color='k', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('V(x)')
plt.plot(4.5, v(4.5, k), 'o', markersize=12, color='tomato')
plt.show()



T = np.zeros(len(xx2))
for i in range(1, 51):
    T[i-1] = periodo(xx2[i], xx2[0:i], k)
print(T)
    
    """
