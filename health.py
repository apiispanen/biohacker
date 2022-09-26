# import xml.etree.ElementTree as ET
import pprint
# with open('Resources/health_export.xml','r') as file:
#     reader = file.read()
import pandas as pd
import xml.etree.ElementTree as ET
from lxml import etree
from lxml import etree
from datetime import datetime as dt
parser = etree.XMLParser(remove_comments=True)

# ****** DATA TO READ BELOW *******
health_xml = 'Resources/health_export-923.xml'
# *********

tree = ET.parse(health_xml, parser=parser)
root = tree.getroot()
records = root.findall("Record")

types_of_interest = ['HKQuantityTypeIdentifierStepCount','HKQuantityTypeIdentifierFlightsClimbed', 'HKCategoryTypeIdentifierMindfulSession', 'HKQuantityTypeIdentifierDistanceWalkingRunning', 'HKQuantityTypeIdentifierWalkingDoubleSupportPercentage']

df_data = [] 


for x in root:
    try:    
        if x.attrib['type'] in types_of_interest:
            df_data.append([
                x.attrib['type'],
                dt.strptime(x.attrib['startDate'][:-6], "%Y-%m-%d %H:%M:%S"), 
                dt.strptime(x.attrib['endDate'][:-6], "%Y-%m-%d %H:%M:%S"),
                x.attrib['unit'], 
                float(x.attrib['value'])
                ])

    except Exception as e:
        try:
            df_data.append([x.attrib['type'],dt.strptime(x.attrib['startDate'][:-6], "%Y-%m-%d %H:%M:%S"), dt.strptime(x.attrib['endDate'][:-6], "%Y-%m-%d %H:%M:%S")]) 
        except:
            # print("*****FAILED TO UPLOAD****", x.attrib)
            # print(str(e))
            continue

health_df = pd.DataFrame(df_data, columns=['Type','startDate', 'endDate','unit', 'Value'])
# Duration made, convert it to minutes (since Mindful is the only one using it)
health_df['duration'] = health_df['endDate'] - health_df['startDate']
health_df['duration'] = health_df['duration'] / pd.Timedelta(minutes=1)

# health_df = health_df.drop(['startDate'], axis=1)

# EXPORT IF DESIRED
# health_df.to_csv('Resources/latest_health_csv.csv')

flights_df = health_df.loc[(health_df['Type'] == 'HKQuantityTypeIdentifierFlightsClimbed' )&
    (health_df['endDate'] > dt(2022, 9, 8))
    ].set_index('endDate').groupby(pd.Grouper(freq='D')).sum()
# st.write(steps_health_df)

steps_health_df = health_df.loc[(health_df['Type'] == 'HKQuantityTypeIdentifierStepCount' )&
    (health_df['endDate'] > dt(2022, 9, 8))
    ].set_index('endDate').groupby(pd.Grouper(freq='D')).sum()
# st.write(steps_health_df)

walkrun_df = health_df.loc[(health_df['Type'] == 'HKQuantityTypeIdentifierDistanceWalkingRunning') &
    (health_df['endDate'] > dt(2022, 9, 8))
    ].set_index('endDate').groupby(pd.Grouper(freq='D')).sum()
# st.write(steps_health_df)

standing_df = health_df.loc[(health_df['Type'] == 'HKQuantityTypeIdentifierWalkingDoubleSupportPercentage' )&
    (health_df['endDate'] > dt(2022, 9, 8))
    ].set_index('endDate').groupby(pd.Grouper(freq='D')).mean()
# st.write(steps_health_df)

mindful_df = health_df.loc[health_df['Type'] == 'HKCategoryTypeIdentifierMindfulSession']
mindful_df.index = pd.to_datetime(mindful_df['startDate'])
mindful_df = mindful_df.drop(['Type','Value', 'endDate', 'unit', 'startDate'],axis=1)
# ['Type','startDate','duration']

# Change Around the mindful data to make it clean
health_df.loc[health_df["Type"]=='HKCategoryTypeIdentifierMindfulSession' , "Value"] = health_df["duration"]
health_df.loc[health_df["Type"]=='HKCategoryTypeIdentifierMindfulSession' , "unit"] = "duration"
health_df = health_df.drop(['duration'],axis=1)
health_df['startDate'] = pd.to_datetime(health_df['startDate'])

health_df = health_df.groupby(by=['Type', 'startDate',"unit"]).sum()
health_df.reset_index(inplace=True)
health_df.index = health_df['startDate']
health_df = health_df.groupby(by=['Type',pd.Grouper(key='startDate', axis=0, freq='D')]).sum()

health_df = health_df.groupby(by=['startDate','Type' ])['Value'].sum().unstack().fillna(0)

health_df.index = health_df.index.rename("timestamp")
health_df = health_df.rename(columns={"HKCategoryTypeIdentifierMindfulSession": "mindful_min", 
                                "HKQuantityTypeIdentifierDistanceWalkingRunning": "walk_run",
                               "HKQuantityTypeIdentifierFlightsClimbed": 'total_flights_climbed',
                               'HKQuantityTypeIdentifierStepCount':'total_steps',
                               'HKQuantityTypeIdentifierWalkingDoubleSupportPercentage':'standing_percent'})
