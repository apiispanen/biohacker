import csv
from statistics import median
import pandas as pd
from datetime import datetime, timedelta

pick_list = []
with open('Resources/pickups.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        pick_list.append(row)

# columns = ['timestamp','Post Date','Description','Category','Type','Amount','Memo']

pickup_df = pd.DataFrame(pick_list[1:], columns=pick_list[0]).drop(['id',' isIgnoredForSleepTime','deviceId'], axis=1)

# Make Session Duration
pickup_df['pickup_duration'] = pd.to_datetime(pickup_df['end']) - pd.to_datetime(pickup_df['start'])
# Now covert it to minutes
pickup_df['pickup_duration'] = pickup_df['pickup_duration'] / pd.Timedelta(minutes=1)
pickup_df['timestamp'] = pd.to_datetime(pickup_df['start'], format="%Y-%m-%d")
pickup_df['pickup_count'] = 1



# MAKE NEW DF FOR SLEEP ANALYSIS
sleep_df = pickup_df[['start', 'end']].copy()
sleep_df['end'] = pd.to_datetime(pickup_df['end']) - timedelta(hours=8)
sleep_df['start'] = pd.to_datetime(pickup_df['start']) - timedelta(hours=8)
sleep_df.index = sleep_df['end'] + timedelta(hours=8)
sleep_df = sleep_df.groupby(pd.Grouper(key="end", freq="D")).agg(
    max=('end', 'max'), min=('start', min)
)

# SPLIT DATA INTO MAX AND MIN DFs, TO MERGE BACK TOGETHER
sleep_df_min = sleep_df[['min']]
sleep_df_min.index = sleep_df_min.index - timedelta(days=1)
sleep_df_max = sleep_df[['max']]


sleep_df = sleep_df_min.merge(sleep_df_max, how='left', on='end')
sleep_df['sleep_minutes'] =  ( pd.to_datetime(sleep_df['min']) - pd.to_datetime(sleep_df['max']) ) / pd.Timedelta(minutes=1) 
sleep_df.reset_index(inplace=True)
sleep_df['end'] = sleep_df['end'].dt.date
sleep_df.index = sleep_df['end']

sleep_df.index = pd.to_datetime(sleep_df.index.rename('timestamp'))


# sleep_df = sleep_df.dropna(axis=0)
sleep_df = sleep_df.drop(['end','min', 'max'], axis=1)




# NOW ADD IT ALL TOGETHER
pickup_df = pickup_df.drop(['start', 'end'], axis=1)

pickup_df = pickup_df.groupby(pd.Grouper(key="timestamp", freq="D")).sum()

pickup_df.reset_index(inplace=True)
pickup_df['timestamp'] = pickup_df['timestamp'].dt.date
pickup_df.index = pd.to_datetime(pickup_df['timestamp'])
pickup_df = pickup_df.drop(['timestamp'],axis=1)
pickup_df['pickup_duration'] = pd.to_numeric(pickup_df['pickup_duration'])
pickup_df = pickup_df.merge(sleep_df, on='timestamp', how='left')
for column in pickup_df.columns:
    pickup_df[column] = pickup_df[column].fillna(pickup_df[column].median()).replace(0,pickup_df[column].median())


print("*********************PICKUP DF *********************", pickup_df) 
