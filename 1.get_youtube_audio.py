from pytube import YouTube
import os
  
# your_video_id = "ocUVg221CCQ" # Englisg Sample
your_video_id = "L_Guz73e6fw" # OpenAI interview more than 25 MB
# your_video_id = "OIx3XDQc3D4" # Chinese Sample
url = "https://www.youtube.com/watch?v=" + your_video_id

# url input from user
# yt = YouTube(
#     str(input("Enter the URL of the video you want to download: \n>> ")))
yt = YouTube(str(url))
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
# print("Enter the destination (leave blank for current directory)")
# destination = str(input(">> ")) or '.'
destination = 'audio'
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
# new_file = base + '.mp3'
new_file = destination + '/sample.mp3'
os.rename(out_file, new_file)
  
# result of success
print(yt.title + " has been successfully downloaded.")