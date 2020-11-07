import pandas as pd
import requests
import datetime
import numpy as np
import streamlit as st


@st.cache(allow_output_mutation=True)
def get_covid_data():
    url = 'https://covidtracking.com/api/v1/states/daily.json'
    data=requests.get(url).json()
    df=pd.DataFrame(data)
    # df['date']=df['date'].astype('str').apply(lambda x: x[:4]+'-'+x[4:6]+'-'+x[6:])
    df.fillna(0, inplace=True)
    df['date']=df['date'].astype('str').apply(lambda x: datetime.date(int(x[:4]), int(x[4:6]), int(x[6:])))
    return df
