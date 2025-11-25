from data_process import (
    CSV_PATH,
    OUTPUT_PATH,
    load_data,
    preprocess_data,
    get_nan_report,
)


def main() -> None:
    # 1) load raw data
    df_raw = load_data(CSV_PATH)
    print(f"Raw shape: {df_raw.shape}")

    # 2) preprocess / clean
    df = preprocess_data(df_raw)
    print(f"Cleaned shape: {df.shape}")

    # 3) compute and print NaN report
    nan_report = get_nan_report(df)
    print("\nFraction of missing values per numeric column:")
    print(nan_report)

    # 4) save cleaned dataframe
    # df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nCleaned data saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
