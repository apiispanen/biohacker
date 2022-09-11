timely_app_id = 'G0Eax-DCLxHeNEw1SZgDp83uYN-ygbJwj92IqfmAxJk'
timely_app_secret = 'G0Eax-DCLxHeNEw1SZgDp83uYN-ygbJwj92IqfmAxJk'
timely_app_callback = 'https://127.0.0.1:5500'


import requests

url = 'https://api.timelyapp.com/1.1/oauth/authorize'

params = {
    'response_type':'code',
    'redirect_uri':timely_app_callback,
    'client_id':timely_app_id
}

r = requests.get(url, params = params)


print(r.text)


# url = 'https://api.timelyapp.com/1.1/oauth/token'

# headers = {
#     "Content-Type": "application/json",
#     "api-key": apikey
# }

# params = {
#     'response_type':'code',
#     'redirect_uri':timely_app_callback,
#     'client_id':timely_app_id
# }

# r = requests.post(url, params = params)
# print(r.text)