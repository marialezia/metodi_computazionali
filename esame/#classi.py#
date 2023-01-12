import numpy as np
import pandas as pd
import sys, os

class Date:
    '''oggetto di tipo date ha informazioni su:
    - data 
    - country code
    - site num
    - city
    - SO2, SO2 err
    - nO2, nO2 err
    -  O3, O3 err
    - CO, CO err

    def __init__(self):
        self.date = '           '
        self.cCode = 0
        self.city = '           '
        self.so2 = 0
        self.so2Err = 0
        self.no2 = 0
        self.no2Err = 0
        self.co = 0
        self.coErr = 0
        self.o3 = 0
        self.o3Err = 0
'''
    def __init__(self, day, cCode, siteNum, city, so2, so2err, no2, no2err, co, coerr, o3, o3err):
        self.day = day
        self.cCode = cCode
        self.city = city
        self.siteNum = siteNum
        self.so2 = so2
        self.so2Err = so2err
        self.no2 = no2
        self.no2Err = no2err
        self.co = co
        self.coErr = coerr
        self.o3 = o3
        self.o3Err = o3err

    def __str__(self):
        return 'Dato registrato in data ' + self.day + '\n nella città ' + self.city + '\n site Num: ' + str(self.siteNum) + '\n media SO2: ' + str(self.so2) + ' + - ' + str(self.so2Err) + '\n media CO2: ' + str(self.no2) + ' + - '+  str(self.no2Err) + '\n media CO: ' + str(self.co) + ' + - '+ str(self.coErr) +  '\n media O3: ' + str(self.o3) + ' + - '+ str(self.o3Err)

    
class Stato:
    '''oggetto di tipo stato ha informazioni: 
    - array con tutti i dati 
    - numero di dati'''
    
    def __init__(self, nome):
        self.data = np.empty(0)
        self.num = len(self.data)
        self.name = nome

    def addDate(self, dato):
        self.data = np.append(self.data, dato)
        self.num = len(self.data)
