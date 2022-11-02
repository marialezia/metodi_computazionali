import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy import optimize


def f(x, mu, sigma, A):
    return A*np.exp(-((np.log(x)-mu)**2)/(2*sigma**2))/(np.sqrt(2*math.pi)*sigma*x)

dati = pd.read_csv('fit_data.csv')
print(dati)
x = dati['x']
y = dati['y']
y_err = np.sqrt(y)

plt.errorbar(x,y, yerr = y_err,fmt= '.')
plt.xscale('log')
plt.show()

pstart = np.array([1,1,100])
params, params_covariance = optimize.curve_fit(f, x, y, sigma = y_err, absolute_sigma = True, p0 = [pstart])

print('params: ', params)
print('params covariance: ', params_covariance)

yexp = f(x, params[0], params[1], params[2])

plt.errorbar(x,y, yerr = y_err,fmt= '.')
plt.errorbar(x, yexp)
plt.xscale('log')

plt.show()

chi2 =  np.sum( (yexp - y)**2 /y )
print('chi2 =', chi2)

#help(optimize.curve_fit)
