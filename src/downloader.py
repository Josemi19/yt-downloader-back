from pytube import YouTube
import os

def download_video(url):
    video_instance = YouTube(url)
    stream = video_instance.streams.get_by_itag(22)
    print(stream.download(output_path = f"{os.environ['UserProfile']}/Downloads"))
    return video_instance.title