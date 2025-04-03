import streamlit as st
import pandas as pd
df= pd.read_csv("climate_change_dataset.csv")
st.write("# Welcome to the AppCloud!")
st.dataframe(df.head())