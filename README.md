# Biohacker
My personal mood tracker & predictor. 

### To find the deployed online application, please see: <a href="https://apiispanen-biohacker-stream-gtgyag.streamlitapp.com/">The Deployed Streamlit Webapp</a>
### To learn more about this project, please see: <a href="https://medium.com/@andrewpiispanen/solutions-to-a-broken-mind-200ea7ac1598">Medium Post</a><br><br>

## Overview
Biohacker is a database used to track my moods. As I give myself a scale of 1-5 (found here <a href="https://docs.google.com/forms/u/0/d/e/1FAIpQLSfUoOkohnvjDoSDwvT945V7QfgA_v4rFHXgsgPkhfqJrjOLGQ/formResponse">here</a>), my tracker will integrate with an algorithm designed to combine this data with any activity, financial and locational data that I have that could play into this. Have I been buying too much take out food? Do I visit people who I don't enjoy being around? Does  sitting inside for 48 hours straight really contribute to my mood? In this process, I want to uncover everything about myself - getting down to the deepest parts of me I didn't know existed. I'll add as many variables for analysis as I go, but this is a personal experiment on myself. <br><br>

## Purpose
In order to find the biggest causes to my mood changes, Biohacker was designed to log my mood while analyzing all other environmental and personal data that has been collected on my behalf during the day.

### Data Being Collected
Currently, there are two types of data being collected in this series:
1. <b>Active Data</b>:
Active data requires manual input and consistent logging. In the case of this study on myself, this is my mood. Any other data that I have to pick up a device to add to during the day (i.e. "What activities are making me feel this way today?") is also considered to be active. The mood will serve as <i>the most important predictor in this study</i>.
2. <b>Passive Data</b>: 
Passive data is all the background noise that gets collected in our phones. This is the app data, the step counts, the number of times your phone was picked up. All of this gets logged somewhere, and Biohacker's job is to reconcile this all in one place. Essentially, you become a part of your own study here.

<br>

## Data Extractors

### Pull_Sheet.py
This is the main sheet that pulls our Google Forms Data & our current gym log. As the interface develops, so will this portion of the database. As of now, a dataframe of three columns are returned:
- timestamp
- mood: The 1-5 scale that was actively entered into how you feel.
- gym: a binary (0 or 1) number that dictates if on this date the gym was visited.

### Health.py
This data is pulled from Apple Health. Go to Apple Health App, click on your account and "export all data" to obtain your own information. The data is exported as an XML file, and then health.py reads the data to splice the data and reconfigure it to the different types of data present:
- Mindful minutes: The daily sum taken from the duration (endDate - startDate)
- Total steps: The daily sum of steps taken.
- Total Flights Climbed: The daily sum of flights climbed.
- Total standing: The total percent of standing time - may not be useful as a variable.
- Total walk-run: The total percent of walk-run time - may not be useful as a variable.

### weather_pull.py
Using the free Open API <a href="https://open-meteo.com/en">open-meteo</a>, this script is able to grab us these variables for each day we analyze:
- apparent_temperature: The "realfeel" temperature, when factoring in misc. variables such as windspeed and humidity. 
- cloudcover: Percentage of the total cloud coverage that day.
- precipitation: Including rain and snow

### pickup_pull.py
Combining the app <a href="https://apps.apple.com/us/app/offscreen-less-screen-time/id1474340105">Offscreen</a> with the power of Python's Pandas library, this script combines the exported data from the free application into 2 insights:
- Total count of pickups each day
- Total screentime logged

## Packages Used
- Google Forms
- IFTTT (for daily pings of Google Forms)
- Python Libraries: Oauth2client, gspread, plotly, numpy, streamlit (for data vis renderings), lxml, requests, pandas, datetime, pprint, numpy, sklearn 
- Jupyter Notebooks


## Applications Used for Data Collection
Data Type: Application Used
- Screentime: Offscreen
- Apple Health: Account -> "Export All Health Data"
- Chase Credit Card: Download all records as CSV
- Gym Visits & Mood: "Manually" entered via Google Forms and gspread connection
- Weather API: Meteo Open API

## NEXT STEPS: ADD SLEEP TIME BASED ON LAST DAILY PICKUP AND FIRST MORNING PICKUP
## Interface design & strongest P values.
## Add methods to the README