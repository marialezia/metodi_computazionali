import pandas as pd
import numpy as np
import classi as cl
import sys, os
from tqdm import tqdm

def contaStati(arr, sc):
    conta = 0
    for i in arr:
        if i == sc:
            conta = conta+1
    return conta

def contaDateUguali(days):
    conta = 1
    for i in range(len(days)-1):
        if days[i] != days[i+1]:
        	conta = conta +1
    return conta

def index(arr, sc):
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

def tab(indici, data, arr, sc):
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
'''
def filtraDateUguali(df):
    date = df['Date Local']
    num = contaDateUguali(date)
    newDf = pd.DataFrame()
    dates = np.full([num], '               ')
    siteNum = np.empty([num])
    city = np.full([num], '                ')
    countryCode = np.empty([num])
    so2 = np.empty([num])
    so2Err = np.empty([num])
    no2 = np.empty([num])
    no2Err = np.empty([num])
    co = np.empty([num])
    coErr = np.empty([num])
    o3 = np.empty([num])
    o3Err = np.empty([num])
                           
    dateUguali = np.array(0)
    for i in tqdm(range(len(date)-1)):
        if date[i] == date[i+1]: #confronto la data con la successiva
            dateUguali = np.append(dateUguali, i+1) #metto gli indici delle righe della tabella in cui ho la stessa data, confrontando con il successivo
            if i+1 == len(date): #aggiungo la condizione se sono arrivato all'ultimo elemento
                so2 = np.zeros([len(dateUguali)])
                co = np.zeros([len(dateUguali)])
                no2 = np.zeros([len(dateUguali)])
                o3 = np.zeros([len(dateUguali)])
                k=0
                for j in dateUguali:
                    no2[k] = df['NO2'][j]
                    so2[k] = df['SO2'][j]
                    co[k] = df['CO'][j]
                    o3[k] = df['O3'][j]
                    k = k+1
                dates[i] = date[i]
                siteNum[i] = df['Site Num'][i]
                city[i] = df['City'][i]
                countryCode[i] = df['CountryCode'][i]
                so2[i] = np.mean(so2)
                so2Err[i] = np.std(so2)
                no2[i] = np.mean(no2)
                no2Err[i] = np.std(no2)
                co[i] = np.mean(co)
                coErr[i] = np.std(co)
                o3[i] = np.mean(o3)
                o3Err[i] = np.std(o3)
        else:
            So2 = np.zeros([len(dateUguali)])
            Co = np.zeros([len(dateUguali)])
            No2 = np.zeros([len(dateUguali)])
            O3 = np.zeros([len(dateUguali)])
            k=0
            for j in dateUguali:
                No2[k] = df['NO2'][j]
                So2[k] = df['SO2'][j]
                Co[k] = df['CO'][j]
                O3[k] = df['O3'][j]
                k = k+1
            dates[i] = date[i]
            siteNum[i] = df['Site Num'][i]
            city[i] = df['City'][i]
            countryCode[i] = df['CountryCode'][i]
            so2[i] = np.mean(So2)
            so2Err[i] = np.std(So2)
            no2[i] = np.mean(No2)
            no2Err[i] = np.std(No2)
            co[i] = np.mean(Co)
            coErr[i] = np.std(Co)
            o3[i] = np.mean(O3)
            o3Err[i] = np.std(O3)
            if i+1== len(date):
                dates[i+1] = date[i+1]
                siteNum[i+1] = df['Site Num'][i+1]
                city[i+1] = df['City'][i+1]
                countryCode[i+1] = df['CountryCode'][i+1]
                so2[i+1] = np.mean(so2)
                so2Err[i+1] = np.std(so2)
                no2[i+1] = np.mean(no2)
                no2Err[i+1] = np.std(no2)
                co[i+1] = np.mean(co)
                coErr[i+1] = np.std(co)
                o3[i+1] = np.mean(o3)
                o3Err[i+1] = np.std(o3)
    newDf['Date Local'] = dates
    newDf['CountryCode'] = countryCode
    newDf['City'] = city
    newDf['Site Num'] = siteNum
    newDf['so2'] = so2
    newDf['no2'] = no2
    newDf['co'] = co
    newDf['o3'] = o3
    newDf['so2Err'] = so2Err
    newDf['no2Err'] = no2Err
    newDf['coErr'] = coErr
    newDf['o3Err'] = o3Err
    return newDf'''

