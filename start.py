from pytube import Playlist
from dotenv import load_dotenv
import os, re

def get_last_n_video_urls(playlist_url, n=5):
    playlist = Playlist(playlist_url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    playlist._video_url_from_webpage = lambda x: "https://www.youtube.com" + playlist._js_to_json(x)
    return [video_url for video_url in playlist.video_urls[:n]]

if __name__ == "__main__":
    load_dotenv()
    playlist_url = os.getenv("PLAYLIST_URL")
    last_n_urls = get_last_n_video_urls(playlist_url, 5)
    print("Last 5 Video URLs:")
    for url in last_n_urls:
        print(url)
    #input("Press Enter to exit...")
