# Gamefinder
A simple code in pyhton for test the IGDB API.

For use this code you have to install 3 libs for python:
```py
pip install requets
pip install igdb-api-v4
pip install pytz
```
And don't forget to change "YOUR_CLIENT_ID" and "YOUR_CLIENT_SECRET" for the data that you can take in the Twitch Developers, in this part of code:
```py
r = requests.post('https://id.twitch.tv/oauth2/token', params={
    'grant_type':'client_credentials',
    'client_id' : 'YOUR_CLIENT_ID',
    'client_secret': 'YOUR_CLIENT_SECRET'
})

token = r.json()['access_token']

wrapper = IGDBWrapper("YOUR_CLIENT_SECRET", token)
```
For read more about IGDB API and how to use it, go to https://www.igdb.com/api.
