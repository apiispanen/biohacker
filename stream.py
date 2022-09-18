from turtle import fillcolor
import streamlit as st
import pandas as pd
import numpy as np
from pull_sheet import data
from datetime import datetime as dt
# from plot import plt
import plotly.express as px
import plotly.graph_objects as go
from health import health_df
from datetime import datetime as dt
import tk-tools

st.title("Biohackerz")

st.subheader('Tracking Mood over time')

# DATE_COLUMN = [datum['timestamp'] for datum in data]
# MOOD_COLUMN = [datum['mood'] for datum in data]

# print(data)

fig = px.scatter(data, x="timestamp", y="mood", text="mood", title='Drew has a bad mood', trendline='ols', trendline_color_override='green')
fig.data[0].update(mode='markers+lines', fill='toself')
fig.update_traces(textposition='top left')

st.plotly_chart(fig, use_container_width=True)



# NEW CHART FOR HEALTH

steps_health_df = health_df.loc[(health_df['Type'] == 'HKQuantityTypeIdentifierStepCount' )&
    (health_df['endDate'] > dt(2022, 9, 8))
    ].set_index('endDate').groupby(pd.Grouper(freq='D')).sum()
# st.write(steps_health_df)

fig = px.scatter(steps_health_df, x=steps_health_df.index, y="Value", title='Health Data Test: Total Steps')
fig.data[0].update(mode='markers', fill='toself')
fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

fig.update_traces(textposition='top left')

st.plotly_chart(fig, use_container_width=True)



# MEXT


steps_health_df = health_df.loc[(health_df['Type'] == 'HKQuantityTypeIdentifierFlightsClimbed' )&
    (health_df['endDate'] > dt(2022, 9, 8))
    ].set_index('endDate').groupby(pd.Grouper(freq='D')).sum()
# st.write(steps_health_df)

fig = px.scatter(steps_health_df, x=steps_health_df.index, y="Value", title='Health Data Test: Total Flights')
fig.data[0].update(mode='markers', fill='toself')
fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

fig.update_traces(textposition='top left')

st.plotly_chart(fig, use_container_width=True)


# NEXT PLOT

# MEXT


steps_health_df = health_df.loc[(health_df['Type'] == 'HKQuantityTypeIdentifierDistanceWalkingRunning' )&
    (health_df['endDate'] > dt(2022, 9, 8))
    ].set_index('endDate').groupby(pd.Grouper(freq='D')).sum()
# st.write(steps_health_df)

fig = px.scatter(steps_health_df, x=steps_health_df.index, y="Value", title='Health Data Test: Dist Walking/Running')
fig.data[0].update(mode='markers', fill='toself')
fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

fig.update_traces(textposition='top left')

st.plotly_chart(fig, use_container_width=True)


# MEXT


steps_health_df = health_df.loc[(health_df['Type'] == 'HKQuantityTypeIdentifierWalkingDoubleSupportPercentage' )&
    (health_df['endDate'] > dt(2022, 9, 8))
    ].set_index('endDate').groupby(pd.Grouper(freq='D')).mean()
# st.write(steps_health_df)

fig = px.scatter(steps_health_df, x=steps_health_df.index, y="Value", title='Health Data Test: Standing-Sitting')
fig.data[0].update(mode='markers', fill='toself')
fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

fig.update_traces(textposition='top left')

st.plotly_chart(fig, use_container_width=True)
# st.write("testing")
