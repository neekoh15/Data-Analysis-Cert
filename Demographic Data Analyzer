//You can use this code as guidance but DO NOT COPY/PASTE IT into your proyect, this code has copyrights

import pandas as pd

df = pd.read_csv('adult.data.csv')

series = []
values = []

df[df['sex'] == 'Male']['age'].mean()
df.columns.get_loc('race')
index =list(df.iloc[:,df.columns.get_loc('race')].unique())


for races in index:
    series.append(len(df[df['race'] == races]))
series

result = pd.Series(series, index = index)
result.tolist()

bachs = round(len(df[df['education'] == 'Bachelors'])/len(df) * 100,1)

partials,totals = 0,0
for grades in ['Bachelors', 'Masters','Doctorate']:
    partials += len(df[df['education']== grades][df['salary'] == '>50K'])
    totals += len(df[df['education']== grades])
    
advancedEduAnd50k = round(partials/totals *100,1)

noneHigherGrades = df[df['education'] !='Bachelors'][df['education'] !='Masters'][df['education'] !='Doctorate']

data1 = round(len(noneHigherGrades[noneHigherGrades['salary'] == '>50K'])/len(noneHigherGrades) *100,1)

data2 = round(len(df[df['hours-per-week'] == df['hours-per-week'].min()][df['salary'] == '>50K'])/len(df[df['hours-per-week'] == df['hours-per-week'].min()]) *100,1)

minNumberOfHours = df['hours-per-week'].min()

index =list(df.iloc[:,df.columns.get_loc('native-country')].unique())
earningsPercents = []
for countries in index:
    earningsPercents.append((round(len(df[df['native-country'] == countries][df['salary'] == '>50K'])/len(df[df['native-country'] == countries]) *100,1), countries))

Job = max(earningsPercents)[0]
Country = max(earningsPercents)[1]

indiansJobs = list(df.iloc[:,df.columns.get_loc('occupation')].unique())


for jobs in indiansJobs:
    values.append((len(df[df['occupation'] == jobs]), jobs))
    
IndianJob = max(values)[1]
