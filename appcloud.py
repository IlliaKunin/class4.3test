import streamlit as st
import pandas as pd
button= st.button("Click me!")
if button:
    df= st.file_uploader("Upload a CSV file", type=["csv"])
    st.dataframe(df.head())
