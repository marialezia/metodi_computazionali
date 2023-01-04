import pandas as pd
import numpy as np
import sys, os
from tqdm import tqdm

def ContaStati(arr, sc):
    conta = 0
    for i in arr:
        if i == sc:
            conta = conta+1
    return conta

def Index(arr, sc):
    copia = arr.copy()
    nStati = ContaStati(arr, sc)
    indici = np.empty([nStati])
    j = 0
    for i in range(len(arr)):
        if arr[i] == sc:
            indici[j] = i
            j = j+1
    return indici

#mi restituisce un array con gli indici della tabella che devo estrarre per quello stato

def Tab(indici, data, arr, sc):
    nStati = ContaStati(arr, sc)
    df = pd.DataFrame()
    dates = np.full([nStati], '               ')
    siteNum = np.empty([nStati])
    city = np.full([nStati], '                ')
    countryCode = np.empty([nStati])
    so2 = np.empty([nStati])
    no2 = np.empty([nStati])
    co = np.empty([nStati])
    o3 = np.empty([nStati])

    for i in tqdm(range(len(indici))):
        j = indici[i]
        dates[i] = data['Date Local'][j]
        countryCode[i] = data['County Code'][j]
        siteNum[i] = data['Site Num'][j]
        city[i] = data['City'][j]
        so2[i] = data['SO2 Mean'][j]
        no2[i] = data['NO2 Mean'][j]
        co[i] = data['CO Mean'][j]
        o3[i] = data['O3 Mean'][j]

    df['Date Local'] = dates
    df['CountryCode'] = countryCode
    df['City'] = city
    df['Site Num'] = siteNum
    df['SO2'] = so2
    df['NO2'] = no2
    df['CO'] = co
    df['O3'] = o3
    return df
    
