from pytube import YouTube

def download_from_url(url, output_path):
    yt = YouTube(url)
    yt.streams.filter(only_audio=True).first().download(output_path)