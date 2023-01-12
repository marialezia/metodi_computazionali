import numpy as np
import pandas as pd
import classi as cl
import funzioni as fz
from tqdm import tqdm

#leggo dati da csv
#ks = pd.read_csv('kansas.csv')
#cl = pd.read_csv('california.csv')
#ny = pd.read_csv('newyork.csv')
il = pd.read_csv('illinois.csv')
mx = pd.read_csv('mexico.csv')

#a partire dai dati mediante l'utilizzo della funzione riempiStato creo degli oggetti stato che contendono i dati di ogni giorno, i giorni ripetuti si è fatta una media associando come errore la deviazione standard tra i valori misurati

#kansas = fz.riempiStato(ks, 'Kansas')
#california = fz.riempiStato(cl, 'California')
#newyork = fz.riempiStato(ny, 'New York')
illinois = fz.riempiStato(il, 'Illinois')
mexico = fz.riempiStato(mx, 'Mexico')

'''
kansasDf = fz.tabStato(kansas)
kansasDf.to_csv('kansasDf.csv')

californiaDf = fz.tabStato(california)
californiaDf.to_csv('californiaDf.csv')

newyorkDf = fz.tabStato(newyork)
newyorkDf.to_csv('newyorkDf.csv') 
'''
illinoisDf = fz.tabStato(illinois)
illinoisDf.to_csv('illinoisDf.csv')

mexicoDf = fz.tabStato(mexico)
mexicoDf.to_csv('mexico.csv')

