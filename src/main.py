from data_process import (

    load_data,
    preprocess_data,
    get_nan_report,
)

#Paths to raw and processed data files (relative to the project root)
CSV_PATH = "data/raw_data/UrbanAirPollutionDataset.csv"
OUTPUT_PATH = "data/process_data/weather_stage1_loaded.csv"

def main():
    # 1) load raw data
    df_raw = load_data(CSV_PATH)
    print(f"Raw shape: {df_raw.shape}")

    # 2) preprocess / clean
    print("\nFirst 5 rows of the raw data:")
    print(df_raw.head())

    # 3) preprocess / clean
    df = preprocess_data(df_raw)
    print(f"Cleaned shape: {df.shape}")
    
    # 2) preprocess / clean
    print("\nFirst 5 rows of the clean data:")
    print(df.head())

    # 4) preprocess / clean
    time_min = df["timestamp"].min()
    time_max = df["timestamp"].max()
    print(f"Time range after cleaning: {time_min.date()}  -->  {time_max.date()}")

    # 5) compute and print NaN report
    nan_report = get_nan_report(df)
    print("\nFraction of missing values per numeric column:")
    print(nan_report)

    # 6) save cleaned dataframe
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nCleaned data saved to: {OUTPUT_PATH}")

    main()
