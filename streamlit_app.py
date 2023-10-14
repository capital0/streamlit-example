from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

consumption_df=pd.read_csv("consumption.csv")
spotprice_df=pd.read_csv("spotprice.csv")
def clean_and_convert(value):
    if isinstance(value, str):
        return float(value.replace(',', ''))
    else:
        return value
consumption_df["Consumption (MWh)"] = consumption_df["Consumption (MWh)"].apply(clean_and_convert)
def extract_year(date_string):
    year = date_string.split('.')[-1]
    return year
consumption_df['Year'] = consumption_df['Date'].apply(extract_year)
consumption_hourly = consumption_df.groupby(["Hour","Year"])["Consumption (MWh)"].mean().reset_index()

"""
# I love Business Analytics. 
This page is dedicated to my answers to homework questions.
Enjoy the art! I used streamlit to make this work. All code is written by Sinan.
"""


with st.echo(code_location='below'):
    pivot_df = consumption_hourly.pivot(index='Hour', columns='Year', values='Consumption (MWh)')
    fig, ax = pivot_df.plot(kind='bar', stacked=True, figsize=(20, 10))
    plt.title('Average Hourly Consumption YoY')
    plt.xlabel('Hours')
    plt.ylabel('Consumption (MWh)')
    plt.legend(title='Year')
    st.pyplot(fig)