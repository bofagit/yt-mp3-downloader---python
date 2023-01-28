from pytube import YouTube
import os

yt = YouTube(input("Enter the URL of the video you want to download to an mp3 file: "))

video = yt.streams.filter(only_audio=True).first()

#Change this to the directory you want to download to (I have it set to my downloads folder)
destination = "C:/Users/USER/Downloads"

out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)



print("Downloaded")
