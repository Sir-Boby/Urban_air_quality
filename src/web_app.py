import streamlit as st
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# project paths (independent from where you run the code)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

CSV_PATH = DATA_DIR / "raw_data" / "UrbanAirPollutionDataset.csv"
OUTPUT_PATH = DATA_DIR / "process_data" / "weather_stage1_loaded.csv"


def get_clean_data():
    output_path = Path(OUTPUT_PATH)

    if not output_path.exists():
        df_raw = load_data(CSV_PATH)
        df_clean = preprocess_data(df_raw)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df_clean.to_csv(output_path, index=False)
    else:
        df_clean = pd.read_csv(output_path, parse_dates=["timestamp"])

    return df_clean

def show_time_patterns(df):
    st.subheader("Time patterns of PM2.5 and PM10")

    df = df.copy()
    df["month"] = df["timestamp"].dt.month

    def get_season(m: int) -> str:
        if m in [12, 1, 2]:
            return "Winter"
        elif m in [3, 4, 5]:
            return "Spring"
        elif m in [6, 7, 8]:
            return "Summer"
        else:
            return "Autumn"

    df["season"] = df["month"].apply(get_season)
    df["hour"] = df["timestamp"].dt.hour
    df["weekday"] = df["timestamp"].dt.dayofweek  # 0 = Mon ... 6 = Sun

    st.markdown("**Average PM by season**")
    season_mean = df.groupby("season")[["pm25", "pm10"]].mean()
    st.dataframe(season_mean)

    fig, ax = plt.subplots(figsize=(6, 4))
    season_mean.plot(kind="bar", ax=ax)
    ax.set_ylabel("Concentration (µg/m³)")
    ax.set_xlabel("Season")
    ax.set_title("Average PM2.5 and PM10 by season")
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("**Monthly averages**")
    monthly_mean = df.groupby("month")[["pm25", "pm10"]].mean()
    st.line_chart(monthly_mean)

    st.markdown("**Hourly averages**")
    hourly_mean = df.groupby("hour")[["pm25", "pm10"]].mean()
    st.line_chart(hourly_mean)

    st.markdown("**Weekday averages (0 = Mon, 6 = Sun)**")
    weekday_mean = df.groupby("weekday")[["pm25", "pm10"]].mean()
    st.line_chart(weekday_mean)

def show_weather_relations(df):
    st.subheader("Weather vs air pollution")

    cols = [
        "temp_c",
        "rain_mm",
        "humidity_pct",
        "pressure_hpa",
        "wind_speed_mps",
        "pm25",
        "pm10",
    ]
    df_weather = df[cols].copy()

    st.markdown("**Correlation matrix**")
    corr = df_weather.corr()
    st.dataframe(corr)

    st.markdown("**PM vs temperature**")
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(df["temp_c"], df["pm25"], alpha=0.2, label="PM2.5")
    ax.scatter(df["temp_c"], df["pm10"], alpha=0.2, label="PM10")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Concentration (µg/m³)")
    ax.set_title("PM vs temperature")
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("**PM vs wind speed**")
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(df["wind_speed_mps"], df["pm25"], alpha=0.2, label="PM2.5")
    ax.scatter(df["wind_speed_mps"], df["pm10"], alpha=0.2, label="PM10")
    ax.set_xlabel("Wind speed (m/s)")
    ax.set_ylabel("Concentration (µg/m³)")
    ax.set_title("PM vs wind speed")
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("**PM2.5 vs rain**")
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(df["rain_mm"], df["pm25"], alpha=0.2)
    ax.set_xlabel("Rain (mm)")
    ax.set_ylabel("PM2.5 (µg/m³)")
    ax.set_title("PM2.5 vs rain")
    plt.tight_layout()
    st.pyplot(fig)

def main():
    st.title("""Urban Air Quality
    Design and develop : Mohammad Movahedinia
    """)

    df = get_clean_data()

    st.write("Preview of the cleaned dataset:")
    st.dataframe(df.head())
    show_time_patterns(df)
    show_weather_relations(df)

main()
