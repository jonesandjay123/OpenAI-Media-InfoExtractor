import openai
import os

# Set the language of the transcription
language = "zh"  # Use "en" for English and "zh" for Chinese
max_tokens = 3000  # max_tokens for gpt3.5 is 4096, but use 3950 to account for additional message tokens

# Read API key from file
with open("api_key.txt", "r") as f:
    api_key = f.read().strip()

# Configure the OpenAI library with your API key
openai.api_key = api_key

def transcribe_audio(file_path, language):
    with open(file_path, "rb") as audio_file:
        prompt = "，。！？" if language == "zh" else ",.!?"
        transcript = openai.Audio.transcribe("whisper-1", audio_file, prompt=prompt)

    return transcript.text

# Replace 'path_to_audio_file' with the path to the downloaded audio file
audio_file_path = 'audio/sample.mp3'
transcript = transcribe_audio(audio_file_path, language)

if transcript is not None:
    # Create output directory if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save transcript to a .txt file
    file_index = 0
    start = 0
    while start < len(transcript):
        end = start + max_tokens
        if end < len(transcript):
            end = transcript.rfind(' ', start, end)
            if end == -1:
                end = start + max_tokens

        output_file_path = os.path.join(output_dir, f"output_transcript{file_index}.txt")
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(transcript[start:end])

        print(f"文字內容已保存到 {output_file_path} 檔案中。")

        start = end + 1
        file_index += 1
else:
    print("由於錯誤，未能生成文字檔案。")