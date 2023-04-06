import torch
import whisper

# 載入模型
model = whisper.load_model("tiny")

# 讀取音頻檔案並將其裁剪或填充為30秒
audio = whisper.load_audio('audio/sample.mp3')
audio = whisper.pad_or_trim(audio)

# 計算對數梅爾頻譜圖並將其移動到與模型相同的設備上
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# 創建解碼選項
# options = whisper.DecodingOptions()
options = whisper.DecodingOptions(fp16 = False)

# 使用解碼函數
result = whisper.decode(model, mel, options)

# 打印識別出的文本
print(result.text)
