# import xml.etree.ElementTree as ET
import pprint
# with open('Resources/health_export.xml','r') as file:
#     reader = file.read()
import pandas as pd
import xml.etree.ElementTree as ET
from lxml import etree
from lxml import etree
parser = etree.XMLParser(remove_comments=True)

health_xml = 'Resources/health_export-916.xml'
tree = ET.parse(health_xml, parser=parser)
root = tree.getroot()
records = root.findall("Record")

types_of_interest = ['HKQuantityTypeIdentifierStepCount','HKQuantityTypeIdentifierFlightsClimbed', 'HKCategoryTypeIdentifierMindfulSession', 'HKQuantityTypeIdentifierDistanceWalkingRunning', 'HKQuantityTypeIdentifierWalkingDoubleSupportPercentage']

df_data = [] 

for x in root:
    try:    
        if x.attrib['type'] in types_of_interest:
            df_data.append([x.attrib['type'],x.attrib['startDate'], x.attrib['endDate'],x.attrib['unit'], x.attrib['value']])
    except Exception as e:
        try:
            df_data.append([x.attrib['type'],x.attrib['startDate'], x.attrib['endDate']]) 
        except:
            print("*****FAILED TO UPLOAD****", x.attrib)
            print(str(e))


health_df = pd.DataFrame(df_data, columns=['Type','startDate', 'endDate','unit', 'Value'])
health_df.to_csv('Resources/latest_health_csv.csv')
# print(health_df)

