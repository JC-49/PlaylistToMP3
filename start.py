from dotenv import load_dotenv
import os, urls, download
import concurrent.futures

if __name__ == "__main__":
    load_dotenv()
    mode = os.getenv("MODE")
    playlist_urls = os.getenv("PLAYLIST_URLS")
    for playlist_url in playlist_urls.split(","):
        if(mode=="all"):
            video_urls = urls.get_all_video_urls(playlist_url)
        else:
            n = int(input("Enter the number of videos to download: "))
            video_urls = urls.get_last_n_video_urls(playlist_url, n)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(download.download_from_url, video_urls)

    print("Download and Conversion complete.")
    input("Press Enter to exit...")