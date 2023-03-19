import streamlit as st
import pandas as pd


st.header('Emotion Analysis')


data = pd.read_csv('tweet_emotions.csv')


button_imp = st.button('click to see dataframes')
if button_imp:
    st.dataframe(data.head())

