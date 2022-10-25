from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#  Spotify keys
Client_ID = "key"
Client_Secret = "key"
REDIRECT_URL = "https://example.com/callback"


date = input("In which year do you want to travel in ? Enter the date in format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
charts = response.text

soup = BeautifulSoup(charts, 'html.parser')
songs = soup.find_all(name="h3", class_="a-no-trucate")
song = [song.getText().strip() for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URL,
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]



