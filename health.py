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

print(dt.strptime('2022-09-13 21:52:05 -0400'[:-6], "%Y-%m-%d %H:%M:%S"))

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
health_df['duration'] = health_df['endDate'] - health_df['startDate']

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

print(health_df.columns)

mindful_df = health_df.loc[health_df['Type'] == 'HKCategoryTypeIdentifierMindfulSession']
mindful_df.index = pd.to_datetime(mindful_df['startDate'])
mindful_df = mindful_df.drop(['Type','Value', 'endDate', 'unit', 'startDate'],axis=1)
# ['Type','startDate','duration']

print(mindful_df)