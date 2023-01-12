import pandas as pd
import numpy as np
import funzioni as fz

#leggo dati da csv
ks = pd.read_csv('kansas.csv')
#cl = pd.read_csv('california.csv')
#ny = pd.read_csv('newyork.csv')
#il = pd.read_csv('illinois.csv')
#mx = pd.read_csv('mexico.csv')

#creo nuove tabelle con dati selezionati 
newKs = fz.filtraDateUguali2(ks)
#newCl = fz.filtrDateUguali2(cl)
#newNy = fz.filtrDateUguali2(ny)
#newIl = fz.filtrDateUguali2(il)
#newMx = fz.filtrDateUguali2(mx)

#salvo le nuove tabelle
newKs.to_csv('newKansas.csv')
#newCl.to_csv('newCalifornia.csv')
#newNy.to_csv('newNewyork.csv')
#newIl.to_csv('newIllinois.csv')
#newMx.to_csv('newMexico.csv')