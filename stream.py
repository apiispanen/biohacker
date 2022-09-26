
from urllib.request import HTTPDefaultErrorHandler
import streamlit as st
import pandas as pd
import numpy as np
# from pull_sheet import dates_visited_gym
from datetime import datetime as dt
# from plot import plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn import linear_model
import statsmodels.api as sm



# IMPORT THE ONLY GIVEN DB
from pull_sheet import daily_data, dates_visited_gym

full_df = daily_data

st.title("Biohackerz")
st.subheader('Tracking Mood over time')

# POSITIONING OF THESE DBS ARE CRTICIAL TO THE BELOW FUNCTIONS. PLEASE ONLY ADJUST LABELS HERE 
library_names = ['Health', 'Phone Pickup Data', 'Chase Financial', 'Weather']
time_lags = ['timestamp','timestamp-1', 'timestamp-2', 'timestamp-3']


def mood_graph(x, y='mood', data = full_df, trace = dates_visited_gym):
    fig = px.scatter(data, x=x, y="mood", text="mood", title='Drew has a bad mood', trendline='ols', labels={"timestamp":"Date",
        'mood':'Mood (1-5)'
    }, trendline_color_override='green')
    fig.data[0].update(mode='markers+lines', fill='toself')
    fig.update_traces(textposition='top left')
    fig.add_trace(go.Bar(x=trace,
        y=[5 for entry in trace], text="Gym Visit",
        opacity=.15, width=1000*3600*24, name="Gym Visits"
    ))
    st.plotly_chart(fig, use_container_width=True)

def pick_database(options, lag_option, full_df=full_df):
    full_df = full_df.reset_index()   
    for option in options:
        # HEALTH
        if option == library_names[0]: 
            from health import health_df           
            health_df.index.names = [lag_option]
            full_df = full_df.merge(health_df, how='left', on=lag_option)
        # PHONE PICKUP
        if option == library_names[1]: 
            from pickup_pull import pickup_df
            pickup_df.index.names = [lag_option]
            full_df = full_df.merge(pickup_df, how="left", on=lag_option)            
        # CHASE
        if option == library_names[2]: 
            from chase_pull import chase_df
            chase_df.index.names = [lag_option]
            full_df = full_df.merge(chase_df, how='left', on=lag_option)
        # WEATHER
        if option == library_names[3]: 
            from weather_pull import weather_df
            weather_df.index.names = [lag_option]           
            full_df = full_df.merge(weather_df, how='left', on=lag_option)

    full_df.index = full_df['timestamp']
    # full_df["matched_date"] = full_df[lag_option] 
    full_df = full_df.drop(time_lags, axis=1)
    full_df = full_df.fillna(0)    
    return full_df

def make_mlr(x,y):
    # with sklearn
    regr = linear_model.LinearRegression()
    regr.fit(x, y)

    print('Intercept: \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)

    # with statsmodels
    x = sm.add_constant(x) # adding a constant
    
    model = sm.OLS(y, x).fit()
    predictions = model.predict(x) 
    
    print_model = model.summary()
    return print_model

# MAKE THE VISUAL ELEMENTS

mood_graph(x=full_df.index)



# LAG SELECTOR
lag_option = st.selectbox(
    'Time Lag',
    (time_lags))

st.write('You selected:', lag_option)

# DATABASE SELECTOR
options = st.multiselect(
    'What databases should we draw from?',
    library_names,
    [library_names[0], library_names[1]])


st.write('Results:')
full_df = pick_database(options, lag_option)


st.write(full_df)


final_regression = st.multiselect(
    'What variables should we run MLR on?',
    [column for column in full_df.columns[1:]],
    [column for column in full_df.columns[1:]])
# st.write(final_regression)
st.write(make_mlr(x = full_df[final_regression], y=full_df['mood']))
