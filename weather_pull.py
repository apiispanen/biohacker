import requests
from pprint import pprint
import pandas as pd
from datetime import datetime as dt

params = {
    'latitude': '40.284760',
    'longitude': '-76.649261',
    'start_date':'2022-09-01',
    'end_date':str(f"{int(dt.now().year):02d}")+'-'+str(f"{int(dt.now().month):02d}")+'-'+str(f"{int(dt.now().day):02d}"),
    'hourly':['apparent_temperature', 'cloudcover','precipitation'],
    'temperature_unit':'fahrenheit',
    'precipitation_unit':'inch',
    'timeformat':'unixtime'
}

url = 'https://archive-api.open-meteo.com/v1/era5'

pull = requests.get(url, params=params).json()

time = [dt.fromtimestamp(int(thing)).strftime('%Y-%m-%d')  for thing in pull['hourly']['time']]
apparent_temperature = pull['hourly']['apparent_temperature']
cloudcover = pull['hourly']['cloudcover']
precipitation = pull['hourly']['precipitation']

df = pd.DataFrame(
    zip(time,apparent_temperature,cloudcover,precipitation),
    columns =['timestamp', 'Apparent Temperature', 'Cloud Cover', 'Precipitation']
)

weather_df = df.groupby(by=['timestamp']).mean()