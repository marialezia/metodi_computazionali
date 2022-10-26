import matplotlib.pyplot as plt
from scipy import integrate
import numpy as np
import pandas as pd

tabella = pd.read_csv('vel_vs_time.csv')
print(tabella)

vel = tabella['v']
time = tabella['t']


plt.plot(tabella['t'], tabella['v'], color = 'violet')
plt.xlabel('tempo [s]')
plt.ylabel('velocità [m\s]')
plt.show()

#help(integrate.simpson)

i = integrate.simpson(vel, time)
print('integrale = ', i)

spazio = np.zeros(len(time))
for i in range(1, len(time)+1):
    spazio[i-1] =  integrate.simpson(vel[:i],time[:i])

plt.plot(time,spazio, color = 'blue')
plt.xlabel('tempo [s]')
plt.ylabel('spazio [m]')
plt.show()
