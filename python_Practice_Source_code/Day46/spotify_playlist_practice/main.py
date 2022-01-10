# 注意：这套代码应该是没有问题的，但是现在 billboard 网站改版，使用 class 类无法爬到原来的数据。
# 屏蔽了爬数据的代码，自己写了一个包含5首歌的数组，测试在spotify 中生成 playlist 成功

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
date = "2020-11-11"

# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
# soup = BeautifulSoup(response.text, "html.parser")
# song_names_spans = soup.find_all(id="title-of-a-story")
# song_names = [song.getText() for song in song_names_spans]
song_names = ["Mood", "Positions","Laugh Now Cry Later","Laugh Now Cry Later","I Hope"]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://lovethisworldbydong.com",
        client_id="7e1dfaa0a2164111af624fb5b83d0356",
        client_secret="b8109547644a4ab4ae24ea5e07487234",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)


# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(
        q=f"track:{song} year:{year}",
        type="track"
    )
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)