from tqdm import tqdm
import pandas as pd
import numpy as np

data = pd.read_csv('pollution_us_2005_2007.csv')
arr = np.empty([0])
for i in tqdm(range(10)):
    arr = np.append(arr, data['County Code'][i])

arr2 = np.empty([10])
for i in tqdm(range(10)):
    arr2[i] = data['County Code'][i]

print(arr, arr2)
