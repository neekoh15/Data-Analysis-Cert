//You can use this code as guidance but DO NOT COPY/PASTE IT into your proyect, this code has copyrights

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#Parte A:

df = pd.read_csv('fcc-forum-pageviews.csv')

topTrunc = round(len(df)*0.975)
botTrunc = round(len(df)*0.025)
print(topTrunc, botTrunc)

df = df.sort_values(by = 'value', ignore_index = True)

df.drop(df[df.index < botTrunc].index, inplace = True)
df.drop(df[df.index >= topTrunc].index, inplace = True)

df = df.sort_values(by = 'date', ignore_index = True)
df = df.set_index('date')

ticks = list(df.index)

plt.figure(figsize=(10,3))
plt.plot(df, 'r')

plt.ylabel('Page Views')
plt.xlabel('Date')
plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize = 9)
plt.xticks([ticks[i] for i in range(len(ticks)) if i%240 == 0])
plt.show()


#drawBar
#Parte B:
    
df = pd.read_csv('fcc-forum-pageviews.csv')

topTrunc = round(len(df)*0.975)
botTrunc = round(len(df)*0.025)

df = df.sort_values(by = 'value', ignore_index = True)

df.drop(df[df.index < botTrunc].index, inplace = True)
df.drop(df[df.index >= topTrunc].index, inplace = True)

df = df.sort_values(by = 'date', ignore_index = True)
df = df.set_index('date')

df['date2'] = df.index
df[['year','month','day']] = df['date2'].str.split('-', 2, expand=True)
#df.sort_values(by = 'value',ignore_index = True)
df.rename(columns = {'date2': 'date'}, inplace = True)
df.set_index('date', inplace=True, drop = True)

df_bar = pd.DataFrame({'year': df['year'].unique()})

monthsList = [ 'January', 'February','March', 'April','May','June','July','August','September','October','November','December'] 
aux = []
i = 0

for month in list(df.sort_values(by = 'month')['month'].unique()):
    for year in list(df['year'].unique()):
        try:
            aux.append(round(df[df['year'] == year ][df['month'] == month].value.mean()))
        except ValueError:
            aux.append(0)
    df_bar[monthsList[i]] = (aux)
    aux = []
    i += 1
       
test = df_bar.copy()
x_pos = list(range(0, 2*len(test),2))
wd = 0.05
i= 0
fig, axs = plt.subplots(1,1, figsize = (7,5))
for x in list(test.columns[1:]):
    plt.bar([x+i*wd for x in x_pos], df_bar[x], width = wd, label = x)
    i+=1

plt.xlabel('Years')
plt.ylabel('Average Page Views')
plt.xticks([x+i*wd/2 for x in x_pos], test.year.values, rotation = 90)
plt.legend(loc='upper left', fontsize=7)

#boxplot
#Parte C:
    
df = pd.read_csv('fcc-forum-pageviews.csv')

topTrunc = round(len(df)*0.975)
botTrunc = round(len(df)*0.025)
print(topTrunc, botTrunc)

df = df.sort_values(by = 'value', ignore_index = True)

df.drop(df[df.index < botTrunc].index, inplace = True)
df.drop(df[df.index >= topTrunc].index, inplace = True)

df = df.sort_values(by = 'date', ignore_index = True)
df = df.set_index('date')

df['date2'] = df.index
df[['year','month','day']] = df['date2'].str.split('-', 2, expand=True)
#df.sort_values(by = 'value',ignore_index = True)
df.rename(columns = {'date2': 'date'}, inplace = True)
df.set_index('date', inplace=True, drop = True)
df.rename(columns = {'value': 'Page Views'}, inplace = True)

df = df.sort_values(by = 'month')

for x in df['month'].unique():
    df.loc[df.month == x, 'month'] = monthsList[int(x)-1][:3]
    
fig, axs = plt.subplots(1,2, figsize=(12,5))
a = sns.boxplot(df.sort_values(by = 'year'), y = 'Page Views', x = 'year', ax=axs[0])
b = sns.boxplot(df, y= 'Page Views', x = 'month', ax=axs[1])
a.set_title('Year-wise Box Plot (Trend)')
b.set_title('Month-wise Box Plot (Seasonality)')
a.set(xlabel= 'Year')
b.set(xlabel ='Month')

fig.show()    
