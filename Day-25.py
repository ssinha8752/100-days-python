import csv

import pandas as pd

with open ("./.venv/weather.csv") as datafile:
    data=csv.reader(datafile)
    temp=[]
    for row in data:
        temp.append(int(row[1]) if row[1]!='temp' else "")
    print(temp)

df=pd.read_csv("weather_data.csv")
print(df['temp']) #to get temp column
print(df['temp'].to_dict()) #conver into dictionary
print(df['temp'].mean()) #find mean of all temp
print(df['temp'].max()) #find max of all temp
print(df[df.day=='Monday']) # row where day is monday
print(df[df.temp==max(df['temp'])]) #row where day has max temp
mon=df[df.day=='Monday']
print(mon.condition) #getting condition for monday
print((mon.temp[0]*9/5)+32) #converting temp for c to F