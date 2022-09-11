# timely_app_id = 'G0Eax-DCLxHeNEw1SZgDp83uYN-ygbJwj92IqfmAxJk'
# timely_app_secret = 'G0Eax-DCLxHeNEw1SZgDp83uYN-ygbJwj92IqfmAxJk'
# timely_app_callback = 'urn:ietf:wg:oauth:2.0:oob'


import requests
import json

# url = 'https://api.timelyapp.com/1.1/oauth/authorize'

### FIRST ATTEMPT BELOW
# params = {
#     'response_type':'code',
#     'redirect_uri':timely_app_callback,
#     'client_id':timely_app_id
# }

# r = requests.get(url, params = params)

# with open('html.html','w') as file:
#     file.write(r.text)

# # END FIRST ATTEMPT

file = open('timely_data.json', 'r',encoding='cp850')

timely_data = json.load(file)

# PRINT HEADERS
print([header for header,key in timely_data[0].items()])

for item in timely_data:
    # print( 'title: ', item['title'] )
    # print('decription: ', item['description'])
    # print('duration: ', item['duration'])
    print('date: ', item['date'])

    print("#####")

dates = list(set([item['date'] for item in timely_data]))
dates.sort()
titles = list(set([item['title'] for item in timely_data]))
print(dates)
