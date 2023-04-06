import openai
import os

# Read API key from file
with open("api_key.txt", "r") as f:
    api_key = f.read().strip()

# Configure the OpenAI library with your API key
openai.api_key = api_key

def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    return transcript.text

# Replace 'path_to_audio_file' with the path to the downloaded audio file
audio_file_path = 'audio/sample.mp3'
transcript = transcribe_audio(audio_file_path)

if transcript is not None:
    # Create output directory if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save transcript to a .txt file
    output_file_path = os.path.join(output_dir, "output_transcript.txt")
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    print(f"文字內容已保存到 {output_file_path} 檔案中。")
else:
    print("由於錯誤，未能生成文字檔案。")