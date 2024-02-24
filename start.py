from dotenv import load_dotenv
import os, urls, download
import concurrent.futures

if __name__ == "__main__":
    n = int(input("Enter the number of videos to download: "))
    load_dotenv()
    playlist_url = os.getenv("PLAYLIST_URL")
    last_n_urls = urls.get_last_n_video_urls(playlist_url, n)
    print(f"Last {n} Video URLs:")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download.download_from_url, last_n_urls)

    print("Download and Conversion complete.")
    #input("Press Enter to exit...")