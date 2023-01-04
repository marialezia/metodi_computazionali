import pandas as pd
import indici as ind

data = pd.read_csv('pollution_us_2005_2007.csv')
statecode = data['State Code'].values


indexCal = ind.Index(statecode, 6)
indexMex = ind.Index(statecode, 80)
indexKan = ind.Index(statecode, 20)
indexNY = ind.Index(statecode, 36)
indexIll = ind.Index(statecode, 17)


california = ind.Tab(indexCal, data, statecode, 6)
mexico = ind.Tab(indexMex, data, statecode, 80)
kansas = ind.Tab(indexKan, data, statecode, 20)
newyork= ind.Tab(indexNY, data, statecode, 36)
illinois = ind.Tab(indexIll, data, statecode, 17)

california.to_csv('california.csv', index = False)
mexico.to_csv('mexico.csv', index = False)
kansas.to_csv('kansas.csv', index = False)
newyork.to_csv('newyork.csv', index = False)
illinois.to_csv('illinois.csv', index = False)

