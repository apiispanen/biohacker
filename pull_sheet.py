from datetime import datetime as dt
import numpy as np
#### GET MY GOOGLE SHEET DATA
import sys
import subprocess


# CHECK DEPENDENCIES:
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'gspread'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'tk-tools'])

# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'oauth2client'])

# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'plotly'])

# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'statsmodels'])





scope =  ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive.file', "https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/drive"]

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# KEEP CREDS.JSON, AS IT SERVES THE AUTH KEY FOR THIS PROJECT
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("How do you feel").sheet1
data = sheet.get_all_records()

#### UNCOMMENT ABOVE ^^^^ 

# IF YOU JUST WANT SAMPLE DATA, UNOMMENT BELOW:
# data = [{'Timestamp': '9/8/2022 0:33:02', 'How Do You Feel?': 4}, {'Timestamp': '9/8/2022 0:51:30', 'How Do You Feel?': 5}, {'Timestamp': '9/8/2022 10:04:27', 'How Do You Feel?': 3}, {'Timestamp': '9/9/2022 7:40:20', 'How Do You Feel?': 3}, {'Timestamp': '9/9/2022 11:45:42', 'How Do You Feel?': 3}, {'Timestamp': '9/9/2022 13:56:57', 'How Do You Feel?': 2}, {'Timestamp': '9/9/2022 19:03:37', 'How Do You Feel?': 4}, {'Timestamp': '9/9/2022 21:31:01', 'How Do You Feel?': 3}, {'Timestamp': '9/10/2022 11:44:07', 'How Do You Feel?': 3}]
# END OF SAMPLE 


y_axis = [line['How Do You Feel?'] for line in data]
x_axis = [dt.strptime(line["Timestamp"], "%m/%d/%Y %H:%M:%S") for line in data]
data = [{'timestamp':x_axin, 'mood':y_axin} for y_axin, x_axin in zip(y_axis, x_axis)]  


