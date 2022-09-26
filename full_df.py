# SCRIPT DEDICATED TO COMBINING ALL DFS TOGETHER

from pull_sheet import daily_data
from health import health_df
from chase_pull import chase_df
from weather_pull import weather_df
from pickup_pull import pickup_df
import pandas as pd

# COMMENT / UNCOMMENT BELOW TO TOGGLE WHICH DBs ARE ADDED
full_df = daily_data.merge(chase_df, how='left', on='timestamp')
full_df = full_df.drop(['timestamp-1','timestamp-2','timestamp-3'],axis=1)

print(full_df)

full_df = full_df.merge(weather_df, how='left', on='timestamp')
full_df = full_df.merge(health_df, how='left', on="timestamp")
full_df = full_df.merge(pickup_df, how="left", on="timestamp")
full_df['pickup_duration'] = pd.to_numeric(full_df['pickup_duration'])

full_df = full_df.fillna(0).drop(['pickup_duration'], axis=1)
print(full_df) 