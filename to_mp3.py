# spotify API
# take a spotify playlist and grab every song from the playlist, append it to spotify_songs
import json
import webbrowser
import requests
import base64
from urllib.parse import urlencode
from dotenv import load_dotenv
import os

load_dotenv()

# grab env variables from .env file
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
spotify_id = os.getenv("SPOTIFY_ID")

print(f"client_id: {client_id}")
print(f"client_secret: {client_secret}")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

token = get_token()

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_user_playlists(token, spotify_id):
    url = "https://api.spotify.com/v1/users/"
    headers = get_auth_header(token)
    query = f"{spotify_id}/playlists"

    query_url = url + query
    result = requests.get(query_url, headers=headers)
    json_result = json.loads(result.content)
    print(json_result)

# print(token)

get_user_playlists(token, spotify_id)



# youtube API?
# take every song on the playlist and look it up on youtube, append it to yt_links (LIST)
# (need to determine how to choose which one)





# youtube -> spotify API
# convert song to mp3 and download it