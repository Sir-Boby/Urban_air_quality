import pandas as pd


#Read the raw CSV file from disk and return it as a pandas DataFrame
def load_data(csv_path: str):  
    df_raw = pd.read_csv(csv_path)
    return df_raw

NUM_COLS = [
    "temp_c",
    "rain_mm",
    "humidity_pct",
    "pressure_hpa",
    "wind_speed_mps",
    "wind_direction_deg",
    "pm25",
    "pm10",
]

#Select, rename and clean the columns of the raw dataframe
def preprocess_data(df_raw: pd.DataFrame):

    #select what we need
    cols = [
        'Station_ID',
        'DateTime',
        'Temp_C',
        'Rain_mm',
        'Humidity_%',
        'Pressure_hPa',
        'Wind_Speed_mps',
        'Wind_Direction_deg',
        'PM2.5',
        'PM10'
    ]
    df = df_raw[cols].copy()

    #clean the columns name
    df.columns = (
        df.columns
          .str.strip()
    )

    #rename the columns name
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
    df.rename(columns=rename_map, inplace=True)

    #convert data type of DateTime column
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')

    #sorting numeric value columns
    num_cols = NUM_COLS
    for c in num_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    #Remove duplicated measurements for the same station and timestamp
    subset_dups = ['station_id', 'timestamp']
    df = df.drop_duplicates(subset=subset_dups, keep="last")

    return df

#Compute the fraction of missing values for each numeric column in NUM_COLS
def get_nan_report(df: pd.DataFrame):
    return df[NUM_COLS].isna().mean()
