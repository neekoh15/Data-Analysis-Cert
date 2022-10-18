//You can use this code as guidance but DO NOT COPY/PASTE IT into your proyect, this code has copyrights

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('medical_examination.csv')

overweight= []
filter = []

for x in range(len(df)):
    if df['weight'][x]/pow((df['height'][x]/100),2) >25:
        overweight.append(1)
    else: overweight.append(0)
df['overweight'] = overweight

df.loc[df.cholesterol <= 1, 'cholesterol'] = 0
df.loc[df.cholesterol > 1, 'cholesterol'] = 1
df.loc[df.gluc <= 1, 'gluc'] = 0
df.loc[df.gluc > 1, 'gluc'] = 1

newDf = pd.melt(df, id_vars = ['cardio'], value_vars = ['active', 'alco', 'cholesterol', 'gluc','overweight','smoke'])

graph = sns.catplot(data = newDf , hue = 'value', x = 'variable', kind = 'count', col = 'cardio')
graph.set(ylabel= 'total')

newDf = df.copy()

newDf.drop(newDf[newDf['ap_lo'] > newDf['ap_hi']].index, inplace= True)
newDf.drop(newDf[newDf['height'] < newDf['height'].quantile(0.025)].index, inplace= True)
newDf.drop(newDf[newDf['height'] > newDf['height'].quantile(0.975)].index, inplace= True)
newDf.drop(newDf[newDf['weight'] < newDf['weight'].quantile(0.025)].index, inplace= True)
newDf.drop(newDf[newDf['weight'] > newDf['weight'].quantile(0.975)].index, inplace= True)
newDf.rename(columns = {'sex':'gender'},inplace = True)

npDf = newDf.to_numpy()

corr = np.corrcoef(npDf, rowvar = False)
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True

with sns.axes_style("dark"):
    f, ax = plt.subplots(figsize=(10, 7))
    ax = sns.heatmap(corr, yticklabels= [x for x in newDf], xticklabels= [x for x in newDf], mask=mask, vmax = 0.3, annot = True, fmt =".1f", square=True, center = 0, linewidths=.5)
