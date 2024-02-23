from pytube import Playlist
import re

def get_last_n_video_urls(playlist_url, n):
    playlist = Playlist(playlist_url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    playlist._video_url_from_webpage = lambda x: "https://www.youtube.com" + playlist._js_to_json(x)
    return [video_url for video_url in playlist.video_urls[:n]]