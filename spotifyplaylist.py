import requests
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
date = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD : ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}

response = requests.get(URL, headers = header)

soup = BeautifulSoup(response.text, "html.parser")
song_elements = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_elements]

CLIENT_ID = "096932aa7d294986a91b232b4e58a325"
CLIENT_SECRET = "797fd041ed734b3a8d9da8f8b1ed865d"

redirect_url = "http://127.0.0.1:5000/callback"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=redirect_url,
        show_dialog=True,
        scope="playlist-modify-private",
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

year = date.split("-")[0]
song_uris = []
for song in song_names:
    result = sp.search(
        q=f"track:{song} year:{year}",
        type="track",
        limit=1
    )
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"Found: {song}")
    except IndexError:
        print(f"Skipped: {song} not found.")

pprint(song_uris)

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)
print(f"Created playlist: {playlist["name"]}")

if len(song_uris) == 0:
    print("No songs to add!")

sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)
print("Songs added successfully!")







