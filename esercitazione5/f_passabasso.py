import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import pandas as pd

def pari(num):
    if int(num%2) ==0:
        return 1
    elif int(num%2) !=0:
        return -1
    
def v_in(t_):
    if np.isscalar(t_)==False:
        vv = np.ones(len(t_))
        for i in range(len(t_)):
            vv[i] = pari(t_[i])
        return vv
    elif np.isscalar(t_)==True:
        return(pari(t_))

def dvdt(v_out, tt, RC, v):
    return (v(tt) - v_out)/RC


h = 10/1000
ttt = np.arange(0,10,h)
v0 = 0


vv1 = np.empty((0,0))
vv2 = np.empty((0,0))
vv3 = np.empty((0,0))

RC_= 1
RC_2 = 0.1
RC_3 = 0.01

V_IN = v_in(ttt)
vv1 = integrate.odeint(dvdt, y0 =v0, t = ttt, args=(RC_, v_in))
vv2 = integrate.odeint(dvdt, y0 =v0, t = ttt, args=(RC_2,v_in))
vv3 = integrate.odeint(dvdt, y0 =v0, t = ttt, args=(RC_3,v_in))

plt.plot(ttt, vv1, color = 'springgreen')
plt.plot(ttt, V_IN, color = 'violet')
plt.show()

plt.plot(ttt, vv2, color = 'springgreen')
plt.plot(ttt, V_IN, color = 'violet')
plt.show()

plt.plot(ttt, vv3, color = 'springgreen')
plt.plot(ttt, V_IN, color = 'violet')
plt.show()

tabella = pd.DataFrame()

tabella['tempo'] = ttt
tabella['v_in'] = V_IN
tabella['v_out_1'] = vv1
tabella['v_out_0.1'] = vv2
tabella['v_out_0.01'] = vv3

tabella.to_csv('filtro_passabasso.csv', index=False)


