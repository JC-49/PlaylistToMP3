from dotenv import load_dotenv
import os, urls, download
import concurrent.futures

def download_url(url):
    print(f"Downloading {url}")
    output_path = os.getcwd() + "/output"
    download.download_from_url(url, output_path)

if __name__ == "__main__":
    n = 5
    load_dotenv()
    playlist_url = os.getenv("PLAYLIST_URL")
    last_n_urls = urls.get_last_n_video_urls(playlist_url, n)
    print(f"Last {n} Video URLs:")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_url, last_n_urls)

    print("Download complete.")
    #input("Press Enter to exit...")