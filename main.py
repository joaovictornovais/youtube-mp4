from pytube import YouTube
from pytube.exceptions import RegexMatchError

link = str(input("Enter the link of the video: "))

try:
    yt = YouTube(link)
    yt.streams.filter(file_extension='mp4').first().download()

    print("Download completed!")
except (RegexMatchError, ValueError):
    print("Invalid link")

