from pytube import Playlist
import re

def get_last_n_video_urls(playlist_url, n):
    playlist = Playlist(playlist_url)
    print(playlist.title)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    playlist._video_url_from_webpage = lambda x: "https://www.youtube.com" + playlist._js_to_json(x)

    n = min(n, len(playlist.video_urls))
    return [video_url for video_url in playlist.video_urls[:n]]

def get_all_video_urls(playlist_url):
    playlist = Playlist(playlist_url)
    print(playlist.title)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    playlist._video_url_from_webpage = lambda x: "https://www.youtube.com" + playlist._js_to_json(x)
    return playlist.video_urls