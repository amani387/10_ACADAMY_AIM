
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from app.utils import load_data, process_data  # Import from utils.py

# Load the dataset
data = load_data("C:/Users/kingsta/Desktop/KIFIYA 10 ACADAMY/10_ACADAMY_AIM/Streamlet-dashboard/data/benin-malanville.csv")
  # Adjust the file path if necessary
data = process_data(data)

# Title and Description
st.title("Data Insights Dashboard By Amanuel Nega ")
st.markdown("This dashboard provides interactive data visualizations to explore insights according to my given task .")

# Sidebar for Navigation
st.sidebar.header("Dashboard Navigation")
options = st.sidebar.radio("Select a section:", ["Overview", "Visualization", "Interactive Insights"])

# Overview Section
if options == "Overview":
    st.header("Dataset Overview")
    st.write(data.head())
    st.write("Basic Statistics:")
    st.write(data.describe())

# Visualization Section
elif options == "Visualization":
    st.header("Data Visualizations")
    column = st.selectbox("Select a column to visualize:", data.columns)
    st.line_chart(data[column])

# Interactive Insights
elif options == "Interactive Insights":
    st.header("Custom Insights")
    slider_value = st.slider("Select range for filtering data:", 0, 100, (10, 50))
    filtered_data = data[(data.iloc[:, 0] >= slider_value[0]) & (data.iloc[:, 0] <= slider_value[1])]
    st.write(filtered_data)
