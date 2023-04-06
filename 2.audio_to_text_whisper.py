import torch
import whisper
import os
import tqdm
import numpy as np

# 載入模型
model = whisper.load_model("tiny")

# 讀取音頻檔案
audio = whisper.load_audio('audio/sample.mp3')

# 計算音頻的總時間（秒）
total_duration = len(audio) / 16000

# 設定每個片段的持續時間（秒）
segment_duration = 30

# 計算需要多少個片段來處理整個音頻
num_segments = int(np.ceil(total_duration / segment_duration))

# 初始化一個空字符串，用於存儲所有片段的識別結果
full_transcript = ""

# 在循環外檢測語言
audio_segment = audio[:segment_duration * 16000]
mel = whisper.log_mel_spectrogram(audio_segment).to(model.device)
_, probs = model.detect_language(mel)
language = max(probs, key=probs.get)

# 創建解碼選項並指定語言
options = whisper.DecodingOptions(fp16=False, language=language)

# 分段處理音頻並添加進度條
for i in tqdm.tqdm(range(num_segments)):
    start = i * segment_duration * 16000
    end = (i + 1) * segment_duration * 16000

    # 裁剪音頻片段
    audio_segment = audio[start:end]

    # 確保音頻片段具有正確的形狀
    if audio_segment.shape[0] < segment_duration * 16000:
        audio_segment = np.pad(audio_segment, (0, segment_duration * 16000 - audio_segment.shape[0]))

    # 計算對數梅爾頻譜圖並將其移動到與模型相同的設備上
    mel = whisper.log_mel_spectrogram(audio_segment).to(model.device)

    # 使用解碼函數
    result = whisper.decode(model, mel, options)

    # 將片段的識別結果添加到完整文本中
    full_transcript += result.text + " "

# 確保 output 資料夾存在
if not os.path.exists('output'):
    os.makedirs('output')

# 寫入 output_transcript.txt 檔案
with open('output/output_transcript.txt', 'w') as file:
    file.write(full_transcript)
