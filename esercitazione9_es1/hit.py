import numpy as np
import matplotlib.pyplot as plt
import sys, os
import pandas as pd
import reco

#definisco funzione che legge la tabella, crea un array della lunghezza delle colonne riempito con hit nulli (questo per non fare append che di solito è lento), fa un ciclo for della lunghezza delle colonne in cui mette nell'array l'hit prendendo l'elemento delle colonne i-esimo, restituisce l'array di hit

def hit_arr(tabella):
    
    mod = tabella['mod_id'].values
    sens = tabella['det_id'].values
    time = tabella['hit_time'].values
    arr = np.full(len(mod), reco.Hit(0,0,0)) 
    
    for i in range(len(mod)):
        arr[i] = reco.Hit(mod[i], sens[i], time[i])
    
    return arr

#leggo dati da file csv
M0 = pd.read_csv('hit_times_M0.csv')
M1 = pd.read_csv('hit_times_M1.csv')
M2 = pd.read_csv('hit_times_M2.csv')
M3 = pd.read_csv('hit_times_M3.csv')



hit_M0 = hit_arr(M0)
hit_M1 = hit_arr(M1)
hit_M2 = hit_arr(M2)
hit_M3 = hit_arr(M3)



'''
aa = np.arange(10)
bb = np.array([aa**2 for a in aa])

bb = np.array([aa**2 for a in aa if a > 5])


 for i in range(len(self.hit)):
            if self.hit[i] > hit:
                self.hit = np.insert(self.hit, i, hit)
'''

