import numpy as np
import pandas as pd

df = pd.read_csv("weather_2012.csv", parse_dates=['Date/Time'])
print(df.head())

temps = df['Temp (C)'].to_numpy()
winds = df['Wind Spd (km/h)'].to_numpy()
vis = df['Visibility (km)'].to_numpy()

print("Temp → mean:", np.nanmean(temps), "min:", np.nanmin(temps), "max:", np.nanmax(temps), "std:", np.nanstd(temps))
print("Wind Speed → mean:", np.nanmean(winds), "max:", np.nanmax(winds))
num_cloudy = np.sum(df['Weather'] == 'Cloudy')
print("Cloudy hours:", num_cloudy)

mask = (winds > 35) & (vis == 25)
print("Extreme windy & clear-vis hours:", np.sum(mask))

df['Month'] = df['Date/Time'].dt.month
pivot = df.pivot_table(index='Month', values='Temp (C)', aggfunc=['mean', 'min', 'max', 'count'])
print(pivot)

grouped = df.groupby('Weather')['Temp (C)'].agg(['mean', 'std', 'count'])
print(grouped.sort_values('count', ascending=False).head())
