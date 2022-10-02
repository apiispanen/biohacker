import csv
import pandas as pd
from datetime import datetime

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
print(pickup_df.head())

# ADD THE LAST PICKUP OF DAY AND FIRST PICKUP OF MORNING, AND GET TOTAL MIN OF SLEEP
# pickup_df['day'] = pickup_df['start'].day
# pickup_df['day']


pickup_df = pickup_df.drop(['start', 'end'], axis=1)

pickup_df = pickup_df.groupby(pd.Grouper(key="timestamp", freq="D")).sum()

pickup_df.reset_index(inplace=True)
pickup_df['timestamp'] = pickup_df['timestamp'].dt.date
pickup_df.index = pd.to_datetime(pickup_df['timestamp'])
pickup_df = pickup_df.drop(['timestamp'],axis=1)
pickup_df['pickup_duration'] = pd.to_numeric(pickup_df['pickup_duration'])

# print(pickup_df)
