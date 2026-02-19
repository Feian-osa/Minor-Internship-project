import streamlit as st
import pandas as pd

# Load Excel file
rfm = pd.read_excel("category_summary.xlsx")  # make sure the file is in the same folder as app.py

st.title("Superstore RFM Dashboard")

# Show the dataframe
st.dataframe(rfm)

