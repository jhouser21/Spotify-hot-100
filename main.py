import requests
from bs4 import BeautifulSoup
from datetime import datetime
import spotipy
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"


def ask_date():
    playlist_date = input("What date would you like to make a playlist for? (YYYY-MM-DD): ")
    return playlist_date

try:
    will_you = ask_date()

    new_url = f"{URL}{will_you}"
    response = requests.get(new_url)
# website_html = response.text

# print(website_html)

    soup = BeautifulSoup(response.content, "html.parser")

    song_pull = soup.select("h3.c-title.a-no-trucate")
    song_names = [song.getText().strip() for song in song_pull]
    artist_names = soup.find_all("span", class_="a-no-trucate")

    print(song_names)
    print(artist_names)
except Exception as e:
    print("you a stink boy")
    print(e)
finally:
    print(will_you)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="1249445113954dbda1d7221c23ddbe05",
                                               client_secret="e4a4d667aaae451e952625a5545195b1",
                                               redirect_uri="https://codepen.io/Zo-/pen/gOmEQew",
                                               scope="playlist-modify-private"))

results = sp.search(q="weezer", limit=100)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
