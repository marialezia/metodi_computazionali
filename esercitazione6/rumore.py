import numpy as np
import pandas as pd
from scipy import constants, fft
import matplotlib.pyplot as plt
from scipy import optimize

#legge i file
data_sample1 = pd.read_csv('data_sample1.csv')
data_sample2 = pd.read_csv('data_sample2.csv')
data_sample3 = pd.read_csv('data_sample3.csv')


t1 = data_sample1['time']
m1 = data_sample1['meas']
t2 = data_sample2['time']
m2 = data_sample2['meas']
t3 = data_sample3['time']
m3 = data_sample3['meas']

#faccio grafico
plt.plot(t1, m1, color = 'rebeccapurple')
plt.plot(t2, m2, color = 'springgreen')
plt.plot(t3, m3, color = 'orange')
plt.show()

#calcolo trasformate
tf1 = fft.rfft(m1.values)
tf2 = fft.rfft(m2.values)
tf3 = fft.rfft(m3.values)

tf1f = 0.5*fft.rfftfreq(tf1.size, d=1)
tf2f = 0.5*fft.rfftfreq(tf2.size, d=1)
tf3f = 0.5*fft.rfftfreq(tf3.size, d=1)
print(tf1f)

#grafici spettro di potenza
plt.plot(np.absolute(tf1[:tf1.size//2])**2, 'o', markersize=3, color = 'rebeccapurple')
plt.plot(np.absolute(tf2[:tf2.size//2])**2, 'o', markersize=3, color = 'springgreen')
plt.plot(np.absolute(tf3[:tf3.size//2])**2, 'o', markersize=3, color = 'orange')
plt.xscale('log')
plt.yscale('log')
plt.show()

#grafici spettro di potenza in funzione delle frequenze
plt.plot(tf1f[:int(tf1.size/2)],np.absolute(tf1[:tf1.size//2])**2, 'o', markersize=3, color = 'rebeccapurple')
plt.plot(tf2f[:int(tf2.size/2)],np.absolute(tf2[:tf2.size//2])**2, 'o', markersize=3, color = 'springgreen')
plt.plot(tf3f[:int(tf3.size/2)],np.absolute(tf3[:tf3.size//2])**2, 'o', markersize=3, color = 'orange')
plt.xscale('log')
plt.yscale('log')
plt.show()

#fit, trovo parametri 
def S(f, beta, A):
    return A/f**beta

pstart1 = np.array([0,10])
params1, params_covariance1 = optimize.curve_fit(S, tf1f[1:int(tf1.size/2)], np.absolute(tf1[1:tf1.size//2])**2, p0 = [pstart1])
s1_exp = S(tf1f[1:int(tf1.size/2)], params1[0], params1[1])

print('params1: ', params1)
print('params covariance1: ', params_covariance1)

pstart2 = np.array([1,10])
params2, params_covariance2 = optimize.curve_fit(S, tf2f[1:int(tf2.size/2)], np.absolute(tf2[1:tf2.size//2])**2, p0 = [pstart2])
s2_exp = S(tf2f[1:int(tf2.size/2)], params2[0], params2[1])

print('params2: ', params2)
print('params covariance: ', params_covariance2)

#tolgo i primi punti perché sennò il fit viene male
pstart3 = np.array([2,10])
params3, params_covariance3 = optimize.curve_fit(S, tf3f[5:int(tf3.size/2)], np.absolute(tf3[5:tf3.size//2])**2, p0 = [pstart3])
s3_exp = S(tf3f[5:int(tf3.size/2)], params3[0], params3[1])

print('params3: ', params3)
print('params covariance: ', params_covariance3)

#grafici spettro di potenza in funzione delle frequenze + grafico fit

fig,ax = plt.subplots(1,3, figsize = (24,6))

ax[0].plot(tf1f[1:int(tf1.size/2)],np.absolute(tf1[1:tf1.size//2])**2, 'o', markersize=3, color = 'rebeccapurple')
ax[1].plot(tf2f[1:int(tf2.size/2)],np.absolute(tf2[1:tf2.size//2])**2, 'o', markersize=3, color = 'springgreen')
ax[2].plot(tf3f[5:int(tf3.size/2)],np.absolute(tf3[5:tf3.size//2])**2, 'o', markersize=3, color = 'orange')

ax[0].plot(tf1f[1:int(tf1.size/2)],s1_exp, '-', markersize=3, color = 'violet')
ax[1].plot(tf2f[1:int(tf2.size/2)],s2_exp, '-', markersize=3, color = 'green')
ax[2].plot(tf3f[5:int(tf3.size/2)],s3_exp, '-', markersize=3, color = 'red')

ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[2].set_xscale('log')
ax[2].set_yscale('log')

plt.show()
