Urban Air Quality – exploratory analysis

This repository contains my final project for the "Coding for Data Science and Data Management" course.
The goal is to practise a small end-to-end data workflow on an air-pollution dataset:
data loading, cleaning, exploratory analysis, visualisation, and a simple web app.

Dataset used: UrbanAirNet – Urban Air Quality and Weather Dataset (Kaggle)
Kaggle link: https://www.kaggle.com/datasets/ziya07/urbanairnet-urban-air-quality-and-weather-dataset

The dataset provides hourly PM2.5, PM10 and basic meteorological variables
(temperature, humidity, pressure, rain, wind speed) over one year.

Project structure

## Project structure

```text
Urban_air_quality/
├─ data/
│  ├─ raw_data/
│  │   └─ UrbanAirPollutionDataset.csv   # original Kaggle CSV (NOT in GitHub)
│  └─ process_data/
│      └─ weather_stage1_loaded.csv      # cleaned dataset (tracked in GitHub)
├─ notebooks/
│  ├─ time_patterns.ipynb        # PM patterns vs season, month, hour, weekday
│  └─ weather_vs_pollution.ipynb # correlations, NumPy stats, scatter plots
├─ output/
│  └─ *.png                      # figures exported from the notebooks
├─ src/
│  ├─ data_process.py            # functions for loading and cleaning data
│  ├─ main.py                    # command-line cleaning pipeline
│  └─ web_app.py                 # simple Streamlit dashboard
├─ .gitignore
├─ requirements.txt
└─ README.md
```

The cleaned dataset data/process_data/weather_stage1_loaded.csv is included
so the notebooks and the web app can run directly.

The raw Kaggle CSV is not included.
To fully reproduce the cleaning step, download the dataset from Kaggle and place:

data/raw_data/UrbanAirPollutionDataset.csv

If you only want to explore the results, you can use the cleaned file directly.

Data processing (src/)
data_process.py

Core data-processing functions:

load_data(csv_path)

read a CSV into a pandas DataFrame.

preprocess_data(df_raw)

select relevant columns (station, timestamp, weather, PM2.5, PM10)

clean and rename columns to snake_case

parse timestamp and sort chronologically

convert numeric columns to numeric dtypes

drop duplicate rows for the same station and timestamp

get_nan_report(df)

compute the fraction of missing values for the main numeric variables
(temperature, rain, humidity, pressure, wind speed, PM2.5, PM10).

File paths are not hard-coded here; they are passed in from main.py
and web_app.py.

main.py

Small linear pipeline:

Load raw data from
data/raw_data/UrbanAirPollutionDataset.csv (if present).

Clean and standardise the data with preprocess_data.

Print shapes of the raw and cleaned DataFrames.

Report the time coverage of the cleaned dataset.

Print a NaN report using get_nan_report.

Save the cleaned DataFrame to:
data/process_data/weather_stage1_loaded.csv.

Run from the project root:

python src/main.py

If the raw file is missing, you can still rely on the already-cleaned CSV
included in the repo.

Exploratory analysis (notebooks/)
1- time_patterns.ipynb

Explores how PM2.5 and PM10 change across different time scales:

create time features from timestamp:

month, season, hour, weekday

compute average PM2.5 and PM10 by:

season (Winter, Spring, Summer, Autumn)

month (1–12)

hour of day (0–23)

day of week (0–6 → Monday–Sunday)

visualise these patterns with bar and line plots.

Several figures from this notebook are exported to output/.

2- weather_vs_pollution.ipynb

Examines relationships between weather and air pollution:

select only weather + PM columns

compute and inspect a correlation matrix

use NumPy to:

convert PM2.5 values to arrays,

compute basic statistics (mean, standard deviation),

build a PM2.5 / PM10 ratio with np.where

create scatter plots:

PM2.5 vs temperature

PM2.5 and PM10 vs temperature

PM2.5 / PM10 vs wind speed

PM2.5 vs rain

PM2.5 vs PM2.5/PM10 ratio

The correlations are weak and the scatter plots do not show strong structure,
which is consistent with a synthetic or heavily smoothed dataset.

The focus is on relative patterns (how PM changes with time and weather),
not on detailed health-risk assessment.

Streamlit web app (src/web_app.py)

A small Streamlit dashboard that reuses the functions from data_process.py.

Data loading logic

If data/process_data/weather_stage1_loaded.csv does not exist:

load the raw CSV (if available),

clean it with preprocess_data,

save to data/process_data/weather_stage1_loaded.csv.

If the cleaned file does exist (typical case in this repo):

load it directly, parsing the timestamp column.

Views

Time-pattern view:

preview of the cleaned dataset (df.head())

PM2.5 and PM10 averages by season, month, hour and weekday

Weather–pollution view:

correlation matrix for weather + PM variables

scatter plots of PM vs temperature, wind speed and rain

Run from the project root:

streamlit run src/web_app.py

Requirements

Main libraries:

pandas – data manipulation and time handling

numpy – basic numerical computations on PM values

matplotlib – plots in the notebooks and in the Streamlit app

streamlit – web app for interactive exploration

Install dependencies:

pip install -r requirements.txt

Notes

The UrbanAirNet data from Kaggle are likely synthetic or strongly
pre-processed; temporal patterns and weather–PM relationships are flatter than
in real urban measurements.

The cleaned file data/process_data/weather_stage1_loaded.csv is tracked in
this repository and is enough to run the notebooks and the web app.
