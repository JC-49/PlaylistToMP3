import os
import re
import eyed3
import trim

def get_artist_and_title(yt):
    title_parts = re.split(' - | – ', yt.title)
    if len(title_parts) > 1 and title_parts[1].strip().upper() not in os.getenv("TITLE_EXCEPTIONS").split(","):
        artist = yt.author  + '; ' +  title_parts[0]
        title = trim.remove_strings_from_title(' - '.join(title_parts[1:]))
    else:
        artist = yt.author
        title = trim.remove_strings_from_title(yt.title)
    return artist, title


def edit_metadata(mp3_file, artist, title):
    audiofile = eyed3.load(mp3_file)
    if (audiofile.tag == None):
        audiofile.initTag()
    audiofile.tag.artist = artist
    audiofile.tag.title = title
    audiofile.tag.save()