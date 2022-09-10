import streamlit as st
import pandas as pd
import numpy as np


st.title("Biohacker")


# PASTED FROM REGRESSION.PY

# Initial imports
import pandas as pd
import hvplot.pandas
from path import Path
import plotly.express as px
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
from pprint import pprint as pp
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from matplotlib.pyplot import figure