import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#leggo dati da file csv
M0 = pd.read_csv('hit_times_M0.csv')
M1 = pd.read_csv('hit_times_M1.csv')
M2 = pd.read_csv('hit_times_M2.csv')
M3 = pd.read_csv('hit_times_M3.csv')

#istogramma dei tempi
timeM0 = M0['hit_time'].values
plt.hist(timeM0, bins = 70, color = 'teal', ec = 'black')
plt.xlabel('tempo')
plt.show()

#istogramma differenze dei tempi, faccio log 10 per vedere meglio
timeM0_diff = np.diff(timeM0)
mask = timeM0_diff > 0
plt.hist(np.log10(timeM0_diff[mask]), bins = 70, color = 'pink', ec = 'black')
plt.xlabel('differenza tempi scala log10')
plt.show()

#interpretazione grafico: due picchi --> due eventi diversi
