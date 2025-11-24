Project overview

This project analyzes air quality in Vienna using an open dataset from Kaggle that combines meteorological variables (temperature, rainfall, wind, humidity, pressure) with air pollution indicators (PM2.5 and PM10).
The goal is to clean the raw data, build a reproducible analysis pipeline in Python, and answer a set of concrete questions about temporal patterns of pollution and its relationship with weather conditions.

The project is implemented in Python using pandas for data manipulation, numpy for numerical computations, and matplotlib/seaborn for visualization. All code and steps are organized so that the analysis can be rerun from raw data to final figures.

Data

Source: Kaggle – urban air pollution and weather data for Vienna

Main variables:

Meteorological: temp_c, rain_mm, humidity_pct, pressure_hpa, wind_speed_mps, wind_direction_deg

Air quality: pm25, pm10

Time and station info: timestamp, station_id

Raw data are stored under data/raw_data/, and cleaned/processed data are written to data/process_data/ by the preprocessing scripts.

Research questions

The analysis focuses on the following questions:

Seasonal and monthly patterns

In which months or seasons are PM2.5 and PM10 concentrations higher?

Is there a clear seasonal pattern in air pollution levels?

Meteorological drivers of pollution

How are PM2.5 and PM10 related to:

air temperature (temp_c),

rainfall (rain_mm),

wind speed (wind_speed_mps)?

Do higher wind speeds or rainy conditions tend to reduce particulate pollution?

Daily cycle

How does pollution vary over the course of the day?

Are PM levels higher during typical traffic hours (e.g. morning and evening)?

Weekday vs weekend

Are there systematic differences in pollution between weekdays and weekends, possibly linked to human activity and traffic?

(If the dataset contains multiple monitoring stations, we also compare average pollution levels between stations.)

Methods and workflow

Data loading and cleaning

Load the raw Kaggle CSV.

Select relevant columns, standardize column names, parse timestamps, convert numeric fields, and remove duplicates (station_id + timestamp).

Save a cleaned version of the dataset to data/process_data/weather_stage1_loaded.csv.

Descriptive statistics

Compute basic statistics (mean, min, max, quantiles) for PM2.5, PM10 and meteorological variables.

Inspect completeness of the data (fraction of missing values).

Scientific computing

Resample the time series to daily/monthly averages to study trends.

Group data by season, month, hour of day, and weekday/weekend to compare pollution levels across time scales.

Compute correlation coefficients between meteorological variables and pollutants to quantify their relationships.

Visualization

Time series plots of PM2.5 and PM10 to show temporal patterns.

Scatter plots (e.g. PM2.5 vs temperature, wind speed, rainfall) to visualize relationships between weather and pollution.

Bar charts for mean pollution by season, hour of day, and weekday/weekend.

Together, these steps provide a reproducible pipeline from raw data to cleaned data, numerical summaries, and visual insights about how air quality in Vienna varies over time and how it is influenced by meteorological conditions.

Note:
The Kaggle dataset used in this project appears to be synthetic or pre-generated (it does not display typical monthly or seasonal variability found in real-world air quality measurements).
Despite this limitation, a full data-analysis pipeline is implemented, including cleaning, scientific computations, and visualization techniques typically applied to real air-quality datasets.