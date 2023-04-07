from pytube import YouTube
import os

# your_video_id = "ocUVg221CCQ" # Englisg Sample
# your_video_id = "L_Guz73e6fw" # OpenAI interview more than 25 MB
your_video_id = "1N0HFkzX5lY"
# your_video_id = "OIx3XDQc3D4" # Chinese Sample
url = "https://www.youtube.com/watch?v=" + your_video_id

def download_youtube_audio(youtube_url, destination='audio'):
    yt = YouTube(youtube_url)
    video = yt.streams.filter(only_audio=True).first()
    duration = yt.length

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = destination + '/sample.mp3'
    os.rename(out_file, new_file)

    return new_file, duration

downloaded_file, duration = download_youtube_audio(url)
yt = YouTube(url)

minutes, seconds = divmod(duration, 60)

print(f"{yt.title} 已成功下載，並匯出成檔名：{downloaded_file}")
print(f"視頻音頻的時間長度為：{duration} 秒 = {minutes}分{seconds}秒")