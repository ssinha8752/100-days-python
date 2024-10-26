import csv

import pandas as pd

with open ("./.venv/weather.csv") as datafile:
    data=csv.reader(datafile)
    temp=[]
    for row in data:
        temp.append(int(row[1]) if row[1]!='temp' else "")
    print(temp)

df=pd.read_csv("weather_data.csv")
print(df['temp'])
print(df['temp'].to_dict())
print(df['temp'].mean())
print(df['temp'].max())
print(df[df.day=='Monday'])
print(df[df.temp==max(df['temp'])])
mon=df[df.day=='Monday']
print(mon.condition)
print((mon.temp[0]*9/5)+32)