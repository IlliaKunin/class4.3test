import streamlit as st
import pandas as pd
button= st.button("Click me!")
df= None
if button:
    df= st.file_uploader("Upload a CSV file", type=["csv"])

if df:
    st.dataframe(df)