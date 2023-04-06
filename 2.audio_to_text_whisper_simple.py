import torch
import whisper
import os

# 載入模型
model = whisper.load_model("tiny")  # tiny, base, small, medium, large

# 識別音頻並獲得文本
result = model.transcribe('audio/sample.mp3')

# 確保 output 資料夾存在
if not os.path.exists('output'):
    os.makedirs('output')

# 寫入 output_transcript.txt 檔案
with open('output/output_transcript.txt', 'w') as file:
    file.write(result["text"])
