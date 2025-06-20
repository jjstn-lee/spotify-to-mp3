# spotify API
# take a spotify playlist and grab every song from the playlist, append it to spotify_songs
import webbrowser
import requests
import base64
from urllib.parse import urlencode
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(f"client_id: {client_id}")
print(f"client_secret: {client_secret}")

auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://127.0.0.1:8000/callback",
    "scope": "user-library-read"
}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

auth_code = os.getenv("AUTH_CODE")

print(f"auth_code: {auth_code}")

encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "authorization_code",
    "code": auth_code,
    "redirect_uri": "http://127.0.0.1:8000/callback"
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

token = r.json()
print("==")
print(token)
print("==")

user_headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}

user_params = {
    "limit": 50
}

user_tracks_response = requests.get("https://api.spotify.com/v1/me/tracks", params=user_params, headers=user_headers)

print(user_tracks_response.json())

# youtube API?
# take every song on the playlist and look it up on youtube, append it to yt_links (LIST)
# (need to determine how to choose which one)





# youtube -> spotify API
# convert song to mp3 and download it