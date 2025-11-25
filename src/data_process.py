#import libraries

import pandas as pd


#load the data
CSV_PATH = "../data/raw_data/UrbanAirPollutionDataset.csv"
OUTPUT_PATH = "../data/process_data/weather_stage1_loaded.csv"
def load_data(csv_path: str = CSV_PATH) -> pd.DataFrame:
    """
    Load raw weather data from CSV.

    Parameters
    ----------
    csv_path : str
        Path to the raw CSV file.

    Returns
    -------
    pd.DataFrame
        Raw dataframe.
    """
    df_raw = pd.read_csv(csv_path)
    return df_raw

#print("Shape raw:", df_raw.shape)
#print("Columns raw:", list(df_raw.columns))

#save the original columns name in python list

#original_columns = df_raw.columns.tolist()

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

def preprocess_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Select, rename and clean columns of the raw dataframe.
    """

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
          #.str.replace(r"\s+", "_", regex=True)
          #.str.replace(r"[^0-9a-zA-Z_\.]", "", regex=True)
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

    #check for duplicated data
    subset_dups = ['station_id', 'timestamp']
    df = df.drop_duplicates(subset=subset_dups, keep="last")

    return df


def get_nan_report(df: pd.DataFrame) -> pd.Series:
    """
    Compute fraction of missing values for numeric columns.
    """
    return df[NUM_COLS].isna().mean()
