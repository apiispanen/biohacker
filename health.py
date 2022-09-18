# import xml.etree.ElementTree as ET
import pprint
# with open('Resources/health_export.xml','r') as file:
#     reader = file.read()
import pandas as pd
import xml.etree.ElementTree as ET
from lxml import etree
from lxml import etree
import datetime as dt
parser = etree.XMLParser(remove_comments=True)

# ****** DATA TO READ BELOW *******
health_xml = 'Resources/health_export-916.xml'
# *********

tree = ET.parse(health_xml, parser=parser)
root = tree.getroot()
records = root.findall("Record")

types_of_interest = ['HKQuantityTypeIdentifierStepCount','HKQuantityTypeIdentifierFlightsClimbed', 'HKCategoryTypeIdentifierMindfulSession', 'HKQuantityTypeIdentifierDistanceWalkingRunning', 'HKQuantityTypeIdentifierWalkingDoubleSupportPercentage']

df_data = [] 


print(dt.datetime.strptime('2022-09-13 21:52:05 -0400'[:-6], "%Y-%m-%d %H:%M:%S"))


for x in root:
    try:    
        if x.attrib['type'] in types_of_interest:
            df_data.append([
                x.attrib['type'],
                dt.datetime.strptime(x.attrib['startDate'][:-6], "%Y-%m-%d %H:%M:%S"), 
                dt.datetime.strptime(x.attrib['endDate'][:-6], "%Y-%m-%d %H:%M:%S"),
                x.attrib['unit'], 
                float(x.attrib['value'])
                ])

    except Exception as e:
        try:
            df_data.append([x.attrib['type'],dt.datetime.strptime(x.attrib['startDate'][:-6], "%Y-%m-%d %H:%M:%S"), dt.datetime.strptime(x.attrib['endDate'][:-6], "%Y-%m-%d %H:%M:%S")]) 
        except:
            print("*****FAILED TO UPLOAD****", x.attrib)
            print(str(e))


health_df = pd.DataFrame(df_data, columns=['Type','startDate', 'endDate','unit', 'Value'])


# EXPORT IF DESIRED
# health_df.to_csv('Resources/latest_health_csv.csv')


