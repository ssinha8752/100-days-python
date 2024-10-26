import csv

import pandas as pd

with open ("./.venv/weather.csv") as datafile:
    data=csv.reader(datafile)
    temp=[]
    for row in data:
        temp.append(int(row[1]) if row[1]!='temp' else "")
    print(temp)

df=pd.read_csv("weather_data.csv")
print(df)