def filtraDateUguali2(df):
    date = df['Date Local']
    num = contaDateUguali(date)
    newDf = pd.DataFrame(index = range(num), columns=['Date Local', 'Site Num', 'City', 'CountryCode', 'so2', 'so2Err', 'no2', 'no2Err', 'co', 'coErr', 'o3', 'o3Err'])                           
    dateUguali = np.array(0)
    p = 0
    for i in tqdm(range(len(date)-1)):
        if date[i] == date[i+1]: #confronto la data con la successiva
            dateUguali = np.append(dateUguali, i+1) #metto gli indici delle righe della tabella in cui ho la stessa data, confrontando con il successivo
            if i+1 == len(date): #aggiungo la condizione se sono arrivato all'ultimo elemento
                k=0
                so2 = np.zeros([len(dateUguali)])
                co = np.zeros([len(dateUguali)])
                no2 = np.zeros([len(dateUguali)])
                o3 = np.zeros([len(dateUguali)])
                for j in dateUguali:
                    no2[k] = df['NO2'][j]
                    so2[k] = df['SO2'][j]
                    co[k] = df['CO'][j]
                    o3[k] = df['O3'][j]
                    k = k+1
                newDf['Date Local'][p] = date[i]
                newDf['Site Num'][p] = df['Site Num'][i]
                newDf['City'][p] = df['City'][i]
                newDf['CountryCode'][p] = df['CountryCode'][i]
                newDf['so2'][p] = np.mean(so2)
                newDf['so2Err'][p] = np.std(so2)
                newDf['no2'][p] = np.mean(no2)
                newDf['no2Err'][p] = np.std(no2)
                newDf['co'][p] = np.mean(co)
                newDf['coErr'][p] = np.std(co)
                newDf['o3'][p] = np.mean(o3)
                newDf['o3Err'][p] = np.std(o3)
        else:
            so2 = np.zeros([len(dateUguali)])
            co = np.zeros([len(dateUguali)])
            no2 = np.zeros([len(dateUguali)])
            o3 = np.zeros([len(dateUguali)])
            k=0
            for j in dateUguali:
                no2[k] = df['NO2'][j]
                so2[k] = df['SO2'][j]
                co[k] = df['CO'][j]
                o3[k] = df['O3'][j]
                k = k+1
            newDf['Date Local'][p] = date[i]
            newDf['Site Num'][p] = df['Site Num'][i]
            newDf['City'][p] = df['City'][i] 
            newDf['CountryCode'][p] = df['CountryCode'][i]
            newDf['so2'][p] = np.mean(so2)
            newDf['so2Err'][p] = np.std(so2)
            newDf['no2'][p] = np.mean(no2)
            newDf['no2Err'][p] = np.std(no2)
            newDf['co'][p] = np.mean(co)
            newDf['coErr'][p] = np.std(co)
            newDf['o3'][p] = np.mean(o3)
            newDf['o3Err'][p]= np.std(o3)

            p = p+1
            if i+1== len(date):
                newDf['Date Local'][p+1]= date[i+1]
                newDf['Site Num'][p+1]= df['Site Num'][i+1]
                newDf['City'][p+1]  = df['City'][i+1]
                newDf['CountryCode'][p+1]= df['CountryCode'][i+1]
                newDf['so2'][p+1] = df['SO2'][i+1]
                newDf['so2Err'][p+1] = 0
                newDf['no2'][p+1] = df['NO2'][i+1]
                newDf['no2Err'][p+1] = 0
                newDf['co'][p+1] = df['CO'][i+1]
                newDf['coErr'][p+1] = 0
                newDf['o3'][p+1] = df['O3'][i+1]
                newDf['o3Err'][p+1] = 0
    return newDf

    
