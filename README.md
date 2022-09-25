# Biohacker
My initial tests at a personal mood tracker. 

### To find the deployed online application, please see: <a href="https://apiispanen-biohacker-stream-gtgyag.streamlitapp.com/">The Streamlit App</a>

## Methods
Biohacker is a database used to track my moods. As I give myself a scale of 1-5 (found here <a href="https://docs.google.com/forms/u/0/d/e/1FAIpQLSfUoOkohnvjDoSDwvT945V7QfgA_v4rFHXgsgPkhfqJrjOLGQ/formResponse">here</a>), my tracker will integrate with an algorithm designed to combine this data with any activity, financial and locational data that I have that could play into this. Have I been buying too much fast food? Do I visit people who I don't enjoy being around? Does  sitting inside for 48 hours straight really contribute to my mood? I'll add more variables for analysis as I go, but this is my personal experimental project. <br><br>
This is my day 1.<br><br> 

## Data Extracters

### Pull_Sheet.py
### Health.py
### Weather_Pull.py
### collect_gyms.py


## Packages Used
- Google Forms
- Python Libraries: Oauth2client, plotly, numpy, streamlit (for data vis renderings)


## Applications Used for Data Collection
- Screentime: Offscreen
- Apple Health: Account -> "Export All Health Data"
- Chase Credit Card: Download all records as CSV
- Gym Visits & Mood: "Manually" entered
- Weather API: Meteo Open API

## NOTE TO SELF - CREATE MOOD REGRESSION WITH ALL VARIABLES
## Next up - regression with gym visits & mindful minutes
## Also look at screentime pulls


