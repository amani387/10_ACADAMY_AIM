import streamlit as st
import pandas as pd

# Use st.cache_data for caching
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

def process_data(data):
    # Example: Fill missing values
    data.fillna(0, inplace=True)
    return data
