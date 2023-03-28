import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Data Frame Visualizer")
file = st.file_uploader("Upload your CSV file", type=["csv"])

st.title("Data Frame Visualizer")

if file is not None:
    df = pd.read_csv(file, sep=";")
    st.title("Data Frame uploaded by user:")
    st.dataframe(df)
