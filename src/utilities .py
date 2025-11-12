#import libraries

import pandas as pd


#load the data
df = pd.read_csv('data/raw_data/UrbanAirPollutionDataset.csv')

#select what we need

cols = [
    'Station_ID', 'DateTime',
    'Temp_C', 'Rain_mm',
    'Humidity_%', 'Pressure_hPa',
    'Wind_Speed_mps', 'Wind_Direction_deg',
    'PM2.5', 'PM10'
]

df_selected = df[cols].copy()


rename_map = {
    'Station_ID': 'station_id',
    'DateTime': 'timestamp',
    'Temp_C': 'temp_c',
    'Rain_mm': 'rain_mm',
    'Humidity_%': 'humidity_pct',
    'Pressure_hPa': 'pressure_hpa',
    'Wind_Speed_mps': 'wind_speed_mps',
    'Wind_Direction_deg': 'wind_direction_deg',
    'PM2.5': 'pm25',
    'PM10': 'pm10'
}

df_selected.rename(columns=rename_map, inplace=True)

#convert data type of Data Time column, from object to datetime64
df_selected['timestamp'] = pd.to_datetime(df_selected['timestamp'])
df_selected = df_selected.sort_values('timestamp').set_index('timestamp')

#sorting numeric value

num_cols = [
        'temp_c', 'rain_mm', 'humidity_pct', 'pressure_hpa', 'wind_speed_mps',
        'wind_direction_deg', 'pm25', 'pm10',
]
for c in num_cols:
    if c in df_selected.columns:
        df_selected[c] = pd.to_numeric(df_selected[c], errors='coerce')

df_selected.head()
#df.tail()
#df.info()
#df.dtypes
#df_selected.dtypes

#print(df_selected.head())