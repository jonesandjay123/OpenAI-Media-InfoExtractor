import openai
import os

language = "zh"  # Use "en" for English and "zh" for Chinese

# Read API key from file
with open("api_key.txt", "r") as f:
    openai.api_key = f.read().strip()

# Print the API key to verify it's being read correctly
print(f"API Key: {openai.api_key}")

output_dir = "output"

def summarize_file(file_path):
    # 讀取轉錄文本
    with open(file_path, "r") as file:
        transcript = file.read()

    # 調用GPT-3.5，提取重點信息並生成摘要
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Please summarize the following transcript into bullet points{' by traditional chinese' if language == 'zh' else ''}: {transcript}"}
        ]
    )

    # 獲取摘要
    summary = response.choices[0].message['content']

    # 將摘要添加到原始轉錄文件中
    with open(file_path, "a") as file:
        file.write("\n------\n\nSummary:\n\n")
        file.write(summary)

# Loop through all files in the output directory and summarize them
for file_name in os.listdir(output_dir):
    if file_name.startswith("output_transcript"):
        file_path = os.path.join(output_dir, file_name)
        summarize_file(file_path)
