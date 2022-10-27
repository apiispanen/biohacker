import requests
import urllib.request

suunto_primary = '3c38c88726c34d2bb6a869aa3c71dacb'
suunto_secondary = '20df26ff883b487db44f080cb44ad7e7'
suunto_client = 'afb4e4c8-af7d-4df7-b2f3-890dea0ad688'

response_type = 'token'
redirect_uri = self._get_uri()


url = 'https://cloudapi-oauth.suunto.com/oauth/authorize'

params = {
    'response_type':response_type,
    'client_id':suunto_client,
    'redirect_uri':redirect_uri
}
suunto_req = requests.get(url, params=params)

# suunto_login_screen = requests.post(suunto_req.url, params=params)
# with requests.Session() as s:
#     p = s.post(url, data=params)
#     # print the html returned or something more intelligent to see if it's a successful login page.
#     print(p.text)

# starturl = suunto_req.url
# res = urllib.request.urlopen(starturl)
# finalurl = res.geturl()
print(suunto_req.text)

