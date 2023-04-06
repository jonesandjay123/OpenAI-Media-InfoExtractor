import whisper
import os

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

def main():
    file_path = 'audio/sample.mp3'
    output_dir = 'output'
    output_filename = 'output_transcript.txt'
    output_path = os.path.join(output_dir, output_filename)
    print("Transcribing audio...")
    transcription = transcribe_audio(file_path)
    print("\nTranscription:\n", transcription)

    with open(output_path, 'w') as f:
        f.write(transcription)

    print("Transcription saved to", output_path)

if __name__ == "__main__":
    main()