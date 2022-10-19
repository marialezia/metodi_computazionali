import numpy as np
import matplotlib.pyplot as plt

x = np.arange(11)
y = np.arange(0, 21, 2)

plt.plot(x,y, color = 'red')
plt.title('retta')
plt.xlabel('asse x')
plt.ylabel('asse y')
plt.show()

print(x)
print(y)
