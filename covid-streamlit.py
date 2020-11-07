import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np
import datetime
from coviddata import get_covid_data

st.title('US COVID 19 dashboard')

# @st.cache
df=get_covid_data()

state_selected=''
top_states=df[df['date']==datetime.date.today()].sort_values(by='positive',ascending=False)['state'].tolist()[:3]
states=df.state.unique().tolist()
state_selected = st.sidebar.multiselect('Select state to view/compare', states, default=top_states)
days = (datetime.date.today() - datetime.date(2020,1,22)).days
number_of_days = st.sidebar.slider("Number of days", 0, days, days)

start_date = (datetime.date.today() - datetime.timedelta(number_of_days))

df.fillna(0)
df['current positive']=df['positive']-df['recovered']

@st.cache
def get_column(df, state_selected, column, start_date):
    if state_selected:
        pos=df[df.state.isin(state_selected) & (df.date>=start_date)].groupby(['date','state']).sum()[column].reset_index()
    return pos.fillna(0)

def create_charts(df, state_selected, start_date):
    if not state_selected:
        st.markdown('## Please select a state')
        return
    field=st.selectbox('Select Field',('Current Positive' ,'New Positives','New Deaths', 'Total Positive', 'Total Deaths'))

    if 'Current' in field:
        check=1
        add='current'
    elif 'Total' in field:
        check=0
        add='cumulative'
    else:
        check=-1
        add='new'

    l=['positive', 'death']
    var={}

    for x in l:

        column=x
        if x in field.lower():

            if add=='current':
                column='current positive'
            elif add=='new':
                column=x+'Increase'

            st.subheader(x.capitalize() + ' ' + add)
            var[column]=get_column(df, state_selected, column, start_date)
            # st.write(pos)
            fig=px.line(var[column], x='date',y=f'{column}',color='state', template='simple_white', height=600,width=900)
            st.plotly_chart(fig)
            # st.altair_chart(alt.Chart(var[x],width=800, height=500).mark_line().encode(x='date',y=f'{x}:Q',color='state:N', tooltip=['date','state']))
            # st.line_chart(var[x])

create_charts(df,state_selected, start_date)
