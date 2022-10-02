import csv
import pandas as pd

chase_list = []
with open('Resources/chase_history.CSV', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        chase_list.append(row)

columns = ['timestamp','Post Date','Description','Category','Type','Amount','Memo']

chase_df = pd.DataFrame(chase_list[1:], columns=columns)
chase_df = chase_df.drop(['Post Date','Description','Type', 'Memo'], axis=1)
chase_df['Amount'] = pd.to_numeric(chase_df['Amount'])
chase_df = chase_df.groupby(by=['timestamp', 'Category'])['Amount'].sum().unstack()
# for column in chase_df.columns:
#     chase_df = chase_df.rename(columns={column:"chase_"+column.lower()})
chase_df.index = pd.to_datetime(chase_df.index)
chase_df = chase_df.dropna(how='all',axis=1).fillna(0)
chase_df.index = chase_df.index.rename('timestamp')
