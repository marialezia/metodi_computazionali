import pandas as pd
import funzioni as fz

data = pd.read_csv('pollution_us_2005_2007.csv')
statecode = data['State Code'].values


indexCal = fz.index(statecode, 6)
indexMex = fz.index(statecode, 80)
indexKan = fz.index(statecode, 20)
indexNY = fz.index(statecode, 36)
indexIll = fz.index(statecode, 17)


california = fz.tab(indexCal, data, statecode, 6)
mexico = fz.tab(indexMex, data, statecode, 80)
kansas = fz.tab(indexKan, data, statecode, 20)
newyork= fz.tab(indexNY, data, statecode, 36)
illinois = fz.tab(indexIll, data, statecode, 17)

california.to_csv('california.csv', index = False)
mexico.to_csv('mexico.csv', index = False)
kansas.to_csv('kansas.csv', index = False)
newyork.to_csv('newyork.csv', index = False)
illinois.to_csv('illinois.csv', index = False)

