# PASTED FROM REGRESSION.PY

# PLOTS REGRESSION ON MATPLOTLIB

# Initial imports
import pandas as pd
import hvplot.pandas
from path import Path
import plotly.express as px
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# from sklearn.decomposition import PCA
# from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib import style
# import seaborn as sns
from pprint import pprint as pppip 

from matplotlib.pyplot import figure

from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.dates

from pull_sheet import data

y_axis = [line['mood'] for line in data]
x_axis = [line["timestamp"] for line in data]
dates = matplotlib.dates.date2num(x_axis)
plt.plot_date(dates,y_axis)
plt.title('How Do You Feel?')
plt.xlabel('Timestamp')
plt.ylabel('Mood (1-5)')
# plt.gcf().autofmt_xdate()


# plt.show()
