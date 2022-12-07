import numpy as np
import sys

#definisco funzione somma primi n numeri e somma prime n radici numeri

def somma_n(n):
    numeri = np.arange(n+1)
    return np.sum(numeri)

def somma_rad_n(n):
    radici = np.sqrt(np.arange(n+1))
    return np.sum(radici)
