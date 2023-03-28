import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(page_title="Data Frame Visualizer")
file = st.file_uploader("Upload your CSV file", type=["csv"])

st.title("Data Frame Visualizer")

if file is not None:
    df = pd.read_csv(file, sep=";")
    st.title("Data Frame uploaded by user:")
    st.dataframe(df)

    # Create a plot using Matplotlib

    products = df['product'].unique()
    df2 = pd.DataFrame()

    for product in products:
        fig, ax = plt.subplots()
        df2 = df[df["product"] == product]
        ax.plot(df2["timestamp"], df2["mid_price"])
        ax.set_xlabel("timestamp")
        ax.set_ylabel("mid_price")
        ax.set_title(product)

        # Display the plot in Streamlit
        st.pyplot(fig)
