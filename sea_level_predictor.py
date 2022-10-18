//You can use this code as guidance but DO NOT COPY/PASTE IT into your proyect, this code has copyrights

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')

for x in list(df.columns[2:]):
    del df[x]

df = df.rename(columns =  {'CSIRO Adjusted Sea Level' : 'Level'})

extension = list(range(2014,2051))

x_axis = df['Year']
sea_level = df['Level']

prediction = linregress(x_axis, sea_level)

dfPredict = df.copy()

for x in extension:
    dfPredict = dfPredict.append(pd.DataFrame({'Year':[x]}), ignore_index = True )

dfPredict2 = df.copy()
dfPredict2.drop(df[df['Year'] < 2000].index, inplace =True)

prediction2 = linregress(dfPredict2['Year'], dfPredict2['Level'])



for x in extension:
    dfPredict2 = dfPredict2.append(pd.DataFrame({'Year':[x]}), ignore_index = True )


#print(dfPredict2)
#print(dfPredict)
fig, ax = plt.subplots(1,1, figsize = (7,5))

plt.scatter(x_axis, sea_level)
plt.plot(dfPredict['Year'], prediction.intercept + prediction.slope*dfPredict['Year'])
plt.plot(dfPredict2['Year'], prediction2.intercept + prediction2.slope*dfPredict2['Year'])
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
