import os
import sys
import whisper
from pathlib import Path

model = whisper.load_model("base")

def transcribe_audio_with_progress(file_path):

    # Load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(file_path)
    audio = whisper.pad_or_trim(audio)

    # Make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    options = whisper.DecodingOptions()

    # Call whisper.decode()
    result = whisper.decode(model, mel, options)

    return result.text

def main():
    file_path = "audio/sample.mp3"
    output_path = Path(file_path).with_suffix('.txt')

    print("Transcribing audio...")
    transcription = transcribe_audio_with_progress(file_path)

    with open(output_path, "w") as output_file:
        output_file.write(transcription)

    print(f"Transcription saved to {output_path}")

if __name__ == "__main__":
    main()
