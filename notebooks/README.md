# Exploratory Data Analysis (EDA) on Solar Radiation Data
# Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on solar radiation measurement data collected from various locations. The dataset includes solar radiation measurements (Global Horizontal Irradiance, Direct Normal Irradiance, Diffuse Horizontal Irradiance), environmental factors (temperature, humidity, wind speed, etc.), and sensor data (cleaning, soiling events).

The goal is to understand key trends and patterns within the dataset to identify high-potential regions for solar energy investments.

# Objective

. Perform statistical analysis and visualizations to understand solar radiation patterns.

. Analyze the relationship between solar radiation and environmental factors.

. Provide insights that can support business decisions for sustainable solar energy investments.

# Data Overview

. The dataset consists of several columns:

. Timestamp: Date and time of each observation.

. GHI (W/m²): Global Horizontal Irradiance (solar radiation on a horizontal surface).

. DNI (W/m²): Direct Normal Irradiance (solar radiation on a surface perpendicular to the sun’s rays).

. DHI (W/m²): Diffuse Horizontal Irradiance (solar radiation that does not come directly from the sun).

. ModA (W/m²), ModB (W/m²): Sensor measurements.

. Tamb (°C): Ambient temperature.

. RH (%): Relative humidity.

. WS (m/s), WSgust (m/s): Wind speed and gust speed.

. BP (hPa): Barometric pressure.

. Cleaning: Indicates whether a cleaning event occurred (1 = cleaned, 0 = not cleaned).

. Precipitation (mm/min): Precipitation rate.

. TModA (°C), TModB (°C): Module temperatures.

. Comments: Any additional notes (mostly null in the dataset).

# Requirements

To run the code in this project, make sure to install the following Python packages:

. pandas

. matplotlib

. seaborn

. scipy

. jupyter (optional, for running in Jupyter Notebooks)

. You can install the required packages using: 

      pip install -r requirements.txt 

you can run by typing 
 
      jupyter notebook eda.ipynb
