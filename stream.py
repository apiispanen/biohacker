import streamlit as st
import pandas as pd
import numpy as np
from pull_sheet import data
from datetime import datetime as dt
# from plot import plt
import plotly.express as px
import plotly.graph_objects as go


st.title("Biohackerz")

st.subheader('Tracking Mood over time')

# DATE_COLUMN = [datum['timestamp'] for datum in data]
# MOOD_COLUMN = [datum['mood'] for datum in data]

# print(data)

fig = px.scatter(data, x="timestamp", y="mood", text="mood", title='Drew has a bad mood', trendline='ols', trendline_color_override='green')
fig.data[0].update(mode='markers+lines', fill='toself')
fig.update_traces(textposition='top left')
st.plotly_chart(fig, use_container_width=True)

st.write("pensi")
