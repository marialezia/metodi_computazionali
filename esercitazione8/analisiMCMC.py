import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import corner
import emcee
from scipy.optimize import minimize
from scipy import stats


#definisco funzione

def flusso(p, E):
    m,b,alfa,mu,sigma = p
    return m*E+b+alfa*np.exp(-(E-mu)**2/(2*sigma**2))

# logaritmo della funzione di verosimiglianza (log likelihood)
def loglike(p, E, y, yerr):
    return -0.5 * np.sum(((y - flusso(p, E))/yerr) ** 2)

# logaritmo della distribuzione di probabilità  a priori (prior) per i paramtri liberi.

def logprior(p):
    m,b,alfa,mu,sigma = p
    if ( -2< m < 2 and  8 < b < 12 and -6.5 < alfa < -3.5 and 2.75 <mu < 6.75 and -1.5 < sigma <2.5 ):
        return 0.0
    return -np.inf

# logaritmo della distribuzione di probabilità totale 
# log(prob) = log(prior) + log(likelihood)
def lnprob(p, E, y, yerr):
    lp = logprior(p)
    if np.isfinite(lp):
        return lp + loglike(p, E, y, yerr) 
    return -np.inf


#leggo dati da csv e grafico

dati = pd.read_csv('absorption_line.csv')
E = dati['E']
f = dati['f']
f_err = dati['ferr']

plt.errorbar(E, f, yerr = f_err, fmt = '-o', color = 'rebeccapurple')
#plt.show()


#parametri di prova per vedere se la funzione ha senso
pprova = np.array([-0.2,10,-5.5,4.75,0.5])
fprova = flusso(pprova, E)

plt.plot(E, fprova, color = 'violet')
plt.errorbar(E, f, yerr = f_err, fmt = '-o', color = 'rebeccapurple')
#plt.show()

# numero di walker
nw = 32

# condizioni iniziali 
c_iniziali = pprova
ndim_acc = len(c_iniziali)

# definisco parametri iniziali per i walker come piccola variazione random attorno
#  ai paramtri iniziali stabiliti 
p0 = np.array(c_iniziali)  +0.1*np.random.randn(nw, ndim_acc)

# definisco il sampler di emcee
sampler_acc = emcee.EnsembleSampler(nw, ndim_acc, lnprob, args=(E, f, f_err))

# Lancio campionamento per 2000 passi
print("Running production...")
sampler_acc.run_mcmc(p0, 100, progress=True);


# Grafico campionamenti per i parametri liberi
fig, axes = plt.subplots(ndim_acc, figsize=(10, 9), sharex=True)
samples_acc = sampler_acc.get_chain()

for i in range(ndim_acc):
    ax = axes[i]
    ax.plot(samples_acc[:, :, i], "k", alpha=0.3)
    ax.set_xlim(0, len(samples_acc))
    ax.yaxis.set_label_coords(-0.1, 0.5)

axes[-1].set_xlabel("numero passi");

plt.show()


# Grafico dati con alcuni campionamenti dei parametri
plt.errorbar(E, f, yerr=f_err, fmt="ok", capsize=0)
plt.xlabel('t [s]')
plt.ylabel('d [m]')
plt.show()

'''
# Grafico 50 campionamenti posterior .
samples_acc = sampler_acc.flatchain
for s in samples_acc[np.random.randint(len(samples_acc), size=50)]:
    plt.plot(time, model_acc(s, time), color="orange", alpha=0.3)

# Escludo i primi 200 passi dalla valutazione 
flat_samples_acc = sampler_acc.get_chain(discard=200, thin=15, flat=True)


# Grafico dei dati e dei campionamenti escludendo i primi 200 passi
plt.errorbar(time, accdata, yerr=sigmay, fmt="ok", capsize=0)
plt.xlabel('t [s]')
plt.ylabel('d [m]')

# Plot 50 posterior samples.
for s in flat_samples_acc[np.random.randint( len(flat_samples_acc), size=50)]:
    plt.plot(time, model_acc(s, time), color="orange", alpha=0.3)
'''
