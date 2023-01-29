import os

try:
  from pytube import YouTube
except:
  answer = input("pytube was not detected, would you like to install it with pip? (y/N): ")
  if "y" in answer.lower():
    os.system("pip install pytube")
    from pytube import YouTube
  else:
    print("This program will not work without pytube, exiting...")
    exit(1)

import getpass

yt = YouTube(input("Enter the URL of the video you want to download to an mp3 file: "))

video = yt.streams.filter(only_audio=True).first()

#Change this to the directory you want to download to (I have it set to my downloads folder)
destination = f"C:\\Users\\{getpass.getuser()}\\Downloads"

out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)



print("Downloaded!")
input()
