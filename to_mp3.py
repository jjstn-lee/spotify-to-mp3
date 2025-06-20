# spotify API
# take a spotify playlist and grab every song from the playlist, append it to spotify_songs
import requests
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


print(f"client_id: {client_id}")
print(f"client_secret: {client_secret}")




# youtube API?
# take every song on the playlist and look it up on youtube, append it to yt_links (LIST)
# (need to determine how to choose which one)





# youtube -> spotify API
# convert song to mp3 and download it