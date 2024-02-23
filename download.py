import os
import eyed3
import re
import tempfile
from pytube import YouTube
from moviepy.editor import AudioFileClip
import shutil

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def download_from_url(url):
    output_path = os.getcwd() + "/output"
    temp_path = tempfile.mkdtemp()
    yt = YouTube(url)
    print(f"Downloading: {url} - {yt.title}")
    title_parts = yt.title.split(' - ')
    if len(title_parts) > 1 and title_parts[1].strip().upper() not in ['HARDSTYLE', 'FRENCHCORE', ':RE']:
        artist = yt.author  + '; ' +  title_parts[0]
        title = ' - '.join(title_parts[1:])
    else:
        artist = yt.author
        title = yt.title

    sanitized_title = sanitize_filename(yt.title)
    mp3_file = output_path + "/" + sanitized_title + ".mp3"

    # Check if the file already exists
    if os.path.exists(mp3_file):
        print(f"File {mp3_file} already exists. Skipping download.")
        return

    video_stream = yt.streams.filter(only_audio=True).first()
    video_file = video_stream.download(temp_path)  
    audio_clip = AudioFileClip(video_file)
   
    audio_clip.write_audiofile(mp3_file)

    # Delete the temporary directory
    shutil.rmtree(temp_path)

    # Edit MP3 metadata
    audiofile = eyed3.load(mp3_file)
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.artist = artist
    audiofile.tag.title = title
    audiofile.tag.save()