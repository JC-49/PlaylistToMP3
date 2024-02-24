import os
import re
import tempfile
import shutil
import metadata, trim
from pytube import YouTube
from moviepy.editor import AudioFileClip

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def download_video(yt, temp_path):
    video_stream = yt.streams.filter(only_audio=True).first()
    return video_stream.download(temp_path)

def convert_to_mp3(video_file, mp3_file):
    audio_clip = AudioFileClip(video_file)
    audio_clip.write_audiofile(mp3_file)

def download_from_url(url):
    #output_path = os.getcwd() + "/output"
    output_path = os.getenv("OUTPUT_PATH")
    temp_path = tempfile.mkdtemp()
    yt = YouTube(url)
    
    artist, title = metadata.get_artist_and_title(yt)
    sanitized_title = sanitize_filename(trim.remove_strings_from_title(yt.title))
    mp3_file = output_path + "/" + sanitized_title + ".mp3"

    if os.path.exists(mp3_file):
        print(f"File {mp3_file} already exists. Skipping download.")
        return
    else:
        print(f"Downloading: {url} - {yt.title}")

    video_file = download_video(yt, temp_path)
    convert_to_mp3(video_file, mp3_file)
    shutil.rmtree(temp_path)
    metadata.edit_metadata(mp3_file, artist, title)