def creoStato(df, name):
    stato = cl.State(name)
    for i in tqdm(range(len(df['CountryCode']))):
        dato = cl.Date(df['Date Local'][i], df['CountryCode'].values[i], df['Site Num'].values[i], df['City'][i], df['so2'].values[i], df['so2Err'].values[i], df['no2'].values[i], df['no2Err'].values[i], df['co'].values[i], df['coErr'].values[i], df['o3'].values[i], df['o3Err'].values[i])
        stato.addDate(dato)
    return stato
                

def riempiStato(df, name):
    date = df['Date Local']
    dateUguali = np.array(0)
    stato = cl.Stato('Kansas')
    #ciclo for da 0 alla lunghezza delle colonne -1
    for i in tqdm(range(len(df['City'])-1)):
        if date[i] == date[i+1]: #confronto la data con la successiva
            dateUguali = np.append(dateUguali, i+1) #metto gli indici delle righe della tabella in cui ho la stessa data, confrontando con il successivo
            if i+1 == len(df['City']): #aggiungo la condizione se sono arrivato all'ultimo elemento
                so2 = np.zeros([len(dateUguali)])
                co = np.zeros([len(dateUguali)])
                no2 = np.zeros([len(dateUguali)])
                o3 = np.zeros([len(dateUguali)])
                k=0
                for j in dateUguali:
                    no2[k] = df['NO2'][j]
                    so2[k] = df['SO2'][j]
                    co[k] = df['CO'][j]
                    o3[k] = df['O3'][j]
                    k = k+1
                dato = cl.Date(date[i], df['CountryCode'][i], df['Site Num'][i], df['City'][i], np.mean(so2), np.std(so2), np.mean(no2), np.std(no2), np.mean(co), np.std(co), np.mean(o3), np.std(o3))
                stato.addDate(dato)
        else: 
            so2 = np.zeros([len(dateUguali)])
            co = np.zeros([len(dateUguali)])
            no2 = np.zeros([len(dateUguali)])
            o3 = np.zeros([len(dateUguali)])
            k=0
            for j in dateUguali:
                no2[k] = df['NO2'][j]
                so2[k] = df['SO2'][j]
                co[k] = df['CO'][j]
                o3[k] = df['O3'][j]
                k = k+1
            dato = cl.Date(date[i], df['CountryCode'][i], df['Site Num'][i], df['City'][i], np.mean(so2), np.std(so2), np.mean(no2), np.std(no2), np.mean(co), np.std(co), np.mean(o3), np.std(o3))
            stato.addDate(dato)
            dateUguali = np.empty(0)
            dateUguali = np.append(dateUguali, i+1)
            stato.addDate(dato)
            if i+1 == len(df['City']): #aggiungo la condizione se sono arrivato all'ultimo elemento
                dato = cl.Date(date[i+1], df['CountryCode'][i+1], df['Site Num'][i+1], df['City'][i+1], df['SO2'][i+1], 0, df['NO2'][i+1], 0, df['CO'][i+1], 0, df['O3'][i+1], 0)
                stato.addDate(dato)
    return stato

def tabStato(stato):
    arr = stato.data
    newDf = pd.DataFrame(index= range(len(arr)), columns = ['day', 'cCode', 'city', 'nSite', 'so2', 'so2Err', 'no2', 'no2Err', 'co', 'coErr', 'o3', 'o3Err'])
    for i in tqdm(range(len(arr))):
        newDf['day'][i]= arr[i].day
        newDf['cCode'][i] = arr[i].cCode
        newDf['city'][i] = arr[i].city
        newDf['nSite'][i] = arr[i].siteNum
        newDf['so2'][i] = arr[i].so2
        newDf['so2Err'][i] = arr[i].so2Err
        newDf['no2'][i] = arr[i].no2
        newDf['no2Err'][i] = arr[i].no2Err
        newDf['o3'][i] = arr[i].o3
        newDf['o3Err'][i] = arr[i].o3Err
        newDf['co'][i] = arr[i].co
        newDf['coErr'][i] = arr[i].coErr
    return newDf